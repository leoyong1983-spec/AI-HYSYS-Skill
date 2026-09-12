from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from hysys_version import HysysVersionError, resolve_hysys_target, verify_reported_version


def registry(versions=("14", "15"), default="14"):
    values = {f"HYSYS.Application.V{v}.0\\CLSID": "{" + v + "}" for v in versions}
    if default:
        values[r"HYSYS.Application\CLSID"] = "{" + default + "}"

    def read(path):
        if path not in values:
            raise FileNotFoundError(path)
        return values[path]

    return read


class VersionSelectionTests(unittest.TestCase):
    def test_explicit_version_beats_generic_default(self):
        for version in ("14", "15"):
            target = resolve_hysys_target(version, read_registry=registry(default="14"))
            self.assertEqual(target.major, version)
            self.assertEqual(target.prog_id, f"HYSYS.Application.V{version}.0")

    def test_auto_follows_registered_default(self):
        self.assertEqual(resolve_hysys_target(read_registry=registry(default="14")).major, "14")

    def test_auto_uses_only_installed_supported_version(self):
        self.assertEqual(resolve_hysys_target(read_registry=registry(("15",), None)).major, "15")

    def test_auto_with_ambiguous_default_fails(self):
        with self.assertRaises(HysysVersionError):
            resolve_hysys_target(read_registry=registry(default=None))

    def test_requested_missing_version_does_not_fall_back(self):
        with self.assertRaises(HysysVersionError):
            resolve_hysys_target("14", read_registry=registry(("15",)))

    def test_no_supported_installation_fails(self):
        with self.assertRaises(HysysVersionError):
            resolve_hysys_target(read_registry=registry((), None))

    def test_legacy_override_is_honored(self):
        target = resolve_hysys_target(registered_prog_id="HYSYS.Application.V15.0", read_registry=registry())
        self.assertEqual(target.major, "15")

    def test_conflicting_or_unsupported_overrides_fail(self):
        for kwargs in ({"version": "14", "prog_id": "HYSYS.Application.V15.0"},
                       {"version": "16"}, {"prog_id": "Other.Application"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(HysysVersionError):
                resolve_hysys_target(**kwargs, read_registry=registry())

    def test_product_version_is_distinct_from_internal_build(self):
        for major, build in (("14", "40.0"), ("15", "41.0")):
            verify_reported_version(f"Aspen HYSYS Version {major} ({build})", resolve_hysys_target(major, read_registry=registry()))

    def test_wrong_or_unknown_reported_version_fails(self):
        target = resolve_hysys_target("15", read_registry=registry())
        for reported in ("Aspen HYSYS Version 14 (40.0)", "unknown", "41.0"):
            with self.subTest(reported=reported), self.assertRaises(HysysVersionError):
                verify_reported_version(reported, target)


class ActivationRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Isolated stand-ins keep the launch contract testable on Linux CI.
        client = types.ModuleType("win32com.client")
        client.DispatchEx = Mock()
        client.GetActiveObject = Mock()
        package = types.ModuleType("win32com")
        package.client = client
        stubs = {"pythoncom": Mock(), "winreg": Mock(), "win32com": package, "win32com.client": client}
        spec = importlib.util.spec_from_file_location("version_test_automation", Path(__file__).resolve().parents[1] / "scripts/hysys_automation.py")
        cls.mod = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {**stubs, spec.name: cls.mod}):
            spec.loader.exec_module(cls.mod)

    def session(self, version):
        session = self.mod.HysysCaseSession(self.mod.HysysLaunchOptions(hysys_version=version, startup_retries=0))
        session.target = resolve_hysys_target(version, read_registry=registry())
        return session

    def test_activation_always_uses_selected_version(self):
        for version in ("14", "15"):
            session = self.session(version)
            app = Mock(Version=f"Aspen HYSYS Version {version}")
            with patch.object(self.mod, "GetActiveObject", side_effect=OSError), patch.object(self.mod, "DispatchEx", return_value=app) as dispatch:
                self.assertIs(session._launch_application(), app)
                dispatch.assert_called_once_with(f"HYSYS.Application.V{version}.0")

    def test_existing_session_is_not_quit(self):
        session = self.session("14")
        app = Mock(Version="Aspen HYSYS Version 14 (40.0)")
        with patch.object(self.mod, "GetActiveObject", return_value=app), patch.object(self.mod, "DispatchEx") as dispatch:
            session.app = session._launch_application()
            session.close_app()
            dispatch.assert_not_called()
            app.Quit.assert_not_called()

    def test_wrong_version_is_rejected_before_setting_preferences(self):
        session = self.session("15")
        app = Mock(Version="Aspen HYSYS Version 14 (40.0)")
        with patch.object(self.mod, "GetActiveObject", side_effect=OSError), patch.object(self.mod, "DispatchEx", return_value=app), patch.object(session, "_launch_registered_server_and_attach") as fallback:
            with self.assertRaises(HysysVersionError):
                session._launch_application()
            fallback.assert_not_called()
            app.ChangePreferencesToMinimizePopupWindows.assert_not_called()

    def test_fallback_uses_same_registry_and_rot_version(self):
        session = self.session("15")
        app = Mock(Version="Aspen HYSYS Version 15 (41.0)")
        with patch.object(self.mod, "registered_local_server_command", return_value=(Path("HYSYS.exe"), ["/Automation"])) as command, patch.object(self.mod.subprocess, "Popen"), patch.object(self.mod, "GetActiveObject", return_value=app) as attach:
            self.assertIs(session._launch_registered_server_and_attach(OSError()), app)
            command.assert_called_once_with("HYSYS.Application.V15.0")
            attach.assert_called_once_with("HYSYS.Application.V15.0")


class ReadinessRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("version_test_readiness", Path(__file__).resolve().parents[1] / "scripts/hysys_readiness_check.py")
        cls.mod = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"winreg": Mock(), spec.name: cls.mod}):
            spec.loader.exec_module(cls.mod)

    def test_legacy_prog_id_controls_actual_readiness_launch(self):
        for major in ("14", "15"):
            target = resolve_hysys_target(major, read_registry=registry())
            with tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / "report.json"
                argv = ["readiness", "--prog-id", target.prog_id, "--output", str(output)]
                with patch.object(sys, "argv", argv), patch.object(self.mod.platform, "system", return_value="Windows"), patch.object(self.mod, "check_pywin32", return_value=True), patch.object(self.mod, "check_registry", return_value={}), patch.object(self.mod, "resolve_hysys_target", return_value=target) as resolve, patch.object(self.mod, "run_launch_check", return_value={}) as launch, redirect_stdout(io.StringIO()):
                    self.assertEqual(self.mod.main(), 0)
                resolve.assert_called_once_with("auto", prog_id=target.prog_id)
                self.assertEqual(launch.call_args.kwargs["prog_id"], target.prog_id)
                self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["selected_hysys_version"], major)

    def test_selection_failure_blocks_launch(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            with patch.object(sys, "argv", ["readiness", "--output", str(output)]), patch.object(self.mod, "check_pywin32", return_value=True), patch.object(self.mod, "resolve_hysys_target", side_effect=HysysVersionError("ambiguous")), patch.object(self.mod, "run_launch_check") as launch, redirect_stdout(io.StringIO()):
                self.assertEqual(self.mod.main(), 1)
            launch.assert_not_called()


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import argparse
import json
import platform
import sys
import tempfile
import time
import winreg
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


def add(checks: list[CheckResult], name: str, status: str, detail: str) -> None:
    checks.append(CheckResult(name=name, status=status, detail=detail))


def query_default_value(root, path: str) -> str:
    with winreg.OpenKey(root, path) as key:
        value, _ = winreg.QueryValueEx(key, "")
    return str(value)


def parse_local_server_command(command: str) -> tuple[str, list[str]]:
    marker = ".exe"
    marker_index = command.lower().find(marker)
    if marker_index < 0:
        raise ValueError(f"cannot find .exe in LocalServer32 value: {command}")
    exe = command[: marker_index + len(marker)].strip().strip('"')
    args = command[marker_index + len(marker) :].strip().split()
    return exe, args or ["/Automation"]


def check_pywin32(checks: list[CheckResult]) -> bool:
    try:
        import pythoncom  # noqa: F401
        import win32com.client  # noqa: F401
    except Exception as exc:
        add(
            checks,
            "pywin32",
            "fail",
            f"pythoncom/win32com import failed under {sys.executable}: {exc}",
        )
        return False
    add(checks, "pywin32", "ok", f"pythoncom/win32com import ok under {sys.executable}")
    return True


def check_registry(checks: list[CheckResult], prog_id: str) -> dict:
    registry: dict[str, str | list[str]] = {}
    try:
        clsid = query_default_value(winreg.HKEY_CLASSES_ROOT, rf"{prog_id}\CLSID")
        command = query_default_value(
            winreg.HKEY_CLASSES_ROOT, rf"CLSID\{clsid}\LocalServer32"
        )
        exe, args = parse_local_server_command(command)
        registry = {"prog_id": prog_id, "clsid": clsid, "local_server": command, "exe": exe, "args": args}
        status = "ok" if Path(exe).exists() else "fail"
        add(checks, "com_registry", status, json.dumps(registry, ensure_ascii=False))
    except Exception as exc:
        add(checks, "com_registry", "fail", f"{prog_id} registry lookup failed: {exc}")
    return registry


def run_launch_check(
    checks: list[CheckResult],
    *,
    visible: bool,
    create_smoke_case: bool,
    keep_smoke_case: bool,
) -> dict:
    from hysys_automation import HysysCaseSession, HysysLaunchOptions, make_temp_case_path

    smoke: dict[str, str] = {}
    started = time.monotonic()
    try:
        with HysysCaseSession(HysysLaunchOptions(visible=visible)) as hysys:
            version = hysys.version
            add(
                checks,
                "hysys_launch",
                "ok",
                f"{version}; launch+attach in {time.monotonic() - started:.1f} s",
            )
            smoke["version"] = version
            if create_smoke_case:
                case_path = make_temp_case_path("hysys_readiness_smoke")
                hysys.create_case(
                    case_path,
                    "HYSYS readiness smoke",
                    "Minimal case created by AI-HYSYS-Skill readiness check.",
                )
                hysys.save_case()
                add(checks, "case_create_save", "ok", str(case_path))
                smoke["smoke_case"] = str(case_path)
                if not keep_smoke_case:
                    hysys.close_case()
                    try:
                        case_path.unlink()
                        add(checks, "case_cleanup", "ok", str(case_path))
                    except Exception as exc:
                        add(checks, "case_cleanup", "warn", f"{case_path}: {exc}")
        return smoke
    except Exception as exc:
        add(checks, "hysys_launch", "fail", str(exc))
        return smoke


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Aspen HYSYS COM readiness.")
    parser.add_argument("--prog-id", default="HYSYS.Application.V15.0")
    parser.add_argument("--skip-launch", action="store_true", help="Only check Python and COM registry.")
    parser.add_argument("--visible", action="store_true", help="Show HYSYS while testing launch.")
    parser.add_argument("--create-smoke-case", action="store_true", help="Create and save a minimal HYSYS case.")
    parser.add_argument("--keep-smoke-case", action="store_true", help="Do not delete the smoke case.")
    parser.add_argument(
        "--output",
        default=str(Path(tempfile.gettempdir()) / "ai_hysys_readiness_report.json"),
        help="JSON report path.",
    )
    args = parser.parse_args()

    checks: list[CheckResult] = []
    add(checks, "platform", "ok" if platform.system() == "Windows" else "fail", platform.platform())
    add(checks, "python", "ok", sys.executable)
    pywin32_ok = check_pywin32(checks)
    registry = check_registry(checks, args.prog_id)

    smoke: dict = {}
    if not args.skip_launch and pywin32_ok:
        smoke = run_launch_check(
            checks,
            visible=args.visible,
            create_smoke_case=args.create_smoke_case,
            keep_smoke_case=args.keep_smoke_case,
        )

    payload = {
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "repository": str(ROOT),
        "registry": registry,
        "smoke": smoke,
        "checks": [asdict(check) for check in checks],
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    for check in checks:
        print(f"{check.status.upper():4} {check.name}: {check.detail}")
    print(f"Report: {output}")

    return 1 if any(check.status == "fail" for check in checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())

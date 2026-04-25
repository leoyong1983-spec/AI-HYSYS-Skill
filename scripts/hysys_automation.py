from __future__ import annotations

import contextlib
import os
import shutil
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import pythoncom
from win32com.client import DispatchEx


class HysysAutomationError(RuntimeError):
    """Raised when the HYSYS COM automation layer fails."""


@dataclass(slots=True)
class HysysLaunchOptions:
    visible: bool = False
    suppress_popups: bool = True
    startup_retries: int = 2
    startup_retry_delay_s: float = 1.0


@dataclass(frozen=True, slots=True)
class SpreadsheetCellBinding:
    """A stable tagged-IO binding for a HYSYS spreadsheet cell."""

    spreadsheet: str
    column: int
    row: int
    label: str = ""
    unit: str = ""


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def copy_file_stable(src: Path, dst: Path) -> Path:
    """Copy via Python stdlib to avoid shell/path encoding issues."""
    _ensure_parent(dst)
    shutil.copy2(src, dst)
    return dst


def stage_case_for_open(src: Path, staged_name: str = "hysys_stage_case.hsc") -> Path:
    """Stage a case under an ASCII temp path before reopening it with HYSYS."""
    staged_path = Path(tempfile.gettempdir()) / staged_name
    copy_file_stable(src, staged_path)
    return staged_path


def _needs_ascii_staging(path: Path) -> bool:
    try:
        str(path).encode("ascii")
        return False
    except UnicodeEncodeError:
        return True


class HysysCaseSession:
    """Small safety wrapper around `HYSYS.Application` COM automation."""

    def __init__(self, options: HysysLaunchOptions | None = None) -> None:
        self.options = options or HysysLaunchOptions()
        self.app = None
        self.case = None
        self._case_path: Path | None = None
        self._com_initialized = False

    def __enter__(self) -> "HysysCaseSession":
        self._initialize_com()
        self.app = self._launch_application()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close_case()
        self.close_app()
        self._uninitialize_com()

    def _initialize_com(self) -> None:
        pythoncom.CoInitialize()
        self._com_initialized = True

    def _uninitialize_com(self) -> None:
        if self._com_initialized:
            pythoncom.CoUninitialize()
            self._com_initialized = False

    def _launch_application(self):
        last_error: Exception | None = None
        for attempt in range(1, self.options.startup_retries + 2):
            try:
                app = DispatchEx("HYSYS.Application")
                app.Visible = self.options.visible
                with contextlib.suppress(Exception):
                    app.ChangePreferencesToMinimizePopupWindows(
                        self.options.suppress_popups
                    )
                return app
            except Exception as exc:  # pragma: no cover - COM specific
                last_error = exc
                if attempt <= self.options.startup_retries:
                    time.sleep(self.options.startup_retry_delay_s)
        raise HysysAutomationError(
            f"Unable to launch HYSYS.Application via COM: {last_error}"
        )

    @property
    def version(self) -> str:
        if self.app is None:
            raise HysysAutomationError("HYSYS application is not running.")
        return str(self.app.Version)

    def create_case(self, temp_case_path: Path, case_name: str, description: str):
        if self.app is None:
            raise HysysAutomationError("HYSYS application is not running.")
        _ensure_parent(temp_case_path)
        if temp_case_path.exists():
            temp_case_path.unlink()
        self.case = self.app.SimulationCases.Add(str(temp_case_path))
        self._case_path = temp_case_path
        self.case.Name = case_name
        self.case.Description = description
        return self.case

    def open_case(self, case_path: Path):
        if self.app is None:
            raise HysysAutomationError("HYSYS application is not running.")
        open_path = case_path
        if case_path.suffix.lower() == ".hsc" and _needs_ascii_staging(case_path):
            open_path = stage_case_for_open(case_path, staged_name=case_path.name.encode("ascii", "ignore").decode("ascii") or "staged_case.hsc")
        self.case = self.app.SimulationCases.Open(str(open_path))
        self._case_path = open_path
        return self.case

    def configure_peng_robinson_basis(self, components: Sequence[str]) -> None:
        if self.case is None:
            raise HysysAutomationError("No open HYSYS case to configure.")
        basis = self.case.BasisManager
        basis.FluidPackages.Add("Basis-1")
        fluid_package = basis.FluidPackages.Item("Basis-1")
        fluid_package.PropertyPackageName = "PengRob"
        component_list = basis.ComponentLists.Item("Component List - 1")
        for component in components:
            component_list.Components.Add(component)
        fluid_package.ComponentList = component_list
        basis.EndBasisChange()

    def add_material_stream(self, name: str, description: str):
        flowsheet = self._flowsheet()
        stream = flowsheet.MaterialStreams.Add(name)
        stream.StreamDescription = description
        return stream

    def add_energy_stream(self, name: str):
        return self._flowsheet().EnergyStreams.Add(name)

    def add_operation(self, name: str, op_type: str):
        return self._operations().Add(name, op_type)

    def get_operation(self, name: str):
        return self._operations().Item(name)

    def get_spreadsheet(self, name: str):
        return self.get_operation(name)

    def get_spreadsheet_cell(self, binding: SpreadsheetCellBinding):
        spreadsheet = self.get_spreadsheet(binding.spreadsheet)
        return spreadsheet.Cell(binding.column, binding.row)

    def read_spreadsheet_cell(self, binding: SpreadsheetCellBinding):
        return self.get_spreadsheet_cell(binding).CellValue

    def write_spreadsheet_cell(self, binding: SpreadsheetCellBinding, value) -> None:
        self.get_spreadsheet_cell(binding).CellValue = value

    @property
    def solver(self):
        if self.case is None:
            raise HysysAutomationError("No open HYSYS case.")
        return self.case.Solver

    def set_solver_enabled(self, enabled: bool) -> None:
        self.solver.CanSolve = enabled

    def wait_for_solver_idle(
        self,
        *,
        timeout_s: float = 120.0,
        poll_interval_s: float = 0.05,
    ) -> None:
        deadline = time.monotonic() + timeout_s
        while bool(self.solver.IsSolving):
            if time.monotonic() >= deadline:
                raise HysysAutomationError(
                    f"HYSYS solver did not become idle within {timeout_s} seconds."
                )
            time.sleep(poll_interval_s)

    def batch_write_spreadsheet_cells(
        self,
        updates: Sequence[tuple[SpreadsheetCellBinding, object]],
        *,
        wait_timeout_s: float = 120.0,
    ) -> None:
        """Pause solver, apply tagged spreadsheet updates, then solve once."""
        self.set_solver_enabled(False)
        try:
            for binding, value in updates:
                self.write_spreadsheet_cell(binding, value)
        finally:
            self.set_solver_enabled(True)
        self.wait_for_solver_idle(timeout_s=wait_timeout_s)

    def add_feed_to_operation(self, operation, stream) -> None:
        operation.Feeds.Add(stream)

    def save_case(self) -> None:
        if self.case is None:
            raise HysysAutomationError("No open HYSYS case to save.")
        self.case.Save()

    def save_case_as(self, destination: Path) -> Path:
        if self.case is None:
            raise HysysAutomationError("No open HYSYS case to save.")
        if self._case_path is None:
            raise HysysAutomationError("Current case path is unknown.")
        self.save_case()
        return copy_file_stable(self._case_path, destination)

    def close_case(self) -> None:
        if self.case is not None:
            with contextlib.suppress(Exception):
                self.case.Close()
            self.case = None
            self._case_path = None

    def close_app(self) -> None:
        if self.app is not None:
            with contextlib.suppress(Exception):
                self.app.Quit()
            self.app = None

    def _flowsheet(self):
        if self.case is None:
            raise HysysAutomationError("No open HYSYS case.")
        return self.case.Flowsheet

    def _operations(self):
        flowsheet = self._flowsheet()
        operations = getattr(flowsheet, "Operations", None)
        if operations is None:
            raise HysysAutomationError("Flowsheet does not expose Operations.")
        return operations


def make_temp_case_path(prefix: str = "hysys_case") -> Path:
    temp_dir = Path(tempfile.gettempdir())
    return temp_dir / f"{prefix}_{int(time.time())}.hsc"


def set_stream_state(
    stream,
    *,
    temperature_c: float | None = None,
    pressure_kpag: float | None = None,
    molar_flow_kmol_h: float | None = None,
    component_molar_fractions: Iterable[float] | None = None,
) -> None:
    if temperature_c is not None:
        stream.TemperatureValue = temperature_c
    if pressure_kpag is not None:
        stream.PressureValue = pressure_kpag
    if molar_flow_kmol_h is not None:
        stream.MolarFlowValue = molar_flow_kmol_h
    if component_molar_fractions is not None:
        stream.ComponentMolarFractionValue = list(component_molar_fractions)


def configure_environment_temp_dirs() -> None:
    temp_root = Path(r"C:\Temp")
    temp_root.mkdir(parents=True, exist_ok=True)
    os.environ["TEMP"] = str(temp_root)
    os.environ["TMP"] = str(temp_root)


def safe_float_attr(obj, attr: str) -> float | None:
    try:
        value = getattr(obj, attr)
    except Exception:
        return None
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return None

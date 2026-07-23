from __future__ import annotations

import argparse
import json
import math
import shutil
import sys
import time
import traceback
from pathlib import Path

import pythoncom
from win32com.client import Dispatch

from hysys_automation import HysysCaseSession, HysysLaunchOptions


PFD_OPERATION = -2
PFD_OPERATION_LABEL = -4
PFD_VISIBLE_AND_HIDDEN = 2
STREAM_TYPES = {"materialstream", "energystream"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rearrange an existing HYSYS PFD on a workcopy and verify that calculations did not change."
    )
    parser.add_argument("--case", required=True, type=Path, help="Validated source .hsc case.")
    parser.add_argument("--output-case", required=True, type=Path, help="Layout workcopy to create.")
    parser.add_argument("--layout", required=True, type=Path, help="PFD layout JSON.")
    parser.add_argument("--report", required=True, type=Path, help="Validation JSON output.")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing output workcopy.")
    parser.add_argument("--visible", action="store_true", help="Show HYSYS during execution.")
    parser.add_argument("--mass-tolerance-kg-h", type=float, default=0.01)
    parser.add_argument("--energy-tolerance-kw", type=float, default=0.01)
    parser.add_argument("--position-tolerance", type=float, default=1e-6)
    parser.add_argument(
        "--allow-label-overlap",
        action="store_true",
        help="Do not fail when the conservative label rectangle check finds overlaps.",
    )
    return parser.parse_args()


def load_layout(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data.get("targets"), dict) or not data["targets"]:
        raise ValueError("Layout JSON must contain a non-empty 'targets' object.")
    return data


def target_xy(value) -> tuple[float, float]:
    if isinstance(value, dict):
        return float(value["x"]), float(value["y"])
    if isinstance(value, (list, tuple)) and len(value) == 2:
        return float(value[0]), float(value[1])
    raise ValueError(f"Invalid target coordinate: {value!r}")


def pfd_items(pfd, item_type: int):
    prop = pfd._prop_map_get_.get("Items")
    dispid = prop[0] if prop else 1610809346
    result = pfd._oleobj_.InvokeTypes(
        dispid,
        0,
        pythoncom.DISPATCH_PROPERTYGET,
        (9, 0),
        ((12, 17), (12, 17)),
        item_type,
        PFD_VISIBLE_AND_HIDDEN,
    )
    return Dispatch(result)


def select_pfd(case, pfd_name: str | None):
    pfds = case.Flowsheet.PFDs
    if not pfd_name:
        return pfds.ActivePFD
    try:
        return pfds.Item(pfd_name)
    except Exception:
        pass
    try:
        count = int(pfds.Count)
    except Exception:
        count = 0
    for index in range(count):
        try:
            pfd = pfds.Item(index)
            if str(pfd.name) == pfd_name:
                return pfd
        except Exception:
            continue
    try:
        return pfds.ActivePFD
    except Exception:
        pass
    raise KeyError(f"PFD not found: {pfd_name}")


def bind_pfd(case, app, pfd_name: str | None) -> tuple[object, str]:
    attempts = (
        ("headless", False, False),
        ("case-visible", True, False),
        ("application-visible", True, True),
    )
    last_error: Exception | None = None
    for mode, case_visible, app_visible in attempts:
        try:
            if case_visible:
                case.Visible = True
            if app_visible:
                app.Visible = True
            if case_visible or app_visible:
                time.sleep(2.0)
            pfd = select_pfd(case, pfd_name)
            if int(pfd_items(pfd, PFD_OPERATION).Count) <= 0:
                raise RuntimeError("PFD proxy is bound but its operation canvas is empty.")
            return pfd, mode
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"Unable to bind native PFD after GUI initialization fallbacks: {last_error}")


def item_map(items) -> dict[str, object]:
    result: dict[str, object] = {}
    for index in range(int(items.Count)):
        item = items.Item(index)
        name = str(item.name)
        if name:
            result[name] = item
    return result


def safe_value(variable, units: str) -> float | None:
    try:
        value = float(variable.GetValue(units))
    except Exception:
        return None
    if not math.isfinite(value) or value == -32767:
        return None
    return value


def object_name(obj) -> str:
    for attribute in ("name", "TaggedName"):
        try:
            value = str(getattr(obj, attribute))
            if value:
                return value.replace(" @Main", "")
        except Exception:
            pass
    return ""


def calculation_fingerprint(case) -> dict:
    flowsheet = case.Flowsheet
    material = {}
    for index in range(int(flowsheet.MaterialStreams.Count)):
        stream = flowsheet.MaterialStreams.Item(index)
        material[object_name(stream)] = safe_value(stream.MassFlow, "kg/h")

    energy = {}
    for index in range(int(flowsheet.EnergyStreams.Count)):
        stream = flowsheet.EnergyStreams.Item(index)
        energy[object_name(stream)] = safe_value(stream.HeatFlow, "kW")

    operations = []
    recycle = {}
    for index in range(int(flowsheet.Operations.Count)):
        operation = flowsheet.Operations.Item(index)
        name = object_name(operation)
        type_name = str(operation.TypeName)
        operations.append({"name": name, "type": type_name})
        if type_name.lower() == "recycle":
            try:
                recycle[name] = int(operation.RecycleConvergence)
            except Exception:
                recycle[name] = None

    return {
        "solver_can_solve": bool(case.Solver.CanSolve),
        "solver_is_solving": bool(case.Solver.IsSolving),
        "material_stream_count": int(flowsheet.MaterialStreams.Count),
        "energy_stream_count": int(flowsheet.EnergyStreams.Count),
        "operation_count": int(flowsheet.Operations.Count),
        "material_mass_flow_kg_h": material,
        "energy_heat_flow_kw": energy,
        "operations": operations,
        "recycle_convergence": recycle,
    }


def layout_snapshot(operations, labels) -> list[dict]:
    rows = []
    for index in range(int(operations.Count)):
        item = operations.Item(index)
        label = labels.Item(index)
        rows.append(
            {
                "name": str(item.name),
                "object_type": str(item.Object.TypeName),
                "x": float(item.XPosition),
                "y": float(item.YPosition),
                "width": float(item.Width),
                "height": float(item.Height),
                "hidden": bool(item.Hidden),
                "label_x": float(label.XPosition),
                "label_y": float(label.YPosition),
                "label_width": float(label.Width),
                "label_hidden": bool(label.Hidden),
            }
        )
    return rows


def move_to(pfd, item, target: tuple[float, float]) -> None:
    dx = target[0] - float(item.XPosition)
    dy = target[1] - float(item.YPosition)
    if abs(dx) > 1e-9 or abs(dy) > 1e-9:
        pfd.MoveBy((item,), dx, dy)


def position_label(item, label, layout: dict) -> None:
    label.Hidden = False
    label.XPosition = item.XPosition + item.Width / 2.0 - label.Width / 2.0
    if str(item.IconName) == "ThreeDSeparator":
        label.XPosition = item.XPosition + item.Width + 12.0
        label.YPosition = item.YPosition + item.Height / 2.0
    elif str(item.name) in set(layout.get("label_below", [])):
        label.YPosition = item.YPosition + item.Height + 25.0
    else:
        label.YPosition = item.YPosition - 38.0
    label.XPosition += float(layout.get("label_x_shift", {}).get(str(item.name), 0.0))
    label.YPosition += float(layout.get("label_y_shift", {}).get(str(item.name), 0.0))


def label_overlaps(snapshot: list[dict], label_height: float) -> list[dict]:
    visible = [row for row in snapshot if not row["label_hidden"]]
    overlaps = []
    for left_index, left in enumerate(visible):
        for right in visible[left_index + 1 :]:
            left_x2 = left["label_x"] + left["label_width"]
            right_x2 = right["label_x"] + right["label_width"]
            left_y2 = left["label_y"] + label_height
            right_y2 = right["label_y"] + label_height
            intersects = (
                left["label_x"] < right_x2
                and left_x2 > right["label_x"]
                and left["label_y"] < right_y2
                and left_y2 > right["label_y"]
            )
            if intersects:
                overlaps.append({"left": left["name"], "right": right["name"]})
    return overlaps


def compare_scalar_maps(before: dict, after: dict, tolerance: float) -> dict:
    missing = sorted(set(before) ^ set(after))
    deltas = {}
    for name in sorted(set(before).intersection(after)):
        left = before[name]
        right = after[name]
        if left is None or right is None:
            if left != right:
                deltas[name] = None
            continue
        delta = float(right) - float(left)
        if abs(delta) > tolerance:
            deltas[name] = delta
    return {"missing_or_extra": missing, "out_of_tolerance": deltas}


def compare_fingerprints(before: dict, after: dict, mass_tolerance: float, energy_tolerance: float) -> dict:
    return {
        "counts_match": all(
            before[key] == after[key]
            for key in ("material_stream_count", "energy_stream_count", "operation_count")
        ),
        "operations_match": before["operations"] == after["operations"],
        "recycle_match": before["recycle_convergence"] == after["recycle_convergence"],
        "material": compare_scalar_maps(
            before["material_mass_flow_kg_h"], after["material_mass_flow_kg_h"], mass_tolerance
        ),
        "energy": compare_scalar_maps(
            before["energy_heat_flow_kw"], after["energy_heat_flow_kw"], energy_tolerance
        ),
    }


def comparison_passed(comparison: dict) -> bool:
    return (
        comparison["counts_match"]
        and comparison["operations_match"]
        and comparison["recycle_match"]
        and not comparison["material"]["missing_or_extra"]
        and not comparison["material"]["out_of_tolerance"]
        and not comparison["energy"]["missing_or_extra"]
        and not comparison["energy"]["out_of_tolerance"]
    )


def persist_staged_case(case, output_case: Path) -> None:
    case.Save()
    current = Path(str(case.FullName))
    if current.resolve() != output_case.resolve():
        shutil.copy2(current, output_case)


def main() -> int:
    args = parse_args()
    source = args.case.resolve()
    output_case = args.output_case.resolve()
    report_path = args.report.resolve()
    report = {"started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "errors": []}

    try:
        if source == output_case:
            raise ValueError("Source case and output workcopy must be different files.")
        if not source.is_file():
            raise FileNotFoundError(source)
        if output_case.exists() and not args.overwrite:
            raise FileExistsError(f"Output case exists; use --overwrite: {output_case}")
        layout = load_layout(args.layout.resolve())
        targets = {name: target_xy(value) for name, value in layout["targets"].items()}

        output_case.parent.mkdir(parents=True, exist_ok=True)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, output_case)

        options = HysysLaunchOptions(visible=args.visible)
        with HysysCaseSession(options) as session:
            case = session.open_case(output_case)
            before_calculation = calculation_fingerprint(case)
            pfd, initial_pfd_mode = bind_pfd(case, session.app, layout.get("pfd"))
            operations = pfd_items(pfd, PFD_OPERATION)
            labels = pfd_items(pfd, PFD_OPERATION_LABEL)
            if int(operations.Count) != int(labels.Count):
                raise RuntimeError("PFD operation and label collections are not index-aligned.")
            items = item_map(operations)

            missing = sorted(set(targets) - set(items))
            if missing:
                raise KeyError(f"Layout targets not found in PFD: {missing}")
            stream_targets = sorted(
                name for name in targets if str(items[name].Object.TypeName).lower() in STREAM_TYPES
            )
            if stream_targets:
                raise ValueError(f"Layout targets must be unit operations, not streams: {stream_targets}")
            unit_names = {
                name
                for name, item in items.items()
                if str(item.Object.TypeName).lower() not in STREAM_TYPES
            }
            unmapped_units = sorted(unit_names - set(targets))
            if unmapped_units:
                raise ValueError(f"Every non-stream PFD object needs a target: {unmapped_units}")

            before_layout = layout_snapshot(operations, labels)
            old_can_solve = bool(case.Solver.CanSolve)
            case.Solver.CanSolve = False
            try:
                def place(reverse: bool = False) -> None:
                    names = list(targets)
                    if reverse:
                        names.reverse()
                    for name in names:
                        move_to(pfd, items[name], targets[name])

                place()
                for index in range(int(operations.Count)):
                    item = operations.Item(index)
                    if str(item.Object.TypeName).lower() in STREAM_TYPES:
                        item.AutoPosition()
                place()

                for index in range(int(operations.Count)):
                    position_label(operations.Item(index), labels.Item(index), layout)

                place(reverse=True)
                for name in layout.get("final_priority", []):
                    if name not in targets:
                        raise KeyError(f"final_priority item has no target: {name}")
                    move_to(pfd, items[name], targets[name])
            finally:
                case.Solver.CanSolve = old_can_solve
            persist_staged_case(case, output_case)

            session.close_case()
            time.sleep(2.0)
            case = session.open_case(output_case)
            after_calculation = calculation_fingerprint(case)
            pfd, reopened_pfd_mode = bind_pfd(case, session.app, layout.get("pfd"))
            operations = pfd_items(pfd, PFD_OPERATION)
            labels = pfd_items(pfd, PFD_OPERATION_LABEL)
            after_layout = layout_snapshot(operations, labels)
            after_items = {row["name"]: row for row in after_layout}

            position_errors = {}
            for name, target in targets.items():
                row = after_items[name]
                dx = row["x"] - target[0]
                dy = row["y"] - target[1]
                if abs(dx) > args.position_tolerance or abs(dy) > args.position_tolerance:
                    position_errors[name] = {"dx": dx, "dy": dy}

            fingerprint_comparison = compare_fingerprints(
                before_calculation,
                after_calculation,
                args.mass_tolerance_kg_h,
                args.energy_tolerance_kw,
            )
            overlaps = label_overlaps(after_layout, float(layout.get("label_height", 18.0)))
            extent = pfd.Extent

            report.update(
                {
                    "hysys_version": session.version,
                    "source_case": str(source),
                    "output_case": str(output_case),
                    "pfd": str(pfd.name),
                    "pfd_initialization": {
                        "initial": initial_pfd_mode,
                        "reopened": reopened_pfd_mode,
                    },
                    "pfd_extent": list(extent) if extent is not None else None,
                    "before_layout": before_layout,
                    "after_layout": after_layout,
                    "position_errors": position_errors,
                    "label_overlaps": overlaps,
                    "before_calculation": before_calculation,
                    "after_calculation": after_calculation,
                    "fingerprint_comparison": fingerprint_comparison,
                }
            )
            report["passed"] = (
                not position_errors
                and comparison_passed(fingerprint_comparison)
                and (args.allow_label_overlap or not overlaps)
                and after_calculation["solver_can_solve"] == old_can_solve
                and not after_calculation["solver_is_solving"]
            )
    except Exception as exc:
        report["errors"].append(f"{type(exc).__name__}: {exc}")
        report["traceback"] = traceback.format_exc()
        report["passed"] = False

    report["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key not in {"before_layout", "after_layout"}}, ensure_ascii=False, indent=2))
    return 0 if report.get("passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())

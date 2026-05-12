# 2026-05-12 HYSYS runtime lessons

This note records execution lessons from a pure-hydrogen density table task. The task was intentionally simple: create a native Aspen HYSYS calculation for hydrogen density from 1 MPa to 90 MPa and export auditable tables.

## What failed first

1. The Python environment initially lacked `pywin32`, so `pythoncom` and `win32com.client` could not be imported.
2. `DispatchEx("HYSYS.Application")` was not reliable by itself. The COM registry existed, but the direct COM server launch could fail with a server execution error.
3. The HYSYS executable could still be launched directly through the registered automation server command, and the Python process could then attach to the active `HYSYS.Application` object.
4. A Peng-Robinson reference calculation is useful for checking magnitude, but it must not be delivered as "HYSYS-native" unless the value was read back from HYSYS.
5. Pressure basis matters. A management-facing table may need `MPa(g)`, while HYSYS still receives absolute pressure. The run log must record the conversion.

## Repository changes implied by the lesson

1. Provide a real `hysys_readiness_check.py` script, separate from repository hygiene checks.
2. Make the direct COM wrapper fall back to `LocalServer32` plus active-object attach before reporting launch failure.
3. Provide a minimal property-table smoke script that creates a pure-H2 HYSYS case, writes pressure and temperature, waits for the solver, and reads `MassDensity.GetValue('kg/m3')`.
4. Require exported property tables to record HYSYS version, property package, component list, pressure basis, pressure conversion, property path, source case path, CSV/JSON, and run log.

## Boundary statement

Native HYSYS results mean the value was read from a HYSYS object after a HYSYS solve. External EOS calculations, fitted curves, CoolProp checks, or hand-coded Peng-Robinson calculations may be useful audit references, but they must be labeled as references and not as native HYSYS outputs.

# Heartbeat scan 2026-05-30

Automation ID: `ai-hysys-daily-scan`

Worktree used: `D:\SKILL\AI-HYSYS-Skill-heartbeat-main`

## Search focus

Searched for latest credible sources around Aspen HYSYS automation, COM/Python/spreadsheet/workbook control, LLM agents for process simulation, HYSYS digital twins, hybrid AI, and third-party Python wrappers.

## New valuable source update

### `aspen-pysys` PyPI/piwheels alpha update

- Source: https://pypi.org/project/aspen-pysys/
- PyPI JSON snapshot: [../community/aspen-pysys-pypi-json-2026-05-30.json](../community/aspen-pysys-pypi-json-2026-05-30.json)
- piwheels JSON snapshot: [../community/aspen-pysys-piwheels-json-2026-05-30.json](../community/aspen-pysys-piwheels-json-2026-05-30.json)
- Current version observed: `0.1.0a2`
- Upload time observed in PyPI metadata: `2026-05-26T06:33:20`
- Requires Python: `>=3.12.12`
- Runtime dependency observed in PyPI metadata: `pywin32>=311`
- License check: Codeberg repository branch `v0.1.0-alpha` still contains GPL-3.0 license text and `pyproject.toml` declares `GPL-3.0-or-later`
- Quality: B-
- Category: community wrapper candidate

## Value judgment

This update is worth tracking because `aspen-pysys` is a direct HYSYS Python API wrapper candidate and has advanced from the previously indexed `0.1.0a0` alpha to `0.1.0a2`.

It does not materially change the project default. The package is still alpha, GPL-licensed, Windows/pywin32/HYSYS-runtime dependent, and not smoke-tested in this local HYSYS runtime. AI-HYSYS-Skill should keep direct COM and spreadsheet/workbook bridge as the default lanes, while learning wrapper design ideas without vendoring or installing this package by default.

## Lower-value findings

- Previously indexed CHERD 2026 ML flash surrogate, Sketch2Simulation, MDPI HYSYS/Python/ScadaBR, and AspenTech official digital-twin sources were not duplicated.
- Secondary news about Emerson/AspenTech Industrial AI did not add stronger evidence than already indexed official Emerson/AspenTech sources.
- No new license-clear, runtime-verified public HYSYS case or wrapper was found that should replace the existing control-lane rules.

## Project updates made

- Added current PyPI/piwheels metadata snapshots under `CASE/community`.
- Updated `CASE/source-index.md`.
- Updated `CASE/notes/hysys-source-digest.md`.
- Updated `README.md` candidate wrapper version note.

## Safety notes

- No package artifact, wheel, sdist, executable, installer, HYSYS case, or proprietary plant file was added.
- No runtime claim was added for `aspen-pysys`.
- No default dependency was changed.

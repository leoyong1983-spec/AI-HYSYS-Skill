# Heartbeat Scan 2026-06-27

## Search Scope

The scan checked current web and GitHub results for:

- AI controlling Aspen HYSYS
- HYSYS automation through COM, Python, spreadsheets, and workbooks
- MCP or LLM agents for process simulation
- Aspen HYSYS digital twins, Aspen OnLine, and hybrid AI workflows

## Adopted Source

### GaboTalero/HYSYS-Python-Case-Builder

- Source: https://github.com/GaboTalero/HYSYS-Python-Case-Builder
- Local snapshots:
  - `CASE/community/hysys-python-case-builder-gabotalero-readme-2026-06-27.md`
  - `CASE/community/hysys-python-case-builder-gabotalero-metadata-2026-06-27.json`
  - `CASE/community/hysys-python-case-builder-gabotalero-tree-2026-06-27.json`
  - `CASE/community/hysys-python-case-builder-gabotalero-license-2026-06-27.txt`
  - `CASE/community/hysys-python-case-builder-gabotalero-hysys-python-creator-2026-06-27.py`
  - `CASE/community/hysys-python-case-builder-gabotalero-spreadsheet-helper-2026-06-27.py`
- License: MIT, according to GitHub metadata and repository license file.
- Grade: C+/B- community automation reference.

This repository is worth tracking because it is a small public MIT example of Aspen HYSYS automation through `win32com`, including session startup, case open/create behavior, fluid-package/component setup, and a spreadsheet helper pattern. It also explicitly uses Windows, Aspen HYSYS, and `pywin32`, which matches the project platform assumptions.

It is not promoted to a default control lane because it is a small community repository, contains no packaged benchmark `.hsc/.hscz` case payload, includes from-scratch case creation examples, and has not been locally validated against this machine's HYSYS runtime. It should be used only as an implementation reference for COM patterns and path hygiene, not as proof that AI-HYSYS-Skill can reliably generate production HYSYS models from scratch.

## Rejected Or Not Promoted

- `ernst70/multicomponent-distillation-design-MATLAB-HYSYS`: rejected for this heartbeat because the repository currently exposes only a single MATLAB shortcut calculation file, has no README, no detected license, and no visible HYSYS COM/API call in the inspected file. It may describe a HYSYS validation context in metadata, but the available payload is not strong enough for CASE ingestion.
- `Sketch2Simulation`, `Text-to-Flowsheet`, `LLM agent process simulation`, `LLM in PSE survey`, Aspen Hybrid Models, Aspen HYSYS Digital Twins course, PySIS, `aspen-pysys`, and `yuuyo-arobet/AspenHYSYS-MCP-Server`: already indexed, not duplicated.
- YouTube, LinkedIn, Medium, Scribd, ResearchGate-only, and generic MCP search results: not adopted because they are weaker than already indexed official, research, or direct-code evidence.

## Project Impact

- Updated `CASE/source-index.md` with a normalized community-candidate entry.
- No README, SKILL, or reference rule change was made because the evidence does not change the project boundary.
- The default boundary remains existing runnable HYSYS case takeover, bounded parameter changes, validation, rollback, and reporting.

## Boundary Notes

This source does not justify any claim that:

- AI-HYSYS-Skill can reliably create production HYSYS models from scratch.
- The repository has been validated on a local Aspen HYSYS runtime.
- Community COM scripts should replace the built-in direct COM starter or spreadsheet/workbook bridge.
- Generated `.hsc` files from community examples are benchmark-quality cases.

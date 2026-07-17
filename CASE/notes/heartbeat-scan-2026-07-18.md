# Heartbeat Scan 2026-07-18

## Search Scope

Searched for recent credible sources about AI controlling Aspen HYSYS, HYSYS COM/Python/spreadsheet/workbook automation, MCP servers, LLM process-simulation agents, digital twins, hybrid AI, and public HYSYS wrappers. Findings were compared with `CASE/source-index.md` through the 2026-07-17 entry.

## Valuable Finding

`aspen-pysys` advanced from the indexed PyPI version `0.1.0a3` to `0.1.0a5` on 2026-07-17.

Saved evidence:

- `CASE/community/aspen-pysys-pypi-release-2026-07-18.json`

Value grade: B-

Reason:

- It is a public, HYSYS-specific Python/COM wrapper with typed object abstractions.
- Archive inspection found a useful a4 safety pattern for distillation-column feed placement: distinguish feeds attached in the main flowsheet from feeds represented inside the column subflowsheet, compare both name sets, and reject a tray-location operation if they do not match.
- The a5 release corrects the documentation homepage but does not add further runtime behavior beyond a4.

Limitations:

- The package remains alpha and GPL-3.0-or-later.
- It requires Python `>=3.12.12` and `pywin32>=311`.
- It was not installed, executed, or smoke-tested against a local HYSYS runtime in this heartbeat.
- No release changelog or evidence of production qualification was found.
- Its package archives include an example `.hsc`; that proprietary-format case was inspected only as an archive entry and was not copied into this repository.

## Project Impact

Adopted:

- Updated the wrapper evidence snapshot and source index from `0.1.0a3` to `0.1.0a5`.
- Added a column-feed identity guard to `SKILL.md`: before changing a feed tray or location, resolve the main-flowsheet attachment and column-subflowsheet representation, compare normalized names, and abort on missing, duplicate, or mismatched identities.

Not adopted:

- The wrapper was not added as a dependency and none of its GPL source code was copied.
- No cache, singleton, concurrency, or COM-performance claim was adopted because this release diff did not provide evidence for those claims.
- No HYSYS runtime validation claim was added.

## Boundary Judgment

This update improves object-identity preflight for an existing HYSYS distillation case. It does not support reliable greenfield case generation, production writeback, or replacement of the repository's direct COM and workbook lanes.

## Rejected Or Deferred Items

- The newly surfaced machine-learning-aided flash paper was already covered by the 2026-07-16 source review and was not duplicated.
- `AspenHYSYS-MCP-Server`, `simulator_codingplatform_integration`, and `HDA-Surrogate-Optimization` show no newer pushed code that changes their existing assessment.
- Repeated PINN, Sketch2Simulation, digital-twin, EHY2311, and generic AI-control results were already indexed.

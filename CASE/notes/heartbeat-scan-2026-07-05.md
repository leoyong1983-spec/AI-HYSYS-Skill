# 2026-07-05 Heartbeat Scan

## Scope

Searched for recent or newly discovered credible public evidence about AI/HYSYS automation, Python/COM control, MCP orchestration, spreadsheet/workbook bridges, and HYSYS digital twin or hybrid AI workflows.

## Valuable findings

### `Anikesh31/simulator_codingplatform_integration`

- URL: https://github.com/Anikesh31/simulator_codingplatform_integration
- Local snapshots:
  - `../community/simulator-codingplatform-integration-readme-2026-07-05.md`
  - `../community/simulator-codingplatform-integration-metadata-2026-07-05.json`
  - `../community/simulator-codingplatform-integration-tree-2026-07-05.json`
- Value grade: B+ direct HYSYS automation evidence.
- Reason: The repository is a public companion-style tutorial for connecting Aspen HYSYS with Python and MATLAB, retrieving streams/unit operations/properties, retrieving backdoor variables, inspecting methods and ordered arguments, modifying objects, and building examples such as TEA. It directly complements the already indexed 2025 Computers & Chemical Engineering paper DOI `10.1016/j.compchemeng.2025.109247`.
- Limits: GitHub API did not identify a license, public adoption signal is modest, and no local HYSYS runtime test was performed in this workspace.
- Project impact: Strengthens the skill rule that HYSYS object inspection, backdoor variables, and method-signature discovery are legitimate support tasks, but still require existing cases, explicit variable maps, unit checks, and workcopy-only writes.

### `DanielVazVaz/PySIS`

- URL: https://github.com/DanielVazVaz/PySIS
- Local snapshots:
  - `../community/pysis-readme-2026-07-05.md`
  - `../community/pysis-metadata-2026-07-05.json`
  - `../community/pysis-tree-2026-07-05.json`
- Value grade: B community wrapper evidence.
- Reason: PySIS is a public abstraction layer over the Aspen HYSYS COM interface and its README claims checks against HYSYS V11, V12, and V14. It has stronger public adoption signal than very new alpha wrappers.
- Limits: GitHub API did not identify a license, no local smoke test was performed, and wrapper behavior should not replace direct COM or spreadsheet/workbook lanes without project approval.
- Project impact: Add PySIS to the third-party wrapper watchlist. It can inform object abstraction and API ergonomics, but should not become a default dependency.

## Duplicate or unchanged findings

- `aspen-pysys` remains at PyPI `0.1.0a3`; no `0.1.0a4` release was found.
- `yuuyo-arobet/AspenHYSYS-MCP-Server` metadata remains unchanged from the 2026-07-04 snapshot.
- `OptiMaL-PSE-Lab/Sketch2Simulation` had repository metadata updates but no new pushed code after the existing March 2026 source snapshot.
- AspenTech Hybrid Models, EHM105, HYSYS interconnection methodology, and spreadsheet bridge examples were repeats of already indexed evidence.

## Skill boundary update

Third-party HYSYS wrappers and tutorial repositories are now tracked as candidate evidence, not adopted dependencies. Before using any of them in a project, require:

1. explicit license compatibility,
2. Python and `pywin32` compatibility,
3. an existing runnable HYSYS case,
4. local smoke-test evidence,
5. workcopy-only write discipline,
6. unit/schema logging,
7. human acceptance before engineering use.


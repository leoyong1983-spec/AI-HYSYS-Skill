# 2026-07-06 Heartbeat Scan

## Scope

Searched for recent credible evidence about AI controlling Aspen HYSYS, HYSYS automation through COM/Python/spreadsheets/workbooks, MCP-based simulator agents, HYSYS wrapper libraries, and HYSYS digital twin or hybrid AI workflows.

## Valuable finding

### `bsha0/ap-python`

- URL: https://github.com/bsha0/ap-python
- Local snapshots:
  - `../community/ap-python-readme-2026-07-06.md`
  - `../community/ap-python-metadata-2026-07-06.json`
  - `../community/ap-python-tree-2026-07-06.json`
  - `../community/ap-python-license-2026-07-06.txt`
- Value grade: B direct community wrapper evidence.
- Reason: The repository is a public MIT-licensed Python automation package for Aspen Plus and Aspen HYSYS. Its README includes a HYSYS example using `ap_python.aspenhysys`, HYSYS variable monikers copied through Excel links, `find_node`, `get_units`, `get_value`, `set_value`, `save`, and `saveas`.
- Limits: The repository is old, has low public adoption signal, and has not been smoke-tested against the local HYSYS runtime in this workspace.
- Project impact: Add it to the wrapper watchlist and use it as evidence that HYSYS moniker-based access and unit-aware get/set wrappers are public patterns. Do not adopt it as a default dependency.

## Not adopted

### LNG cold energy recovery GA paper

- URL: https://doi.org/10.48130/een-0026-0007
- Title: "Enhancements and optimization of LNG cold energy recovery via advanced binary working fluid power cycle systems"
- Decision: Not added to CASE as HYSYS evidence.
- Reason: The article is credible process-simulation and genetic-algorithm optimization evidence for LNG cold energy recovery, but the source page and PDF did not contain explicit `Aspen` or `HYSYS` evidence. It is too adjacent for this repository's HYSYS-specific source pack.
- Boundary note: It may be useful for a future LNG cold-energy research review, but not for AI-HYSYS-Skill's HYSYS control-lane claims.

## Duplicate or unchanged findings

- `aspen-pysys` remains at PyPI `0.1.0a3`; no `0.1.0a4` release was found.
- `yuuyo-arobet/AspenHYSYS-MCP-Server` remains the current B+ direct HYSYS MCP community candidate already indexed on 2026-07-04.
- `Anikesh31/simulator_codingplatform_integration` and `DanielVazVaz/PySIS` remain the direct wrapper/tutorial evidence indexed on 2026-07-05.
- AspenTech Hybrid Models, HYSYS interconnection methodology, Sketch2Simulation, and spreadsheet bridge examples were repeated search results already covered by the source pack.

## Project rule update

Third-party wrappers now tracked by name include `aspen-pysys`, `PySIS`, `ap-python`, and `simulator_codingplatform_integration`. All remain optional evidence only until license, runtime, `pywin32`, local HYSYS smoke test, workcopy-only writes, unit logging, and human acceptance are checked.


# 2026-07-04 Heartbeat Scan

## Scope

Searched for recent credible evidence about AI controlling Aspen HYSYS, HYSYS COM/Python automation, MCP-based simulator agents, workbook/spreadsheet bridges, and HYSYS digital twin or hybrid AI workflows.

## High-value finding

### `yuuyo-arobet/AspenHYSYS-MCP-Server`

- URL: https://github.com/yuuyo-arobet/AspenHYSYS-MCP-Server
- Local snapshots:
  - `../community/aspen-hysys-mcp-server-readme-2026-07-04.md`
  - `../community/aspen-hysys-mcp-server-metadata-2026-07-04.json`
  - `../community/aspen-hysys-mcp-server-tree-2026-07-04.json`
  - `../community/aspen-hysys-mcp-server-architecture-2026-07-04.md`
  - `../community/aspen-hysys-mcp-server-license-2026-07-04.txt`
- Value grade: B+ direct community evidence.
- Reason: The project directly targets Aspen HYSYS via MCP and pywin32/COM, documents 51 tools, uses a read/session/write mode gate, defaults away from model-writing operations, and claims HYSYS V14 real-machine verification. It is more directly relevant than AVEVA APS MCP examples because it is HYSYS-specific.
- Limits: It is a third-party community repository with one maintainer, low public adoption signal, and no local HYSYS runtime verification in this workspace. Its real-machine verification claims are source claims, not AI-HYSYS-Skill validation results.
- Project impact: Use it as a design reference for MCP orchestration, explicit tool modes, read-only-first operation, dry-run/write separation, workcopy discipline, and audit logging. Do not adopt it as a default dependency or treat it as an AspenTech-supported HYSYS API.

## Lower-value or duplicate findings

- `aspen-pysys` remains at PyPI `0.1.0a3`; no new version was found. It remains a B- wrapper candidate because it is alpha, GPL-3.0-or-later, requires Python `>=3.12.12` and `pywin32>=311`, and has not been smoke-tested against the local HYSYS runtime.
- `gsi-lab/APS-Agent` metadata still shows a June 2026 APS MCP implementation. It remains useful as adjacent architecture evidence, but it is not a HYSYS API.
- The published ScienceDirect page for the APS LLM-agent paper is useful bibliographic confirmation, but the arXiv/PDF and GitHub snapshots already cover the architecture lessons needed by this project.
- Search results also repeated Sketch2Simulation, Aspen Hybrid Models, AspenTech EHM105, HYSYS interconnection methodologies, and generic AI automation material already covered in the source pack.

## Skill boundary update

AI-HYSYS-Skill now recognizes HYSYS-specific MCP servers as community candidate orchestration layers. The operating rule remains conservative:

1. Existing runnable HYSYS cases remain the default starting point.
2. MCP is a protocol wrapper above COM/spreadsheet/workbook lanes, not simulator authority by itself.
3. Read-only or session-only modes are preferred for discovery and reporting.
4. Write-capable tools require explicit operation lists, units, schemas, single-workcopy locks, dry-run behavior, audit logs, rollback expectations, and human acceptance.
5. No third-party MCP server is a default dependency unless license, runtime, and local smoke-test checks pass.

## Repository-facing changes

- Added source snapshots under `CASE/community/`.
- Updated `CASE/source-index.md`.
- Updated `CASE/notes/hysys-source-digest.md`.
- Updated `README.md`.
- Updated `SKILL.md`.


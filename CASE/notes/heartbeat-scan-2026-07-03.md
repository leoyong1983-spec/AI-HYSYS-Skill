# Heartbeat Scan 2026-07-03

Time basis: 2026-07-03 03:00 Asia/Shanghai.

## Search Scope

Searched for current public sources on:

- AI controlling Aspen HYSYS
- HYSYS COM / Python / pywin32 / spreadsheet automation
- HYSYS and Model Context Protocol workflows
- LLM agents for process simulation
- HYSYS digital twin and hybrid AI workflows

## Value Judgment

No source found today changes the project boundary. AI-HYSYS-Skill should still focus on existing runnable HYSYS cases for bounded takeover, validation, and reporting.

Valuable additions:

1. `aspen-pysys` PyPI metadata, version `0.1.0a3`
   - Source: https://pypi.org/project/aspen-pysys/
   - Local snapshot: [../community/aspen-pysys-pypi-json-2026-07-03.json](../community/aspen-pysys-pypi-json-2026-07-03.json)
   - Value: B- community wrapper candidate. It is directly aimed at HYSYS Python access, but remains alpha, GPL-3.0-or-later, Python `>=3.12.12`, `pywin32>=311`, and not locally smoke-tested.
   - Action: Track only. Do not install, vendor, or make it the default control lane.

2. `gsi-lab/APS-Agent`
   - Source: https://github.com/gsi-lab/APS-Agent
   - Local snapshots:
     - [../community/aps-agent-gsi-lab-metadata-2026-07-03.json](../community/aps-agent-gsi-lab-metadata-2026-07-03.json)
     - [../community/aps-agent-gsi-lab-readme-2026-07-03.md](../community/aps-agent-gsi-lab-readme-2026-07-03.md)
     - [../community/aps-agent-gsi-lab-tree-2026-07-03.json](../community/aps-agent-gsi-lab-tree-2026-07-03.json)
     - [../community/aps-agent-gsi-lab-license-2026-07-03.txt](../community/aps-agent-gsi-lab-license-2026-07-03.txt)
   - Value: B adjacent MCP implementation evidence for process simulation agents. It targets AVEVA Process Simulation, not HYSYS, so it is architecture precedent only.
   - Action: Use to reinforce MCP boundary rules: lifecycle tools, read-only-first, explicit schemas, single workcopy lock, logs, rollback, and human acceptance.

3. RSC / Zenodo Text-to-flowsheet artifact
   - Article: https://pubs.rsc.org/en/content/articlelanding/2026/dd/d6dd00060f
   - Metadata snapshot: [../research/text-to-flowsheet-zenodo-19910216-2026-07-03.json](../research/text-to-flowsheet-zenodo-19910216-2026-07-03.json)
   - Value: B adjacent paper/code artifact for text-to-flowsheet and Graph-IR style workflows. It does not prove HYSYS greenfield generation is reliable.
   - Action: Keep as research evidence for auditable intermediate representations and bounded optimizer repair only.

Rejected or not adopted:

- Medium, YouTube, Scribd, Reddit, LinkedIn, and generic MCP posts remain C-level background unless corroborated by code, official documentation, or peer-reviewed sources.
- Unlicensed or heavy GitHub repositories are not downloaded as benchmark cases.
- No third-party wrapper is promoted to default dependency.

## Project Update

Updated project-facing docs to make the new evidence operational:

- `SKILL.md`: added wrapper and MCP boundary rules.
- `README.md`: added public reference links.
- `CASE/source-index.md`: indexed the new snapshots and this note.

## Boundary

Do not claim from-scratch HYSYS model generation is reliable. Do not claim production writeback or autonomous plant control. All AI, MCP, wrapper, surrogate, and text-to-flowsheet paths remain advisory until a HYSYS workcopy readback, solver status, KPI export, failed-sample log, rollback path, and human acceptance record exist.

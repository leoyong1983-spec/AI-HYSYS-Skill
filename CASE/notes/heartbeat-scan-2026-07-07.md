# Heartbeat scan 2026-07-07

## Scope

Searched for recent credible sources about AI controlling Aspen HYSYS, HYSYS automation through COM/Python/Excel/workbooks, LLM agents for process simulation, MCP-style simulator control, and HYSYS digital-twin or hybrid-AI workflows.

## Adopted sources

### 1. Automation in the simulation of processes with Aspen HYSYS: An academic approach

- Source: https://doi.org/10.1002/cae.22589
- Local snapshot: `CASE/research/hysys-automation-aspen-excel-vba-cae-2023-crossref.json`
- Value grade: B+ direct HYSYS automation evidence.
- Reason: Crossref metadata confirms a Wiley article specifically about automation in Aspen HYSYS simulation. The title and metadata support the project's existing control-lane stance that Aspen HYSYS automation can be taught and organized around external code and spreadsheet-style workflows.
- Boundary: This is evidence for automation methodology, not a claim that AI can create reliable HYSYS production models from zero. It does not replace local HYSYS runtime smoke testing.
- Project action: Updated `CASE/source-index.md`, `CASE/notes/hysys-source-digest.md`, and `references/control-lane-decision-matrix.md`.

### 2. Large language model agent for user-friendly chemical process simulations

- Source: https://doi.org/10.1016/j.dche.2026.100312
- Local snapshot: `CASE/research/llm-agent-process-simulation-crossref-2026-07-07.json`
- Value grade: B adjacent agent/MCP evidence.
- Reason: Crossref metadata confirms the published Digital Chemical Engineering version of the LLM-agent process-simulation paper. It strengthens the already-indexed arXiv/APS-Agent evidence that process simulators can be wrapped behind tool and MCP-style interfaces.
- Boundary: The published paper is adjacent process-simulation evidence and does not prove HYSYS-specific greenfield model generation or default write-capable control.
- Project action: Updated `CASE/source-index.md` and `CASE/notes/hysys-source-digest.md`.

## Deferred or rejected findings

- AspenTech EHY2311 course page: search results suggest an official "Developing Automation Solutions for Aspen HYSYS" course, but local `curl.exe` and PowerShell fetches to `esupport.aspentech.com` timed out. Deferred until a reliable snapshot can be saved.
- AspenTech Hybrid Models certification page: relevant to official HYSYS/hybrid-model training, but existing CASE evidence already covers EHM105, Hybrid Models FAQ, AI Model Builder, and Aspen OnLine boundaries. No new project rule was needed today.
- LinkedIn "AI Agent for Aspen HYSYS Simulation" style posts: not adopted because they are secondary promotional material and may imply from-scratch HYSYS model construction without enough reproducible evidence.
- Generic "MCP design strategies" posts: not adopted because they do not add HYSYS-specific evidence beyond existing MCP and APS-Agent records.

## Resulting project rule

The new CAE metadata strengthens this rule: for HYSYS automation work, treat Excel/VBA/spreadsheet bridges as legitimate engineered IO lanes when a case exposes stable variables through them, but keep direct COM or a proven project runner as the authoritative case lifecycle lane. AI should still operate on workcopies with explicit solver policy, schema, logs, and human acceptance.

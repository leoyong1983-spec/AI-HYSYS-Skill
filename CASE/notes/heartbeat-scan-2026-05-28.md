# Heartbeat scan 2026-05-28

Automation ID: `ai-hysys-daily-scan`

Worktree used: `D:\SKILL\AI-HYSYS-Skill-heartbeat-main`

## Search focus

Searched for latest credible sources around Aspen HYSYS automation, COM/Python/spreadsheet/workbook control, LLM agents for process simulation, HYSYS digital twins, hybrid AI, ML surrogate workflows, and process-simulation acceleration.

## New valuable source

### CHERD 2026 ML-aided flash surrogate validated against Aspen HYSYS

- Source: https://doi.org/10.1016/j.cherd.2026.05.041
- Publisher page: https://www.sciencedirect.com/science/article/pii/S0263876226003400
- Local metadata snapshot: [../research/hysys-ml-flash-cherd-2026-metadata.md](../research/hysys-ml-flash-cherd-2026-metadata.md)
- Local Crossref metadata: [../research/hysys-ml-flash-cherd-2026-crossref.json](../research/hysys-ml-flash-cherd-2026-crossref.json)
- Quality: B+
- Category: HYSYS reference simulator / Python ML thermodynamic surrogate evidence

## Value judgment

This source is worth adding because it is a recent peer-reviewed HYSYS-adjacent process-simulation acceleration paper. It uses Aspen HYSYS as the reference simulator and Python-side ML flash surrogates as an acceleration layer for large-batch thermodynamic and flowsheet calculations.

It materially improves the project boundary for surrogate tasks: AI-HYSYS-Skill may prepare HYSYS-derived training data schemas, candidate batch runs, error tables, extrapolation limits, and HYSYS rerun checklists, but must not let an ML flash surrogate replace final HYSYS runtime validation or human engineering review.

## Lower-value findings

- Previously indexed arXiv and official AspenTech digital-twin results were not duplicated.
- Generic AI/process-industry posts were not added because they did not improve HYSYS automation, validation, or boundary rules.
- No new license-clear, runtime-verified GitHub HYSYS wrapper or public HYSYS case was found that should replace the repository's direct COM and spreadsheet/workbook lanes.

## Project updates made

- Added CHERD / Crossref metadata under `CASE/research`.
- Updated `CASE/source-index.md`.
- Updated `CASE/notes/hysys-source-digest.md`.
- Updated `README.md`, `SKILL.md`, `references/digital-twin-boundary.md`, and `references/literature-patterns.md` with a flash-surrogate boundary rule.

## Safety notes

- No proprietary case files were added.
- No `.hsc`, `.hscz`, installer, executable, wheel, source distribution, or raw plant data file was added.
- The ScienceDirect full article text was not stored; only a local metadata/value snapshot and Crossref metadata were added.

# Heartbeat Scan 2026-07-17

## Search Scope

Searched for recent credible sources about AI controlling Aspen HYSYS, HYSYS COM/Python/spreadsheet/workbook automation, MCP servers, LLM process-simulation agents, digital twins, hybrid AI, LNG optimization, and surrogate workflows. Findings were compared with `CASE/source-index.md` through the 2026-07-16 entry.

## Valuable Finding And Re-evaluation

The open-access paper "Enhancements and optimization of LNG cold energy recovery via advanced binary working fluid power cycle systems" was re-evaluated.

The 2026-07-06 heartbeat did not adopt it because the source available at that time did not expose explicit Aspen HYSYS evidence. The current publisher HTML now contains the full methods text and explicitly states that the genetic algorithm was implemented in Python with an automated Aspen HYSYS interface. This new verifiable evidence supersedes the earlier rejection.

Saved evidence:

- `CASE/research/hysys-lng-cold-energy-ga-2026-07-17.html`

Value grade: B+

Reason:

- Peer-reviewed, open-access, direct HYSYS/Python optimization evidence.
- Defines the objective as maximizing integrated-cycle net power.
- Publishes decision-variable ranges for pressures, temperatures, mixture fractions, and separator ratio.
- Publishes GA settings: 50/100 generations, 100/200 population, and 0.2 mutation probability.
- States that optimization results were exported to Excel for analysis.
- Uses a bounded LNG regasification case with Peng-Robinson and explicit process assumptions.

Limitations:

- No reusable HYSYS case, Python code, or public dataset was identified.
- Data are available only from the corresponding author on reasonable request.
- A fixed generation count alone does not establish global convergence or production readiness.
- The study is an offline design optimization, not autonomous plant control.

## Project Impact

Adopted:

- Added the publisher HTML snapshot and source-index entry.
- Added the re-evaluation to the source digest.
- Updated `references/heat-exchanger-ai-patterns.md` to require optimizer configuration and stopping criteria in the audit package.

Not changed:

- `SKILL.md` already requires an approved HYSYS workcopy, bounded variables, logged objectives/iterations, HYSYS readback, and human acceptance.
- No third-party optimizer or HYSYS wrapper was added.

## Boundary Judgment

This paper supports the pattern `existing HYSYS case -> bounded Python optimizer -> HYSYS evaluations -> Excel/KPI analysis`. It does not support reliable greenfield HYSYS generation, replacement of the HYSYS baseline, or production writeback.

For similar work, record the case and property-package basis, objective, variables and units, bounds, constraints, population, generations, mutation/crossover settings, stopping rule, random seed when available, failed samples, HYSYS solver status, final readback, and human acceptance.

## Rejected Or Deferred Items

- A University of South-Eastern Norway thesis contained useful Python/HYSYS sensitivity and retry patterns, but its repository has migrated and the original PDF currently redirects to a retirement page; no valid snapshot was saved.
- `aspen-pysys` remains at PyPI `0.1.0a3`.
- Tracked HYSYS MCP and wrapper repositories have no newer code push that changes their assessment.
- Repeated PINN, ML-flash, OTS, EHY2311, Sketch2Simulation, and product-page results were not duplicated.

# Heat Exchanger AI Patterns for HYSYS

## Purpose

Read this note when a task mentions heat exchangers, Aspen EDR, heat exchanger networks, HEN, pinch analysis, `Delta Tmin`, heat duty prediction, cryogenic heat exchangers, cold boxes, LNG exchangers, or AI-assisted exchanger optimization.

The project position is narrow: AI-HYSYS-Skill supports advisory optimization and validation on existing runnable HYSYS or HYSYS/EDR cases. It does not treat a paper, surrogate model, or GitHub demo as permission for autonomous production control or greenfield HYSYS model generation.

## Evidence Pattern

The useful pattern across the current source set is:

1. Start from an existing HYSYS, HYSYS/EDR, or workbook-backed exchanger model.
2. Freeze property method, topology, exchanger names, stream names, units, and solver policy.
3. Expose a controlled variable schema through COM, spreadsheet/workbook tags, or a proven project runner.
4. Generate a design-of-experiments or bounded scenario matrix.
5. Use AI, ML, grey-box models, genetic algorithms, Bayesian optimization, PSO, or another optimizer only to propose candidate conditions.
6. Recalculate accepted candidates in a HYSYS workcopy or HYSYS/EDR model.
7. Export machine-readable KPIs, failed samples, unit checks, constraint violations, and a human acceptance note.

## Source Classification

Use these sources as precedent, not as direct runtime authority:

- Official AspenTech HYSYS and Aspen EDR material is authority for product capability, heat exchanger design/rating integration, and digital-twin positioning.
- `Galigeigei-Z/HDA-Surrogate-Optimization` is a community/research program precedent for Python-assisted HYSYS heat exchanger network supertargeting and `Delta Tmin` screening.
- The shell-and-tube exchanger grey-box / GA paper is research precedent for using Aspen EDR / HYSYS-style exchanger simulations to train an optimizer, then validating recommendations.
- The HYSYS + XGBoost + PSO pressure-swing distillation paper is adjacent evidence for the broader pattern: HYSYS baseline, ML surrogate, optimizer candidate, HYSYS/human review.
- LNG cryogenic heat-exchanger digital-twin papers are evidence for monitoring and early-warning workflows, not proof of autonomous closed-loop HYSYS control.
- The 2026 LNG cold-energy GA paper (DOI `10.48130/een-0026-0007`) is direct precedent for a bounded Python optimizer calling Aspen HYSYS, publishing variable ranges and GA settings, and exporting results to Excel. It is offline design-optimization evidence, not production-control authority.

## Required Task Setup

Before running or designing a heat-exchanger AI workflow, capture:

1. Source case or workbook path.
2. Exchanger object names and stream name map.
3. Hot/cold stream classification.
4. Property package and unit set.
5. Heat-duty, outlet-temperature, approach-temperature, pressure-drop, utility, and constraint KPIs.
6. Manipulated variables and bounds.
7. Rollback values for every write.
8. Solver pause/resume policy and convergence wait rule.
9. Design-space limits and extrapolation warning.
10. Human review owner and acceptance criterion.
11. Optimizer configuration and stopping criteria, including objective, constraints, population, generations or iterations, mutation/crossover settings, random seed when available, and the reason a run is accepted as complete.

## KPI Schema

Prefer a small machine-readable schema:

| Field | Meaning |
|---|---|
| `case_id` | Workcopy or baseline identifier |
| `exchanger_id` | HYSYS/EDR exchanger object or workbook tag |
| `hot_streams` | Hot-side stream identifiers |
| `cold_streams` | Cold-side stream identifiers |
| `manipulated_variables` | Variables allowed for advisory tuning |
| `bounds` | Lower/upper bound with units and rationale |
| `heat_duty` | Duty value and unit |
| `outlet_temperatures` | Hot/cold outlet temperatures with units |
| `approach_temperature` | Minimum approach or MITA basis when available |
| `pressure_drop` | Hot/cold pressure drops |
| `utility_cost` | Utility and cost basis when available |
| `constraint_violations` | Unit, thermal, hydraulic, or operational violations |
| `solver_status` | Converged, failed, timeout, or manually rejected |
| `human_acceptance` | Pending, accepted, rejected, or needs review |

## Acceptance Rules

- Treat surrogate and optimizer outputs as candidate recommendations only.
- Never let an optimizer change property packages, exchanger topology, stream identity, equipment naming, or frozen package boundaries unless the user explicitly reopens the design.
- Do not report "AI controlled the exchanger" unless a real HYSYS workcopy was recalculated and the control authority was explicitly approved.
- For production contexts, phrase the output as advisory optimization, decision support, monitoring, or early warning unless an approved plant writeback procedure exists.
- Preserve failed samples. They are important evidence of design-space limits and model reliability.

## Rejected Shortcuts

- Do not import third-party code into this repository as a dependency just because it demonstrates HYSYS/AI integration.
- Do not download unlicensed `.hsc`, `.hscz`, or plant files as benchmark cases.
- Do not treat Aspen EDR calculations, external ML models, or Excel-only results as HYSYS-native results unless they are explicitly read back from the approved HYSYS/EDR lane.
- Do not claim from-scratch exchanger or LNG cold-box model generation is reliable without a validated case and expert review.

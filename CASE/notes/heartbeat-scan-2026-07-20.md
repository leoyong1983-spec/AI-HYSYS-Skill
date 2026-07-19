# Heartbeat Scan 2026-07-20

## Local Project Experience Watch

The read-only hash comparison found `0` new, `0` changed, and `0` deleted HYSYS-evidence files among the 290 tracked candidates. Evidence types monitored included scripts, structured result/readback files, calculation notes, logs, and workflow documents. No local file was opened for content review because there was no delta, and no private project material was copied into `CASE` or repository documentation.

Local lesson decision: no new lesson adopted and no prior lesson duplicated.

## Public Search And Value Judgment

Searches covered recent HYSYS AI/automation, COM/Python wrappers, MCP servers, LLM process-simulation agents, digital twins, surrogate workflows, and optimization studies. Tracked wrapper and MCP repositories did not expose a newer code revision that changed their assessment. Repeated Sketch2Simulation, PINN, flash-surrogate, product-page, and promotional agent results were not duplicated.

Valuable new source:

- `CASE/research/hysys-hydrogen-liquefaction-optimizer-comparison-2026-07-20.html`
- DOI: `10.1016/j.susoc.2026.03.001`
- Grade: B+ direct research evidence

The peer-reviewed paper compares Aspen HYSYS built-in BOX, genetic algorithm, particle swarm optimization, and knowledge-based optimization for an existing hydrogen-liquefaction model. It uses sensitivity analysis to identify influential variables and set bounds, and reports initialization dependence and local-optimum limitations for some methods.

## Adopted Project Improvement

The transferable rule is optimizer governance, not the paper's case-specific ranking:

- derive bounds from engineering limits and documented sensitivity screening;
- record objective, constraints, optimizer settings, initial point or random seed, stopping rule, failed evaluations, and solver status;
- compare multiple approved starts or seeds for initialization-dependent or stochastic methods when practical;
- rerun the selected candidate in the original HYSYS workcopy and confirm constraint and KPI readback before human acceptance.

Updated `SKILL.md` and `references/control-lane-decision-matrix.md` accordingly. No optimizer package or wrapper was added.

## Limitations And Rejections

- No reusable HYSYS case, source code, or dataset was identified; the saved file is a public university research-portal metadata and abstract snapshot.
- The reported optimizer ranking is specific to the studied flowsheet and must not be generalized without a case-specific benchmark.
- Reflux Agent is retained only as a C+/B- commercial market signal because the public page does not provide reproducible API details, validation evidence, code, or a license basis for adoption.
- `aspen-pysys` remains an alpha watchlist item and is not a default dependency.

## Boundary

This evidence supports `existing HYSYS case -> bounded optimization candidates -> HYSYS rerun/readback -> human acceptance`. It does not support reliable from-scratch HYSYS generation, replacement of the HYSYS baseline, or autonomous production writeback.

# Literature-Derived HYSYS AI Patterns

## Purpose

Use this reference when a task asks about publishability, cites AI/HYSYS papers, or asks an agent to extend the skill from literature.

The repository position is narrow by design: production-facing work should start from an existing runnable HYSYS case, then perform auditable parameter takeover, bounded scenario execution, validation, and reporting.

## Paper-To-Rule Mapping

| Literature pattern | What it supports | Skill rule |
|---|---|---|
| Python/COM automation of Aspen HYSYS | HYSYS can be controlled from scripts for data extraction, sensitivity, and optimization workflows | Use direct COM as the authoritative lane after readiness checks; record launch/open/binding/solver failures separately |
| HYSYS interconnection methodology comparisons | Direct communication, indirect communication, internal spreadsheets, and data tables are distinct lanes | Choose lane before writing; prefer direct COM for lifecycle control and spreadsheet/workbook for stable tagged IO |
| HYSYS + Python full-factorial sensitivity or techno-economic studies | Existing cases can be automated across many parameter combinations | Require scenario matrix, sample IDs, input bounds, KPI schema, failure classification, and rerun policy before full batch execution |
| LLM / multi-agent flowsheet generation for Aspen HYSYS | Agents can generate HYSYS scripts in research settings | Treat greenfield model generation as research/prototype unless a validated case and approved runner exist; preserve prompts, generated code, logs, convergence state, and expert review |
| Text-to-flowsheet with Graph-IR and black-box optimization | Natural-language process descriptions can be translated into an intermediate flowsheet graph and then into a rigorous simulator with validation and optimizer-assisted convergence in research settings | Use Graph-IR as an auditable intent layer, not as proof of HYSYS correctness; allow optimizer-assisted convergence only on whitelisted variables with bounds, residual objective, iteration logs, and final HYSYS/human review |
| SFILES or transformer-based flowsheet autocompletion | Public Aspen Plus or DWSIM flowsheet data can support topology suggestions and interactive completion | Treat autocomplete output as a candidate topology only; convert it into an explicit object/stream map, reject unsupported nodes/edges, and require HYSYS workcopy validation before engineering use |
| LLM agent process-simulation workflows in adjacent simulators | Agentic simulation can be split into task understanding, configuration, evaluation, optimization, and reporting | Use stepwise workflows; do not allow a single prompt to jump directly to engineering conclusions |
| Broad LLM-in-PSE architecture surveys | LLMs can support process design, simulation interfaces, digital twins, optimization, control, and safety workflows | Treat LLMs as constrained interface, orchestration, reasoning, and reporting layers; require explicit tool contracts, simulator readback, validation metrics, fallback behavior, and human acceptance |
| Chemical-engineering MCP design strategies | Industrial agents require field-validated tools for plant data, SOPs, safety constraints, simulation, maintenance, quality, carbon accounting, and operator knowledge | Treat MCP as an auditable tool boundary; prefer read-only-first deployment and require access control, tool-call logs, rollback, failure behavior, and human approval before any write-capable workflow |
| Specialized multi-agent LLMs for process systems engineering | Role-specialized agents can support soft sensing, mechanistic modeling, validation, and NMPC-style control formulation in PSE research | Use role-separated planning/modeling/execution/validation/reporting; require physical consistency, validation metrics, feasibility checks, HYSYS workcopy readback, and human acceptance before recommendations are treated as accepted |
| HYSYS-generated data for ML, surrogate, PINN, or digital twin workflows | HYSYS can serve as a first-principles data source or validation baseline | Require design space, training/validation/test split, error metrics, extrapolation limits, and HYSYS/human review of recommendations |
| HYSYS COM demos with heat-network supertargeting, surrogate modeling, and Bayesian optimization | Public examples show how existing HYSYS cases can be connected to Python for stream/unit-operation mapping, structured parameter changes, HEN screening, and sustainability optimization | Treat mock notebooks and surrogate/BO outputs as advisory; require thermal-stream schema, Delta Tmin basis, utility assumptions, HYSYS workcopy readback, and human review |
| ML-aided flash or thermodynamic surrogate calculations validated against HYSYS | Python-side surrogates can accelerate large batches of thermodynamic or flowsheet evaluations | Treat as acceleration and screening only; require component slate, EOS/property package, P-T-z bounds, pointwise HYSYS comparison, extrapolation limits, and final HYSYS/human review |
| HYSYS/Python/SCADA or digital-twin supervisory studies | HYSYS can connect to external monitoring or supervisory testbeds | Classify as simulation testbed, dashboard, training, or production boundary; default to read-only or human-approved writeback |
| Operational AI / multi-agent setpoint recommendation studies | Agents can propose candidate operating points and use HYSYS-like models for validation | Treat recommendations as advisory; validate candidates on a workcopy and keep production writeback outside the default skill |
| LLM-generated HAZOP or process-safety worksheets | LLMs can draft deviations, causes, consequences, safeguards, and safety-analysis worksheets in research settings | Treat as safety-support drafting only; require validated HYSYS operating-envelope data, PFD/P&ID inputs, explicit nodes/deviations, and qualified human HAZOP-team acceptance |

## Publishable Gap For This Repository

Do not claim that AI-HYSYS-Skill is the first AI + HYSYS work globally. Existing publications already cover HYSYS Python automation, interconnection methods, batch sensitivity, LLM flowsheet generation, HYSYS-generated ML datasets, and digital-twin supervision.

The defensible contribution is:

> an auditable existing-case takeover workflow for Aspen HYSYS that combines AI planning, lane selection, Python/COM or spreadsheet/workbook execution, batch validation, failure classification, and engineering report generation.

## Minimum Evidence For A Paper-Grade Demonstration

Before describing a result as paper-grade, produce:

1. Case provenance: baseline case, workcopy path, HYSYS version, property package, and frozen topology.
2. Lane decision: chosen lane, rejected lanes, and why.
3. Variable schema: object path or spreadsheet/workbook tag, unit, valid range, baseline value, new value, and rollback value.
4. Scenario design: sample ID, variable set, bounds, DOE/full-factorial/optimizer method, and stop rule.
5. Graph or intent representation when text/diagram/autocomplete-to-simulation is involved: source prompt, normalized flowsheet graph or SFILES-like representation, simulator translation, rejected edges/nodes, and human topology review.
6. Optimizer evidence when black-box repair is used: objective function, variable bounds, initial point, iteration count, residual or penalty, failed samples, and stop reason.
7. Runtime evidence: launch/open/binding/solver/export status, timestamps, errors, and rerun decisions.
8. KPI exports: machine-readable CSV/JSON plus concise human-readable summary.
9. Human review: topology, property method, units, convergence, optimization recommendation, and reporting boundary.
10. For HEN or sustainability-surrogate tasks: thermal-stream schema, utility assumptions, `Delta Tmin` basis, stream/unit-operation map, surrogate validity range, and HYSYS workcopy readback.

## Claims To Avoid

- Do not claim reliable production-grade greenfield HYSYS model generation from text, diagrams, or sketches.
- Do not treat flowsheet autocompletion or SFILES graph completion as proof of a runnable HYSYS case.
- Do not claim a surrogate, PINN, or hybrid model replaces the validated HYSYS baseline.
- Do not claim SCADA, Modbus, Aspen OnLine, AVA, PIMS, APC, DCS, or SIS production writeback unless a project-approved procedure exists.
- Do not present wrapper availability, PyPI packages, or code-generation success as runtime validation.
- Do not treat a solved single sample as proof that a full sensitivity matrix is safe.
- Do not present black-box optimization convergence as engineering correctness without HYSYS readback, KPI export, and human review.
- Do not treat MCP availability as simulator validation, authorization, or production writeback approval.
- Do not treat an agent-platform release, default-model change, browser recovery feature, or voice/meeting integration as HYSYS runtime validation.
- Do not treat LLM-generated HAZOP similarity scores, safeguard lists, or safety worksheets as process-safety approval.
- Do not treat a broad LLM-in-PSE architecture survey as evidence that this repository has implemented or validated every cited deployment pattern.
- Do not treat a chemical-engineering MCP design preprint as proof that this repository has implemented a production MCP server or writeback workflow.

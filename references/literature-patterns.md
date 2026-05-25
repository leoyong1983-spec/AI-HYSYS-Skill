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
| LLM agent process-simulation workflows in adjacent simulators | Agentic simulation can be split into task understanding, configuration, evaluation, optimization, and reporting | Use stepwise workflows; do not allow a single prompt to jump directly to engineering conclusions |
| HYSYS-generated data for ML, surrogate, PINN, or digital twin workflows | HYSYS can serve as a first-principles data source or validation baseline | Require design space, training/validation/test split, error metrics, extrapolation limits, and HYSYS/human review of recommendations |
| HYSYS/Python/SCADA or digital-twin supervisory studies | HYSYS can connect to external monitoring or supervisory testbeds | Classify as simulation testbed, dashboard, training, or production boundary; default to read-only or human-approved writeback |
| Operational AI / multi-agent setpoint recommendation studies | Agents can propose candidate operating points and use HYSYS-like models for validation | Treat recommendations as advisory; validate candidates on a workcopy and keep production writeback outside the default skill |

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
5. Runtime evidence: launch/open/binding/solver/export status, timestamps, errors, and rerun decisions.
6. KPI exports: machine-readable CSV/JSON plus concise human-readable summary.
7. Human review: topology, property method, units, convergence, optimization recommendation, and reporting boundary.

## Claims To Avoid

- Do not claim reliable production-grade greenfield HYSYS model generation from text, diagrams, or sketches.
- Do not claim a surrogate, PINN, or hybrid model replaces the validated HYSYS baseline.
- Do not claim SCADA, Modbus, Aspen OnLine, AVA, PIMS, APC, DCS, or SIS production writeback unless a project-approved procedure exists.
- Do not present wrapper availability, PyPI packages, or code-generation success as runtime validation.
- Do not treat a solved single sample as proof that a full sensitivity matrix is safe.

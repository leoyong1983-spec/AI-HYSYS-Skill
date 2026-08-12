---
name: ai-hysys-basic-package
description: "Control Aspen HYSYS with auditable, script-first workflows for existing-case takeover, bounded updates, validation, reporting, and native PFD cleanup. 中文：通过 direct COM、spreadsheet/workbook bridge 或已验证项目脚本接管已有可运行 HYSYS case，完成环境检查、有限调参、验证、导出、原生 PFD 整理和审查阶段基础工艺包交付；不默认支持从零建模或生产写回。"
---

# AI HYSYS Basic Package

## Overview

Use this skill when the task is not theoretical process discussion but actual Aspen HYSYS execution with reproducible artifacts.

Default assumption: the safest production path is takeover of a human-built, already-runnable HYSYS case. Do not treat AI greenfield case construction as the normal path.

中文说明：本技能用于让 AI 以可审计、脚本优先的方式接管已有 Aspen HYSYS 模型，重点是环境验证、控制通道选择、有限参数修改、求解状态检查、结果导出和基础工艺包交付。默认边界是“已有可运行 case 的受控接管”，不是“AI 从零可靠创建生产级 HYSYS 模型”，也不是“无人批准的生产系统写回”。

Prefer scriptable, reviewable, repeatable control lanes:

1. Existing proven project runner
2. Direct `HYSYS.Application` COM automation
3. Spreadsheet or Aspen Simulation Workbook bridge
4. Data tables or special-object lanes when already configured in the case
5. Existing indirect bridges such as Excel / VBA, Matlab, C#, or intermediate files only if already present and working
6. GUI only for layout sign-off or unavoidable visual checks

Read [references/authority-and-path-selection.md](references/authority-and-path-selection.md) before choosing the control lane.

Read [references/control-lane-decision-matrix.md](references/control-lane-decision-matrix.md) before writing parameters, running sensitivity, freezing a baseline, or choosing between direct COM, spreadsheet/workbook, data tables, and indirect communication.

Read [references/literature-patterns.md](references/literature-patterns.md) when a task cites AI/HYSYS papers, asks whether the method is publishable, requests an experiment design, or mixes LLM agents with HYSYS execution.

Read [references/digital-twin-boundary.md](references/digital-twin-boundary.md) when the user asks for HYSYS digital twin, hybrid AI, soft sensor, historian, monitoring, yield optimization, or emissions optimization support.

Read [references/heat-exchanger-ai-patterns.md](references/heat-exchanger-ai-patterns.md) when the user asks for heat exchanger, Aspen EDR, HEN, pinch, `Delta Tmin`, heat duty, LNG cold-box, cryogenic heat-exchanger, or exchanger AI optimization support.

Read [references/project-lessons.md](references/project-lessons.md) when resuming an existing HYSYS project or when a baseline/review/release workflow already exists.

Read [references/pfd-layout-workflow.md](references/pfd-layout-workflow.md) before reorganizing a native HYSYS PFD, moving equipment or labels, preparing a human-handoff layout, or using `scripts/hysys_pfd_layout.py`.

Read [references/basic-package-deliverables.md](references/basic-package-deliverables.md) before generating package outputs.

If the user wants provenance, precedent, launch material, heartbeat source triage, or cross-skill maintenance rules, read [CASE/SOURCE_EVALUATION_RULES.md](CASE/SOURCE_EVALUATION_RULES.md), [CASE/source-index.md](CASE/source-index.md), and [CASE/notes/hysys-source-digest.md](CASE/notes/hysys-source-digest.md) selectively instead of loading the whole `CASE/` tree.

## Workflow

### 1. Gate the execution path

Decide the path in this order:

1. If the workspace already contains proven HYSYS runners, smoke tests, tuning scripts, workbook bridges, or export tools, reuse them first.
2. If direct COM launch works, use `HYSYS.Application` as the default execution lane.
3. If direct `DispatchEx("HYSYS.Application")` fails but the registry contains a valid `LocalServer32`, start the registered `aspenhysys.exe /Automation` server and attach to the active HYSYS object before abandoning native HYSYS.
4. If object-path access is fragile but spreadsheet names or workbook tags are stable, use the spreadsheet bridge.
5. If HYSYS data tables or special objects are already configured and expose the required variables cleanly, use them as supplementary lanes and document the schema.
6. If only an existing indirect bridge is already in service, use it carefully and document that the lane is weaker than direct COM.
7. Do not default to AI greenfield case construction for production work.
8. Do not default to GUI clicking for production work.

Treat direct COM as the authoritative baseline lane because it controls case launch, open, save, and object access directly.

Treat spreadsheets or Aspen Simulation Workbook as stable tagged IO layers, not as the primary truth source, because they simplify automation but can hide deeper object-model issues.

Before any write operation, produce a short lane decision note covering chosen lane, rejected lanes, case source, solver policy, and rollback plan.

### 2. Verify the environment before touching the case

Always check:

1. Aspen HYSYS installation path
2. Aspen HYSYS version
3. Whether the active Python environment can import `pythoncom` and `win32com.client`
4. Whether `HYSYS.Application` launches directly or via registered automation-server fallback
5. Whether a known case can open and save, or whether a minimal smoke-test case can be created and saved when no valid case exists
6. Whether spreadsheet or workbook bridges exist and bind correctly
7. Whether existing case files, workcopies, audits, status files, and package exports already exist

Do not begin tuning or package compilation before confirming which control lane actually works.

Use `scripts/hysys_readiness_check.py` when available. It must classify Python/pywin32 failures, COM registry failures, launch failures, case open/create failures, object-binding failures, and solver failures separately.

For installation, readiness, or version-migration tasks, compare observed HYSYS version, Windows/Office/Python facts, pywin32 state, COM registration, and Aspen product availability against the official platform-support sources in `CASE/official/aspentech-platform-support-2026-05.html` and `CASE/official/aspentech-v15-engineering-platform-specifications-2026.pdf`. Report unsupported or missing platform prerequisites as environment blockers, not as prompt or skill failures.

If multiple lanes work, prefer the one already proven in the current workspace.

### 3. Choose the case with strict priority

Use this priority order:

1. Frozen formal baseline if the task is review support, package compilation, or evidence extraction
2. Latest loadable audited workcopy if the task is bounded tuning or pre-freeze improvement
3. Latest loadable mother case if no frozen or tuned workcopy is available
4. A minimal experimental case only for smoke tests or interface proving when no usable case loads

Never overwrite a frozen baseline.

Do not present a newly AI-built minimal case as equivalent to a validated human-built project baseline.

If a frozen baseline exists, copy it to a new workcopy before any executable change.

### 4. Run with bounded intent

Use explicit run modes:

1. `readiness` for environment and smoke tests
2. `load-and-calculate` for proving the case can run
3. `bounded-tuning` for small, auditable parameter changes
4. `freeze-and-export` for baseline locking and package generation
5. `review-support` for comment closure, consistency checking, and supplemental outputs
6. `layout-review` for native PFD cleanup on a workcopy with calculation-fingerprint verification

For `layout-review`, never overwrite the accepted case. Use `scripts/hysys_pfd_layout.py` with an explicit equipment-coordinate JSON, keep streams topology-driven, then close and reopen the workcopy and prove that material, energy, recycle, object inventory, and solver fingerprints are unchanged.

For simple property-table requests, such as pure hydrogen density from 1 MPa to 90 MPa, prefer a minimal native HYSYS material-stream case after readiness passes. Record the table pressure basis explicitly:

1. `MPa(a)` means the table pressure is written directly as absolute pressure.
2. `MPa(g)` means the table pressure is converted before writing to HYSYS, normally `P_abs = P_gauge + 0.101325 MPa`.
3. Read the HYSYS property directly, for example `MassDensity.GetValue('kg/m3')`, and do not relabel external EOS or fitted values as HYSYS-native results.

For LNG or cryogenic plantwide tasks, first identify the existing HYSYS case, plantwide boundary, multi-stream cryogenic heat exchanger objects, refrigeration or utility KPIs, product quality specs, bottleneck or troubleshooting target, and human review owner. Do not treat an official LNG plantwide simulation source as permission for AI greenfield LNG model generation; use it to structure takeover, bounded tuning, validation, and reporting on an approved workcopy.

For heat-integration, heat exchanger network, pinch-analysis, `Delta Tmin`, supertargeting, or sustainability-surrogate tasks, first identify the source HYSYS case or workbook, thermal-stream schema, stream and unit-operation name map, utility assumptions, objective metrics, surrogate or optimizer role, and human review owner. Treat mock-mode notebooks, Excel-only calculations, surrogate models, and Bayesian optimization outputs as advisory candidates until HYSYS workcopy readback, unit checks, and KPI exports pass.

For bounded tuning:

1. Freeze property method, unit-operation topology, key equipment naming, spreadsheet schema, and already-proven convergence structure unless the user explicitly reopens them.
2. Change one logical variable family at a time.
3. When an external, seasonal, environmental, or calculation-basis input changes, map the dependency from that basis to exact HYSYS write targets. Update only dependent inputs, freeze independent source terms and accepted boundaries, and record both the changed and intentionally unchanged items.
4. Record old value, new value, convergence state, engineering comment, and effect on key KPIs.
5. Prefer the minimum change that clears the target.
6. Stop if the task has moved into review or release support mode.
7. For spreadsheet/workbook writes, pause solver, batch-write inputs, resume solver, wait until `IsSolving` is false, then read KPIs.
8. For a case containing recycle operations, do not accept a single `RecycleConvergence` value as sufficient proof. Record the recycle's `IsIgnored` state, feed/product bindings, solver-idle state, and project-approved tear-stream residuals for mass, temperature, pressure, enthalpy, and composition when available; then save, close, reopen, and repeat the readback before acceptance.
9. If a run reaches a valid staged snapshot but later fails a policy, export, or finalization check, preserve the original error and traceback. Do not relabel the run as successful until a separate finalization step revalidates the reopened staged case, confirms the source-case hash is unchanged, records the previous error, and promotes only the verified artifact.
10. For every pressure write, declare whether the external requirement is gauge or absolute, record the atmospheric-pressure basis used for conversion, write the corresponding absolute pressure to HYSYS, and read the HYSYS pressure back in an explicit absolute unit. Report both the original basis and the converted/readback value; never infer the basis from a bare number or equipment label.
11. For a batch of derived scenarios, start every scenario from the same approved source hash or frozen baseline rather than chaining one scenario from another. Give each scenario an independent workcopy and audit record with `RUNNING`, `PASS`, or `ERROR`; promote only a saved, closed, reopened, and revalidated result. A failed scenario must remain reproducible and must not invalidate or silently alter the other scenarios.
12. Before adding an unfamiliar unit operation through `Flowsheet.Operations.Add(...)`, do not assume its UI label is the registered COM type identifier. On a disposable workcopy with the solver frozen, probe only a bounded candidate list; log each candidate, exception, returned object type, and `VisibleTypeName`; then use the confirmed identifier only inside the approved change boundary. A successful probe proves runtime discoverability, not acceptance of the topology change.
13. For a large or phase-sensitive boundary change, first map every requested value to the exact HYSYS object and physical measurement point; do not confuse compressor discharge, aftercooler outlet, condenser outlet, or a saturation condition. On a disposable workcopy, move from the approved baseline to the target in bounded continuation steps, solving and recording temperature, pressure, vapour fraction, actual volume when capacity matters, and affected KPIs at each accepted step. Near a phase boundary, target temperature alone is insufficient; retain utility/capacity tradeoffs and vendor or human open issues.
14. Before accepting a batch that expands a scenario matrix into multiple case variants, reconcile the planned matrix against the output inventory. Require exactly one unique case ID, independent workcopy, audit record, source hash, output hash, and reopened validation result for every expected matrix cell. Reject missing, duplicate, orphaned, or cross-contaminated outputs, and build aggregate CSV or JSON only from individually `PASS` results; keep failed cells isolated and rerunnable from the approved baseline.
15. Before reconnecting or deleting streams in an existing case, classify each affected stream as a physical equipment path, boundary/input stream, bookkeeping-only stream, or approved recycle/tear stream. Do not allow a bookkeeping stream and its physical counterpart to carry nonzero flow into the same balance. On a disposable workcopy with the solver paused, rewire only mapped physical streams, remove or zero bookkeeping streams only inside the approved boundary, then resume solving and reject nonzero orphaned streams, duplicate feeds, broken equipment bindings, or failed mass/energy closure. Save, close, reopen, and repeat the topology and balance readback before acceptance.

For paper-informed AI/HYSYS tasks, classify the task before executing:

1. Existing-case takeover: production-preferred. Require case provenance, variable schema, smoke test, solver policy, KPI export, and audit log.
2. Batch scenario / sensitivity / techno-economic workflow: require scenario matrix, sample IDs, input bounds, output KPIs, failure classes, and rerun rules before full execution.
3. LLM agent / text-to-simulation / diagram-to-simulation: research or prototype unless a validated case and approved runner exist. Preserve prompts, generated scripts, tool logs, convergence states, and expert review notes.
4. Text-to-flowsheet / Graph-IR / black-box convergence repair: research or bounded-assistance only. Keep topology and parameter intent in an auditable intermediate representation before simulator writes; allow numerical optimization only on whitelisted variables with explicit bounds, objective, residuals, iterations, and rollback.
5. Surrogate / ML / hybrid model / digital twin: HYSYS remains the first-principles baseline. Require design space, training/validation/test split, extrapolation limits, and HYSYS or human review of recommendations.
6. Operational AI / setpoint recommendation: advisory only unless the project provides an approved writeback procedure. Validate candidates on a workcopy, not a production case.

### 5. Export machine-readable outputs first

Prefer `CSV`, `JSON`, and concise `Markdown` summaries before `Word`, `Excel`, or `PowerPoint`.

When an existing case must be inventoried or archived without changing it, prefer HYSYS-native `SimulationCase.GetXMLForCase()` when the installed runtime exposes it. Record source and XML SHA-256, HYSYS version, solver state, XML parse status, and any error; close the source case without saving. Treat the XML as a read-only audit and interchange artifact until a separate import/reopen test proves round-trip and cross-version behavior.

At minimum, export:

1. Key streams
2. Key unit operations
3. Solver status
4. Assumptions and boundary notes
5. Error capture
6. Traceability to the source workcopy

When the project is already in package/review mode, treat the machine-readable layer as the source of truth for formal Office deliverables.

### 6. Enforce release discipline

If any mismatch appears between:

1. Frozen case object inventory
2. Exported result tables
3. Package narrative or equipment list

create a release blocker immediately and switch to blocker-resolution mode.

Do not describe the package as clean for release while a release blocker is still open.

Human decisions stay open until explicitly closed by the user or another authorized human reviewer.

### 6.1 Keep digital twin claims bounded

Official AspenTech digital twin and hybrid model cases can support engineering value, monitoring, diagnosis, optimization, and KPI-reporting workflows.

Do not use those sources to claim that:

1. AI can reliably build a complex HYSYS model from zero.
2. Digital twin automatically means direct COM control.
3. Hybrid models replace the validated HYSYS baseline, property method, topology, or human review.

If a digital twin task is requested, first identify the existing HYSYS baseline, data source, KPI or soft sensor definition, control lane, and human validation responsibility.

If the task mentions online digital twins, Aspen OnLine, AI Model Builder, AspenTech AVA, agentic Industrial AI, or Hybrid Models, separate:

1. offline HYSYS/Aspen Plus model preparation
2. plant data import or historian binding
3. hybrid model or soft-sensor design
4. online publishing or dashboard integration
5. audit and human acceptance

If the task mentions data-driven simulation, surrogate models, machine learning models, or ML-based soft sensors, treat HYSYS as the validated data source and baseline. Require an explicit design space, variable map, train/validation/test split, error metrics, model validity range, extrapolation limits, and human review path. Do not let a surrogate replace HYSYS runtime validation unless the user provides an approved project procedure.

If the task uses active learning, adaptive sampling, uncertainty sampling, or sequential design to reduce HYSYS evaluations, require an approved initial design, acquisition or uncertainty metric, batch size, stopping rule, sample IDs, failed-run handling, and an untouched validation set. Count a sample as HYSYS evidence only after the approved workcopy solves and its outputs are read back; never relabel surrogate predictions or optimizer candidates as HYSYS-generated samples. Revalidate final candidates in HYSYS and keep the active-learning layer advisory until human acceptance.

If the task mentions heat exchangers, Aspen EDR, HEN, pinch analysis, `Delta Tmin`, exchanger duty prediction, cryogenic heat exchangers, LNG cold boxes, or exchanger AI optimization, classify AI/ML/optimizer output as an advisory candidate layer. Require the source HYSYS or HYSYS/EDR case, exchanger and stream name map, hot/cold stream schema, manipulated variables and bounds, heat-duty/outlet-temperature/approach-temperature/pressure-drop KPIs, failed-sample logging, HYSYS or EDR workcopy readback, and human acceptance before reporting any recommendation as accepted.

If the task uses a HYSYS optimizer, genetic algorithm, particle swarm, Bayesian optimization, or another black-box search method, derive the search bounds from engineering limits and a documented sensitivity screen rather than arbitrary ranges. Record the optimizer, objective, constraints, initial point or random seed, stopping rule, failed evaluations, and solver status. For initialization-dependent or stochastic methods, compare multiple approved initial points or seeds when practical, then rerun the selected candidate in the original HYSYS workcopy and confirm the KPI readback before human acceptance. Do not generalize one paper's winning algorithm to a different flowsheet without a case-specific benchmark.

If the task mentions third-party HYSYS Python wrappers or tutorial repositories such as `aspen-pysys`, `aspen_pysys`, `PySIS`, `ap-python`, or `simulator_codingplatform_integration`, do not adopt them as default dependencies. First check license compatibility, alpha/stability status, Python and `pywin32` requirements, whether an existing HYSYS case and COM runtime are available, and whether the wrapper or tutorial code has been smoke-tested in the current workspace. If any check fails, keep using the repository's direct COM starter and spreadsheet/workbook bridge guidance.

If the task changes a distillation-column feed tray or feed location, do not trust one visible stream name or one COM object path by itself. On the approved workcopy, resolve both the feed attached in the main flowsheet and its representation inside the column subflowsheet, normalize and compare the complete feed-name sets, and reject the write when an identity is missing, duplicated, or mismatched. Log the resolved names, original tray, requested tray, solver state, and post-write readback before accepting the change.

If the task replaces or rebuilds an approved subsystem inside an existing case, first hash the source case and capture a calculation fingerprint for the unaffected side. Where thermodynamic pressure levels are needed, prefer explicit HYSYS property or saturation probes with documented composition, temperature, vapor fraction, and units over unlabeled constants. Make topology changes only on a temporary workcopy, keep the approved change boundary narrow, then save, close, reopen, and confirm that the source hash and unaffected-side material, energy, object-inventory, and solver fingerprints have not drifted before accepting the result.

If the task mentions MCP, MCP server, tool server, remote simulator node, or protocol-based simulation control, treat MCP as an orchestration boundary above the existing lanes, not as simulator authority by itself. Require explicit read/write operations, units, schemas, access-control assumptions, single-workcopy lock policy, dry-run mode, audit logs, failure behavior, rollback behavior, and human acceptance before any write-capable HYSYS tool is enabled. HYSYS-specific MCP repositories are community candidate control wrappers that still require license checks, local HYSYS runtime smoke tests, and workcopy-only write discipline before use; AVEVA APS MCP examples remain architecture references only, not portable HYSYS APIs.

If the task mentions HEN supertargeting, pinch analysis, `Delta Tmin`, Bayesian optimization, LCSI, sustainability assessment, or HDA-style surrogate optimization, separate the spreadsheet/notebook layer, surrogate/optimizer layer, and HYSYS runtime layer. Require thermal-stream units, hot/cold stream classification, utility assumptions, minimum approach-temperature basis, HYSYS object mapping, and final workcopy validation before accepting recommendations.

If the task mentions ML-aided flash calculations, thermodynamic surrogates, accelerated flash evaluation, or Python-side property surrogate models, classify it as a simulation-acceleration layer. Require component slate, EOS/property package, pressure-temperature-composition bounds, HYSYS reference-data provenance, error metrics, extrapolation limits, and final HYSYS or human engineering review before accepting any result.

If the task mentions HYSYS Dynamics, online simulation, live process digital twin, Aspen OnLine, production planning, PIMS, Aspen DMC3, APC, distributed control systems, or DCS, split the work into offline model preparation, dynamic/online conversion prerequisites, external commercial-system boundaries, validation evidence, and human acceptance. Do not imply this skill can publish online models, replace PIMS/DMC3/APC/DCS, or close a production loop by itself.

If the task mentions Aspen OnLine or online HYSYS digital twins, require explicit input/output tag schema, plant-data source, schedule/run policy, case-history or replay path, KPI/reporting schema, failure handling, external APC/DCS boundary, and human acceptance record before any execution or recommendation.

If the task mentions ammonia, urea, fertilizer, `NH3-CO2-H2O`, ElecNRTL, first-principles OTS, or HYSYS Dynamics operator-training scenarios, require an existing dynamic case or validated conversion plan, property-package basis, dynamic holdup and pressure-flow assumptions, DCS/SIS loop map, training-scenario list, trainee acceptance criteria, failure behavior, and human sign-off. Treat embedded DCS/SIS logic as simulation/training evidence only unless the project provides a separate qualified safety and production approval path.

If the task mentions third-party rigorous models such as MySep, multi-unit plant digital twins, refinery process digital twins, live KPI monitoring, or unmeasured KPI inference, identify the HYSYS baseline, external model boundary, live data source, KPI schema, model version, and human acceptance owner before any automation work. Do not imply this skill can reproduce commercial live digital twin products or write recommendations directly to production systems.

If the task mentions LLM agents, text-to-simulation, flowsheet synthesis, diagram-to-simulation, or autonomous case construction, treat it as research/prototyping unless an existing validated HYSYS case or approved project runner is available. Prefer step-by-step construction over single-prompt generation, preserve tool logs and convergence status, and require human review of topology, property package, parameters, units, and solver results before any engineering use.

If the task mentions text-to-flowsheet, Graph-IR, black-box optimization, convergence repair, or optimizer-assisted simulation, separate the AI intent layer from the HYSYS execution layer. The AI may propose topology or candidate parameters, but HYSYS writes must still use an approved workcopy and a chosen control lane. A numerical optimizer may only adjust pre-approved variables within documented engineering bounds; it must not silently change property packages, unit-operation topology, equipment naming, frozen baselines, or reporting boundaries. Log the objective function, input bounds, initial point, iterations, residual or penalty value, solver status, failed samples, final KPI export, and human acceptance note.

If the task mentions SFILES, flowsheet autocompletion, graph completion, or transformer-generated flowsheet suggestions, treat the output as a candidate intent artifact. Convert it into an explicit stream/unit-operation map, record unsupported nodes and rejected edges, and validate against an existing HYSYS workcopy or approved runner before any engineering conclusion.

If the task mentions specialized multi-agent process-systems-engineering workflows, soft sensors, calibration, dynamic modeling, NMPC, or control recommendation generation, split the work into role-separated planning, modeling, execution, validation, and reporting steps. Require physical-consistency checks, validation metrics, feasibility checks, workcopy readback, and human acceptance before reporting any model or control recommendation as accepted. Do not treat a multi-agent result as production writeback permission.

If the task mentions hierarchical agents, chemical process development agents, knowledge/concept/parameter cohorts, or CeProAgents-style workflows, keep the stages separate: knowledge retrieval, concept generation, parameter write-set construction, simulation execution, validation, and reporting. Do not let a concept-generation agent write directly into HYSYS. Require an explicit workcopy, variable schema, bounds, rollback values, solver evidence, KPI export, and human review before accepting any generated process configuration.

If an LLM proposes or infers operating constraints, optimization bounds, feasible ranges, or missing parameter limits, treat them as hypotheses until validated. Record the source rationale, baseline value, proposed lower/upper bound, engineering unit, rollback value, and rejection criteria. Do not write inferred bounds into HYSYS or run optimizer sweeps until they pass engineering range checks, workcopy readback, failed-sample logging, and human acceptance.

If the task cites broad LLM-in-process-systems-engineering architectures or surveys, map the claim to a specific lane before acting: interface, orchestration, simulation execution, digital twin supervision, optimization, control recommendation, safety support, or reporting. Require explicit tool contracts, deterministic HYSYS or approved-simulator readback, validation metrics, fallback behavior, and human acceptance. Do not treat a literature survey as implementation evidence for this repository.

If the task mentions MCP, MCP server, tool server, remote simulator node, or protocol-based simulation control, treat MCP as an orchestration boundary above the existing lanes, not as a simulator authority by itself. The MCP tool contract must expose explicit read/write operations, units, schemas, authentication assumptions, access-control assumptions, single-workcopy lock policy, dry-run mode, audit logs, failure behavior, and rollback behavior before any write operation. Prefer read-only-first deployment and require human acceptance before enabling write-capable HYSYS or plant-data tools. Do not imply distributed or production writeback capability unless the project has a configured runtime, approval owner, and tested recovery path.

If designing a HYSYS MCP or COM wrapper, expose lifecycle and health tools before write tools: open/close/save, status, probe, run/reinit, stop, result readback, and error classification. Keep HYSYS COM ownership in one process/thread boundary or an explicit STA-style worker; document retry and reconnect limits; serialize writes against one workcopy; and log every tool call, unit, old value, new value, solver status, rollback value, and human acceptance state. Adjacent Aspen Plus MCP examples are architecture references only, not portable HYSYS APIs.

Public HYSYS MCP servers are still candidate implementations until validated in the current local runtime. Learn from read-only/default/enhanced mode separation and explicit tool tagging, but do not install, expose, or rely on a third-party MCP server as the default control lane without local HYSYS smoke tests, permission review, failure recovery checks, and maintainer approval.

If the task mentions AVA-style or agentic operational AI recommendations, treat the AI layer as advisory workflow support unless a project-approved writeback procedure exists. Identify the validated HYSYS baseline, data source, first-principles or hybrid model boundary, recommendation target, approval owner, and audit trail before producing or applying any recommendation.

If the task mentions SCADA, ScadaBR, Modbus, OPC, external supervisory interfaces, dashboards, operator training, or online monitoring, first classify the lane as simulation testbed, training system, engineering dashboard, or production control boundary. Require tag schema, read/write direction, units, refresh rate, failure behavior, rollback, and human approval before any writeback. Do not treat a SCADA bridge as permission for autonomous DCS/APC/SIS or production-loop control.

If the task mentions carbon accounting, decarbonization, energy-saving optimization, or reasoning-agent process simulation, separate simulator outputs, optimization variables, energy scenarios, carbon factors, reporting boundary, uncertainty, and human engineering review. Treat Aspen Plus agent papers as adjacent workflow evidence, not as proof that HYSYS greenfield model construction is reliable.

If the task mentions HAZOP, process hazard analysis, safeguard review, alarm review, interlocks, SIS, deviation worksheets, or operating envelope review, classify the task as safety-support only. Start from a validated HYSYS case, exported operating envelope, PFD/P&ID inputs, and explicit node/deviation definitions. LLM-generated causes, consequences, safeguards, alarms, interlocks, or SIS suggestions are advisory drafts; require qualified human HAZOP-team review before any safety item is treated as accepted or closed.

### 7. Keep the package at the right depth

This skill is for review-stage basic process package work, not detailed design by default.

Do not silently upgrade the project claim from:

- review-stage basic process package

to:

- detailed design

unless the user explicitly changes the project stage and depth.

Detailed sizing, full control philosophy, full safeguards/interlocks, and full datasheets belong to a later phase unless the project explicitly says otherwise.

### 8. Chinese-first delivery rule

If the project requires Chinese submission:

1. Use Chinese for reader-facing file names and 正文.
2. Keep necessary English only for paths, file extensions, stream tags, equipment tags, API names, object names, or standard abbreviations.
3. Add Chinese annotations for reader-visible English terms that remain.
4. Do not mistake console mojibake for real file corruption; verify with UTF-8 reads or formal extraction tools before editing.

### 9. Keep agent state and model compatibility explicit

For long-running HYSYS tasks, create or update a machine-readable checkpoint before and after each major stage:

1. lane decision
2. readiness check
3. case selection or workcopy creation
4. planned write set
5. solver run
6. KPI export
7. release or handoff summary

At minimum, the checkpoint should record run mode, source case, workcopy path, HYSYS version if known, property package if known, frozen topology boundary, variable schema, valid ranges, rollback values, solver policy, output paths, open human decisions, and last successful stage.

For resumable batch execution, keep one checkpoint and output namespace per scenario. On restart, verify the source hash and reuse only a scenario whose reopened result already passed; rerun `RUNNING`, incomplete, or `ERROR` scenarios from the approved baseline instead of continuing from an uncertain live COM session.

If the agent host, model, provider, prompt template, or JSON schema changes, run a small schema smoke test before any HYSYS write. Treat invalid JSON, missing units, missing rollback values, unknown object paths, or changed enum names as blockers, not as minor formatting issues.

If multiple agents or models are used, keep one writer lane per workcopy. A supervisor agent may audit checkpoints, compare planned versus actual writes, and request rollback, but it must not share live HYSYS COM handles, issue parallel writes, or close human decisions by itself.

Voice calls, meetings, browser automation, and web dashboards are presentation or lookup layers. They may summarize results, retrieve documentation, or support human review, but they are not HYSYS execution authority and must not replace COM/workbook evidence, solver logs, KPI exports, or human acceptance.

## Guardrails

- Do not claim a case solved if it did not.
- Do not mix launch failure, case open failure, object-binding failure, and solver failure.
- Do not replace auditable script control with GUI-only actions.
- Do not overwrite a frozen baseline.
- Do not reopen free tuning after the project enters package review unless the user explicitly authorizes it.
- Do not close human decisions without explicit human direction.
- Do not assume AI can build a production-ready HYSYS flowsheet from zero just because COM object creation works.
- Do not bind the skill to a specific agent runtime or default model unless the user explicitly configures that runtime and the schema smoke test passes.
- Do not treat voice, meeting, browser, or dashboard integration as permission to write to HYSYS.
- Do not let AI-generated HAZOP, safeguard, alarm, interlock, or SIS recommendations close process-safety decisions without qualified human review.

## Source hierarchy

Use external knowledge in this order:

1. Official AspenTech HYSYS and Aspen Simulation Workbook product/support/training material
2. Proven project-local runners, logs, and validated workcopies
3. Community spreadsheet-bridge examples and reusable HYSYS automation snippets
4. Recent AI-for-HYSYS or process-simulation agent research when the user asks for agentic, diagram-to-simulation, text-to-simulation, surrogate-model, LNG optimization, production-planning, or digital-twin workflows
5. Secondary community material only as fallback

Treat paper evidence as precedent, not permission. A paper showing HYSYS/Python automation, LLM flowsheet generation, surrogate optimization, or digital-twin validation changes the task classification and required evidence; it does not remove runtime readiness, case provenance, solver validation, or human review requirements.

Do not adopt third-party HYSYS Python wrappers as default dependencies just because a package exists on PyPI. For candidates such as `aspen_pysys`, first check license compatibility, alpha/stability status, Python and pywin32 requirements, whether an existing HYSYS case and COM runtime are available, and whether the wrapper has been smoke-tested in the current workspace. If any of those checks fail, keep using the repository's direct COM starter and spreadsheet/workbook bridge guidance.

When extending the direct COM layer, keep wrapper ideas but not wrapper code: use per-session object caches only, normalize COM tuple/list/array-like readbacks before validation or reporting, and do not share live HYSYS COM handles across processes.

## Output expectations

When this skill is used well, the result should be a chain of artifacts, not just advice:

1. Workcopy or frozen baseline reference
2. Logs showing what lane was used and why
3. Calculation or tuning outputs
4. Export tables
5. Package-stage formal deliverables or review-support files when requested

For property-table outputs, include the HYSYS version, property package, component list, pressure basis, pressure conversion if any, density property path, source case path, CSV/JSON outputs, and run log.

---
name: ai-hysys-basic-package
description: "Control Aspen HYSYS with auditable, script-first workflows to take over, update, tune, freeze, export, and visually organize an existing process case. Use when Codex must use direct COM automation, spreadsheet/workbook bridges, or proven project runners to verify the environment, load a validated case, run calculations, perform bounded tuning, export results, compile review-stage basic process package deliverables, or rearrange a native PFD on a workcopy without changing calculation boundaries."
---

# AI HYSYS Basic Package

## Overview

Use this skill when the task is not theoretical process discussion but actual Aspen HYSYS execution with reproducible artifacts.

Default assumption: the safest production path is takeover of a human-built, already-runnable HYSYS case. Do not treat AI greenfield case construction as the normal path.

Prefer scriptable, reviewable, repeatable control lanes:

1. Existing proven project runner
2. Direct `HYSYS.Application` COM automation
3. Spreadsheet or Aspen Simulation Workbook bridge
4. Data tables or special-object lanes when already configured in the case
5. Existing indirect bridges such as Excel / VBA, Matlab, C#, or intermediate files only if already present and working
6. GUI only for layout sign-off or unavoidable visual checks

Read [references/authority-and-path-selection.md](references/authority-and-path-selection.md) before choosing the control lane.

Read [references/control-lane-decision-matrix.md](references/control-lane-decision-matrix.md) before writing parameters, running sensitivity, freezing a baseline, or choosing between direct COM, spreadsheet/workbook, data tables, and indirect communication.

Read [references/digital-twin-boundary.md](references/digital-twin-boundary.md) when the user asks for HYSYS digital twin, hybrid AI, soft sensor, historian, monitoring, yield optimization, or emissions optimization support.

Read [references/heat-exchanger-ai-patterns.md](references/heat-exchanger-ai-patterns.md) when the user asks for heat exchanger, Aspen EDR, HEN, pinch, `Delta Tmin`, heat duty, LNG cold-box, cryogenic heat-exchanger, or exchanger AI optimization support.

Read [references/project-lessons.md](references/project-lessons.md) when resuming an existing HYSYS project or when a baseline/review/release workflow already exists.

Read [references/pfd-layout-workflow.md](references/pfd-layout-workflow.md) before reorganizing a native HYSYS PFD, moving equipment or labels, preparing a human-handoff layout, or using `scripts/hysys_pfd_layout.py`.

Read [references/basic-package-deliverables.md](references/basic-package-deliverables.md) before generating package outputs.

If the user wants provenance, precedent, or launch material, read [CASE/source-index.md](CASE/source-index.md) and [CASE/notes/hysys-source-digest.md](CASE/notes/hysys-source-digest.md) selectively instead of loading the whole `CASE/` tree.

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

For bounded tuning:

1. Freeze property method, unit-operation topology, key equipment naming, spreadsheet schema, and already-proven convergence structure unless the user explicitly reopens them.
2. Change one logical variable family at a time.
3. Record old value, new value, convergence state, engineering comment, and effect on key KPIs.
4. Prefer the minimum change that clears the target.
5. Stop if the task has moved into review or release support mode.
6. For spreadsheet/workbook writes, pause solver, batch-write inputs, resume solver, wait until `IsSolving` is false, then read KPIs.
7. For a case containing recycle operations, do not accept a single `RecycleConvergence` value as sufficient proof. Record the recycle's `IsIgnored` state, feed/product bindings, solver-idle state, and project-approved tear-stream residuals for mass, temperature, pressure, enthalpy, and composition when available; then save, close, reopen, and repeat the readback before acceptance.
8. If a run reaches a valid staged snapshot but later fails a policy, export, or finalization check, preserve the original error and traceback. Do not relabel the run as successful until a separate finalization step revalidates the reopened staged case, confirms the source-case hash is unchanged, records the previous error, and promotes only the verified artifact.
9. For every pressure write, declare whether the external requirement is gauge or absolute, record the atmospheric-pressure basis used for conversion, write the corresponding absolute pressure to HYSYS, and read the HYSYS pressure back in an explicit absolute unit. Report both the original basis and the converted/readback value; never infer the basis from a bare number or equipment label.

### 5. Export machine-readable outputs first

Prefer `CSV`, `JSON`, and concise `Markdown` summaries before `Word`, `Excel`, or `PowerPoint`.

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

If the task mentions online digital twins, Aspen OnLine, AI Model Builder, or Hybrid Models, separate:

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

If the task mentions HYSYS Dynamics, online simulation, live process digital twin, Aspen OnLine, production planning, PIMS, distributed control systems, OTS, operator training, DCS/SIS loop training, or APC, split the work into offline model preparation, dynamic/online conversion prerequisites, external commercial-system boundaries, validation evidence, and human acceptance. Do not imply this skill can publish online models, replace PIMS/APC/DCS/OTS platforms, or close a production loop by itself.

If the task mentions ammonia, urea, fertilizer, `NH3-CO2-H2O`, ElecNRTL, first-principles OTS, or HYSYS Dynamics operator-training scenarios, require an existing dynamic case or validated conversion plan, property-package basis, dynamic holdup and pressure-flow assumptions, DCS/SIS loop map, training-scenario list, trainee acceptance criteria, failure behavior, and human sign-off. Treat embedded DCS/SIS logic as simulation/training evidence only unless the project provides a separate qualified safety and production approval path.

If the task mentions third-party rigorous models such as MySep, multi-unit plant digital twins, refinery process digital twins, live KPI monitoring, or unmeasured KPI inference, identify the HYSYS baseline, external model boundary, live data source, KPI schema, model version, and human acceptance owner before any automation work. Do not imply this skill can reproduce commercial live digital twin products or write recommendations directly to production systems.

If the task mentions LLM agents, text-to-simulation, flowsheet synthesis, diagram-to-simulation, or autonomous case construction, treat it as research/prototyping unless an existing validated HYSYS case or approved project runner is available. Prefer step-by-step construction over single-prompt generation, preserve tool logs and convergence status, and require human review of topology, property package, parameters, units, and solver results before any engineering use.

If the task mentions SCADA, ScadaBR, Modbus, OPC, external supervisory interfaces, dashboards, operator training, or online monitoring, first classify the lane as simulation testbed, training system, engineering dashboard, or production control boundary. Require tag schema, read/write direction, units, refresh rate, failure behavior, rollback, and human approval before any writeback. Do not treat a SCADA bridge as permission for autonomous DCS/APC/SIS or production-loop control.

If the task mentions carbon accounting, decarbonization, energy-saving optimization, or reasoning-agent process simulation, separate simulator outputs, optimization variables, energy scenarios, carbon factors, reporting boundary, uncertainty, and human engineering review. Treat Aspen Plus agent papers as adjacent workflow evidence, not as proof that HYSYS greenfield model construction is reliable.

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

## Guardrails

- Do not claim a case solved if it did not.
- Do not mix launch failure, case open failure, object-binding failure, and solver failure.
- Do not replace auditable script control with GUI-only actions.
- Do not overwrite a frozen baseline.
- Do not reopen free tuning after the project enters package review unless the user explicitly authorizes it.
- Do not close human decisions without explicit human direction.
- Do not assume AI can build a production-ready HYSYS flowsheet from zero just because COM object creation works.

## Source hierarchy

Use external knowledge in this order:

1. Official AspenTech HYSYS and Aspen Simulation Workbook product/support/training material
2. Proven project-local runners, logs, and validated workcopies
3. Community spreadsheet-bridge examples and reusable HYSYS automation snippets
4. Recent AI-for-HYSYS or process-simulation agent research when the user asks for agentic, diagram-to-simulation, text-to-simulation, surrogate-model, LNG optimization, production-planning, or digital-twin workflows
5. Secondary community material only as fallback

## Output expectations

When this skill is used well, the result should be a chain of artifacts, not just advice:

1. Workcopy or frozen baseline reference
2. Logs showing what lane was used and why
3. Calculation or tuning outputs
4. Export tables
5. Package-stage formal deliverables or review-support files when requested

For property-table outputs, include the HYSYS version, property package, component list, pressure basis, pressure conversion if any, density property path, source case path, CSV/JSON outputs, and run log.

---
name: ai-hysys-basic-package
description: "Control Aspen HYSYS with auditable, script-first workflows to take over, update, tune, freeze, and export an existing process case. Use when Codex must take over Aspen HYSYS through direct COM automation, spreadsheet/workbook bridges, or proven project runners to: (1) verify the environment, (2) load an existing validated case, (3) run calculations, (4) perform bounded sensitivity or tuning, (5) export machine-readable results, or (6) compile review-stage basic process package deliverables without changing frozen calculation boundaries."
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

Read [references/project-lessons.md](references/project-lessons.md) when resuming an existing HYSYS project or when a baseline/review/release workflow already exists.

Read [references/basic-package-deliverables.md](references/basic-package-deliverables.md) before generating package outputs.

If the user wants provenance, precedent, or launch material, read [CASE/source-index.md](CASE/source-index.md) and [CASE/notes/hysys-source-digest.md](CASE/notes/hysys-source-digest.md) selectively instead of loading the whole `CASE/` tree.

## Workflow

### 1. Gate the execution path

Decide the path in this order:

1. If the workspace already contains proven HYSYS runners, smoke tests, tuning scripts, workbook bridges, or export tools, reuse them first.
2. If direct COM launch works, use `HYSYS.Application` as the default execution lane.
3. If object-path access is fragile but spreadsheet names or workbook tags are stable, use the spreadsheet bridge.
4. If HYSYS data tables or special objects are already configured and expose the required variables cleanly, use them as supplementary lanes and document the schema.
5. If only an existing indirect bridge is already in service, use it carefully and document that the lane is weaker than direct COM.
6. Do not default to AI greenfield case construction for production work.
7. Do not default to GUI clicking for production work.

Treat direct COM as the authoritative baseline lane because it controls case launch, open, save, and object access directly.

Treat spreadsheets or Aspen Simulation Workbook as stable tagged IO layers, not as the primary truth source, because they simplify automation but can hide deeper object-model issues.

Before any write operation, produce a short lane decision note covering chosen lane, rejected lanes, case source, solver policy, and rollback plan.

### 2. Verify the environment before touching the case

Always check:

1. Aspen HYSYS installation path
2. Aspen HYSYS version
3. Whether `HYSYS.Application` launches
4. Whether a known case can open and save
5. Whether spreadsheet or workbook bridges exist and bind correctly
6. Whether existing case files, workcopies, audits, status files, and package exports already exist

Do not begin tuning or package compilation before confirming which control lane actually works.

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

For bounded tuning:

1. Freeze property method, unit-operation topology, key equipment naming, spreadsheet schema, and already-proven convergence structure unless the user explicitly reopens them.
2. Change one logical variable family at a time.
3. Record old value, new value, convergence state, engineering comment, and effect on key KPIs.
4. Prefer the minimum change that clears the target.
5. Stop if the task has moved into review or release support mode.
6. For spreadsheet/workbook writes, pause solver, batch-write inputs, resume solver, wait until `IsSolving` is false, then read KPIs.

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
4. Recent AI-for-HYSYS research when the user asks for agentic or diagram-to-simulation workflows
5. Secondary community material only as fallback

## Output expectations

When this skill is used well, the result should be a chain of artifacts, not just advice:

1. Workcopy or frozen baseline reference
2. Logs showing what lane was used and why
3. Calculation or tuning outputs
4. Export tables
5. Package-stage formal deliverables or review-support files when requested

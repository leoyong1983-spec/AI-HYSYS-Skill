# Heartbeat Scan 2026-07-13

## Search Scope

Searched for recent credible sources about AI controlling Aspen HYSYS, HYSYS COM/Python automation, spreadsheet/workbook bridges, LLM agents for process simulation, HYSYS digital twins, HYSYS Dynamics, and operator-training workflows.

## Valuable Finding

The valuable new source is AspenTech's official Aspen Operator Training product page, plus the linked official "Top 10 Questions About Aspen Operator Training" FAQ PDF.

Saved evidence:

- `CASE/official/aspen-operator-training-product-page-2026-07-13.html`
- `CASE/official/aspen-operator-training-faq-ots-2017.pdf`

Value grade: B+

Reason:

- Official AspenTech product-level source.
- Directly connects Aspen Operator Training with dynamic simulation, DCS-agnostic OTS, Inprocess software, and Aspen HYSYS Dynamic Lifecycle.
- Strengthens the project boundary for HYSYS Dynamics, OTS, operator-training scenarios, DCS/SIS loop mapping review, KPI capture, and audit/report support.

## Project Impact

This evidence improves the public source pack and the digital-twin / OTS boundary documentation. It does not require a new control path or dependency.

Adopted:

- Added source-pack entries to `CASE/source-index.md`.
- Added a digest conclusion to `CASE/notes/hysys-source-digest.md`.
- Added an official OTS boundary update to `references/digital-twin-boundary.md`.

Not changed:

- `SKILL.md` was not changed because it already contains OTS, operator-training, HYSYS Dynamics, ammonia/urea, DCS/SIS, and production-writeback boundary clauses.

## Boundary Judgment

This source is official OTS / HYSYS Dynamics evidence. It is not evidence that AI can autonomously control production HYSYS models, replace commercial OTS platforms, replace DCS/SIS engineering, or reliably build HYSYS models from zero.

For OTS-style work, the skill must continue to require an existing dynamic model or validated conversion plan, property-package basis, dynamic assumptions, DCS/SIS loop mapping, training-scenario scope, failure behavior, replay/audit logs, and human acceptance.

## Rejected Or Deferred Items

Repeated MCP wrapper, process-simulation-agent, and PSE survey results were already covered by prior CASE entries and were not duplicated.

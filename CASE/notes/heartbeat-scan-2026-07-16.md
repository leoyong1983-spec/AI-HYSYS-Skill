# Heartbeat Scan 2026-07-16

## Search Scope

Searched for recent credible sources about AI controlling Aspen HYSYS, HYSYS COM/Python/Excel/workbook automation, MCP tool servers, LLM process-simulation agents, digital twins, hybrid AI, and operator-training workflows. Results were compared with `CASE/source-index.md` through the 2026-07-14 entry.

## Valuable Finding

The useful source is AspenTech's official EHY2311 course page, "Developing Automation Solutions for Aspen HYSYS." It was previously deferred because the support site timed out, but the page is now accessible and has been saved as a valid HTML snapshot.

Saved evidence:

- `CASE/official/aspentech-ehy2311-hysys-automation-course-2026-07-16.html`

Value grade: B+

Reason:

- Official AspenTech training source dedicated to HYSYS automation.
- Explicitly covers the HYSYS Type Library and Excel Object Browser.
- Includes Visual Basic/VBA, User Variables, User Operations, debugging, and linking process information across simulations.
- Directly supports the repository's existing direct-COM and Excel/spreadsheet/workbook control-lane taxonomy.

## Project Impact

Adopted:

- Added the official snapshot and source-index entry.
- Strengthened `references/authority-and-path-selection.md` with the specific EHY2311 evidence.
- Added this conclusion to the source digest.

Not changed:

- `SKILL.md` already prioritizes proven runners, direct COM, and spreadsheet/workbook bridges, so no new execution rule was necessary.
- No dependency or automation wrapper was added.

## Boundary Judgment

The course confirms that HYSYS exposes supported automation and customization concepts. It does not prove that this repository has locally exercised every Type Library object, User Variable, or User Operation, and it does not authorize production writeback.

For project execution, the repository must still require runtime readiness, a known workcopy, one-point object-binding tests, explicit units, solver policy, rollback, audit output, and human acceptance before batch writes.

## Rejected Or Deferred Items

- `aspen-pysys` remains at PyPI `0.1.0a3`; no new release was found.
- The tracked HYSYS MCP and wrapper repositories show no newer code push that changes the current assessment.
- The July 2026 hydrogen ANN/GA paper uses Aspen Plus rather than HYSYS and therefore was not added as direct HYSYS evidence.
- Repeated Sketch2Simulation, PINN, ML-flash, OTS, and product-page results were already indexed.
- General training listings and social-media discussions did not add implementation evidence.

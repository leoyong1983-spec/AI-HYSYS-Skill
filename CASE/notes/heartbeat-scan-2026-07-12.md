# Heartbeat Scan - 2026-07-12

## Search scope

Searched for recent credible sources about AI controlling Aspen HYSYS, HYSYS automation via COM/Python/spreadsheets/workbooks, LLM agents for process simulation, and HYSYS digital twin or hybrid AI workflows.

## Valuable findings

### Inprocess OPTIMIZE 26 technical contributions

- Source: `https://inprocessgroup.com/inprocess-achieves-strong-visibility-at-aspentech-optimize-2026-through-multiple-technical-contributions/`
- Local snapshot: `CASE/community/inprocess-optimize26-technical-contributions-2026-07-12.html`
- Value grade: `B`
- Why it matters: This industry source records multiple AspenTech OPTIMIZE 26 presentations tied to process simulation, dynamic modeling, digital twin methods, Aspen HYSYS-based OTS, Aspen HYSYS Dynamics, real-time dynamic simulation, and refinery lifecycle safety.
- Boundary: It is credible operating-context evidence, not proof that AI can autonomously control production HYSYS models or build complex HYSYS cases from zero.

### First-principles OTS for a urea plant

- Source: `https://inprocessgroup.com/when-a-single-incident-pays-for-a-decade-of-training-a-first-principles-operator-training-system-for-a-urea-plant-and-the-business-case-for-building-one/`
- Local snapshot: `CASE/community/inprocess-urea-plant-ots-hysys-dynamics-2026-07-12.html`
- Value grade: `B+`
- Why it matters: The article explicitly describes a high-fidelity urea-plant OTS for ammonia and urea facilities built on Aspen HYSYS Dynamics with Aspen Properties and ElecNRTL for non-ideal `NH3-CO2-H2O` chemistry. It also states that DCS loops and SIS interlocks are embedded in the simulation.
- Boundary: This supports dynamic-simulation, OTS, training, and operator-readiness workflows. It does not authorize this repository to close a production control loop or to treat DCS/SIS logic as accepted without qualified project review.

### Inprocess OPTIMIZE 26 IPA OTS poster

- Source: `https://inprocessgroup.com/wp-content/uploads/2026/06/OPTIMIZE-26-Poster-IPA_final.pdf`
- Local snapshot: `CASE/community/inprocess-optimize26-ipa-hysys-dynamics-ots-poster-2026-07-12.pdf`
- Value grade: `B`
- Why it matters: The PDF is a downloadable industry poster and confirms the same HYSYS Dynamics OTS / operator-readiness pattern in another plant context.
- Boundary: It is OTS and dynamic-simulation evidence, not autonomous AI-control evidence.

### AspenTech OPTIMIZE 26 performance-engineering page

- Source: `https://solutions.aspentech.com/en/resources/video/performance-engineering-for-operations-at-optimize-26`
- Local snapshot: `CASE/official/aspentech-optimize26-performance-engineering-operations-2026-07-12.html`
- Value grade: `B-`
- Why it matters: Official AspenTech event page metadata mentions performance engineering, dynamic process simulation, real-time calibration, digital twin, urea process, and AI in the same operations context.
- Boundary: This is event-positioning evidence with limited technical depth. It should support framing only, not execution claims.

## Project changes

- Added the source snapshots above to `CASE/`.
- Updated `CASE/source-index.md` with a 2026-07-12 index block.
- Updated `references/digital-twin-boundary.md` with OTS and fertilizer-plant dynamic-simulation boundaries.
- Updated `SKILL.md` so OTS / operator-training / ammonia-urea dynamic-model tasks require explicit baseline, property package, DCS/SIS mapping, training-scenario scope, and human acceptance.

## Rejected or deferred findings

- Repeated HYSYS MCP and wrapper sources were already covered by the 2026-07-03 to 2026-07-06 entries, so no duplicate snapshots were added.
- Broad Aspen Plus MCP material was not added because the repository already has stronger HYSYS-specific MCP evidence.
- Promotional or low-detail event pages were only saved when they added official or direct HYSYS Dynamics context; they were not used to expand repository claims.

## Boundary conclusion

The new evidence strengthens the repository's support for existing HYSYS Dynamics cases, OTS, operator training, DCS/SIS mapping reviews, and dynamic-simulation reporting. It does not change the core AI-HYSYS-Skill boundary: production-preferred work remains existing-case takeover, bounded parameter changes, validation, export, and human-reviewed reporting.

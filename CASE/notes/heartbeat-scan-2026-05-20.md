# Heartbeat scan 2026-05-20

Automation ID: `ai-hysys-daily-scan`

Worktree used: `D:\SKILL\AI-HYSYS-Skill-heartbeat-main`

## Search focus

Searched for latest credible sources around Aspen HYSYS automation, COM/Python/spreadsheet/workbook control, LLM agents for process simulation, AspenTech AVA, digital twins, hybrid AI, and HYSYS runtime/platform support.

## New valuable sources

### AspenTech Platform Support

- Source: https://www.aspentech.com/en/platform-support
- Local snapshot: [../official/aspentech-platform-support-2026-05.html](../official/aspentech-platform-support-2026-05.html)
- Quality: A
- Category: official platform/support evidence
- Value: high for installation, readiness, version migration, and product-family boundary checks.

### AspenTech V15 Engineering Platform Specifications

- Source: https://www.aspentech.com/-/media/aspentech/home/platform-support/v15/v15engspecs.pdf
- Local PDF: [../official/aspentech-v15-engineering-platform-specifications-2026.pdf](../official/aspentech-v15-engineering-platform-specifications-2026.pdf)
- SHA256: `4d65db675f1b597aa5921101dd066e694c202bc2ab457c4726269ecdb79912ac`
- Quality: A
- Category: official platform specification
- Value: high for distinguishing runtime/platform prerequisites from AI-HYSYS-Skill logic.

## Value judgment

These sources are worth adding because repeated HYSYS automation failures can be caused by platform prerequisites rather than bad prompt logic or bad COM code. The official platform support page and V15 Engineering PDF give the project a more defensible way to separate Aspen HYSYS runtime availability, supported Windows/Office/Python context, COM registration, Engineering Suite product family boundaries, and external commercial product prerequisites.

They do not change the core project boundary. AI-HYSYS-Skill still focuses on existing runnable HYSYS cases, controlled parameter takeover, validation, and reporting. Platform specifications do not prove that HYSYS is installed locally, do not validate a case, and do not create evidence for reliable from-scratch model generation.

## Lower-value findings

- Secondary articles repeating existing Emerson / Aramco or AspenTech AVA material were not added.
- Generic AI/process-industry articles were ignored because they do not improve HYSYS control, readiness, or boundary decisions.
- GitHub searches did not produce a new license-clear, high-confidence HYSYS COM/Python case that improves the current CASE baseline.

## Project updates made

- Added official platform support HTML and V15 Engineering PDF to `CASE/official`.
- Updated `CASE/source-index.md`.
- Updated `CASE/notes/hysys-source-digest.md`.
- Updated `README.md` official references.
- Updated `SKILL.md` and `references/authority-and-path-selection.md` so readiness/version tasks distinguish platform prerequisites from skill logic.

## Safety notes

- No proprietary case files were added.
- No `.hsc`, `.hscz`, installer, executable, or plant data files were added.
- The downloaded V15 Engineering specification is a public official PDF under 1 MB.

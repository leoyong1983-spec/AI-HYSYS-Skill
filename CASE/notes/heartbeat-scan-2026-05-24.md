# Heartbeat scan 2026-05-24

Automation ID: `ai-hysys-daily-scan`

Worktree used: `D:\SKILL\AI-HYSYS-Skill-heartbeat-main`

## Search focus

Searched for latest credible sources around Aspen HYSYS automation, COM/Python/spreadsheet/workbook control, public examples, LLM agents for process simulation, HYSYS digital twins, hybrid AI, and HYSYS sensitivity/optimization workflows.

## New valuable source

### Eksergi CCS-EOR HYSYS V14 + Python automation paper

- Article page: https://jurnal.upnyk.ac.id/index.php/eksergi/article/view/16590
- DOI: https://doi.org/10.31315/eksergi.v23i2.16590
- Local article snapshot: [../research/hysys-ccs-eor-python-automation-eksergi-2026.html](../research/hysys-ccs-eor-python-automation-eksergi-2026.html)
- Local PDF: [../research/hysys-ccs-eor-python-automation-eksergi-2026.pdf](../research/hysys-ccs-eor-python-automation-eksergi-2026.pdf)
- PDF SHA256: `70873484f354e9fa60a5e648ad60b530e46eed9919564d3cefae27956e9c709b`
- HTML SHA256: `c329dd1f6f50ddd269d016004071bf5f3ddfe44c465ced71367e26c47e58a19e`
- Quality: B+
- Category: peer-reviewed HYSYS/Python automation and sensitivity evidence

## Value judgment

This source is worth adding because it directly documents Aspen HYSYS V14 automated with Python for a full-factorial techno-economic sensitivity workflow. The article metadata states that four parameters were varied to generate 162 CCS-EOR scenarios. That is highly aligned with AI-HYSYS-Skill's existing-case parameter takeover, batch scenario execution, KPI readback, validation, and reporting boundary.

It does not support from-scratch HYSYS model generation or production closed-loop control. It strengthens the rule that batch HYSYS automation must define a scenario matrix, variable schema, solver policy, failure classification, economic/KPI outputs, and human review path before running large scenario sets.

## Lower-value findings

- Generic HYSYS V15 blog material was not added because official V15 and platform-support sources are already indexed.
- Commercial digital-twin/AI integration marketing pages were not added because the current CASE already has stronger AspenTech and Emerson/AspenTech official evidence.
- GitHub and wrapper-oriented searches did not produce a new license-clear, runtime-verified HYSYS case or wrapper that should replace the repository's direct COM and spreadsheet/workbook guidance.

## Project updates made

- Added Eksergi article snapshot and PDF under `CASE/research`.
- Updated `CASE/source-index.md`.
- Updated `CASE/notes/hysys-source-digest.md`.
- Updated `README.md`.
- Updated `references/control-lane-decision-matrix.md` so full-factorial, DOE, optimizer, and batch scenario runs require explicit scenario matrices, KPI schemas, failure classes, and rerun rules.
- Included previously validated direct-COM wrapper improvements that learn from `aspen_pysys` design without copying GPL code: per-session object caches, COM readback normalization, and empty-value handling.

## Safety notes

- No proprietary case files were added.
- No `.hsc`, `.hscz`, installer, executable, wheel, source distribution, or raw plant data file was added.
- The new PDF is a public journal PDF under 1 MB.

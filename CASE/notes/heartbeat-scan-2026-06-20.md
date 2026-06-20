# Heartbeat Scan - 2026-06-20

## Search Scope

Searched for recent credible papers, official pages, technical posts, and public examples about AI controlling Aspen HYSYS, HYSYS automation via COM/Python/spreadsheets/workbooks, LLM agents for process simulation, and HYSYS digital twin or hybrid AI workflows.

## Valuable Findings

### Aspen HYSYS Digital Twins course EAO026

- Source: https://esupport.aspentech.com/T_course?id=a3pUn000002QjRlIAK
- Local HTML snapshot: `CASE/official/aspen-hysys-digital-twins-course-eao026-2026.html`
- SHA256: `FE2216EA7F6917C00B6D476D4E06CAA6FCD0913A674C69770FD91217E4A1BBB7`
- Grade: **A official HYSYS digital twin / Aspen OnLine workflow evidence**

This course is valuable because it explicitly frames digital twin work as integration of existing Aspen HYSYS process simulation models with real-time plant data. Its agenda covers Aspen OnLine, input/output tag configuration, scheduled model execution, and case history replay. That directly strengthens the project rule that online/digital-twin work needs model provenance, tag schemas, schedules, case history, and human acceptance rather than generic "AI control" claims.

### BPCL Aspen HYSYS-based ARU real-time digital twin case

- Source: https://solutions.aspentech.com/en/resources/case-studies/indian-refinery-reduces-energy-consumption-using-real-time-digital-twin
- Local HTML snapshot: `CASE/official/aspen-hysys-bpcl-aru-real-time-digital-twin-2026.html`
- Local PDF: `CASE/official/aspen-hysys-bpcl-aru-real-time-digital-twin-2023.pdf`
- PDF SHA256: `28D44C15DE7F4D1A8C8597A3566FD06EF690730E57AB1A83783BBF554F2E9F39`
- Grade: **A official HYSYS online digital twin + DMC3/APC boundary evidence**

This case is valuable because AspenTech describes a BPCL amine regeneration unit online digital twin based on Aspen HYSYS and supporting an Aspen DMC3 APC system. It strengthens the boundary that AI-HYSYS-Skill may prepare HYSYS baselines, KPI/tag schemas, validation records, and audit packages, but must not claim to replace Aspen OnLine, DMC3, APC, DCS, or production closed-loop authority.

### DanielVazVaz/PySIS

- Source: https://github.com/DanielVazVaz/PySIS
- Local README snapshot: `CASE/community/pysis-danielvazvaz-readme-2026-06-20.md`
- Local metadata snapshot: `CASE/community/pysis-danielvazvaz-github-metadata-2026-06-20.json`
- Local setup snapshot: `CASE/community/pysis-danielvazvaz-setup-2026-06-20.py`
- Grade: **B-/C+ direct community wrapper candidate**

PySIS is useful to track because it is a public Python abstraction layer over the Aspen HYSYS COM interface and claims checked use with HYSYS V11, V12, and V14. It is not adopted as a default dependency because GitHub license detection is absent, the package is marked pre-alpha in `setup.py`, and no local HYSYS runtime validation was performed.

## Adopted Project Change

- Updated `CASE/source-index.md` with official digital-twin evidence and the PySIS candidate.
- Updated `references/digital-twin-boundary.md` with Aspen OnLine tag/schedule/case-history and BPCL DMC3/APC boundary rules.
- Updated `SKILL.md` to require tag schema, schedule, case history, external APC/DCS boundaries, and human acceptance for online HYSYS digital twin tasks.
- Updated `README.md` references.

## Not Adopted

- PySIS was not installed or vendored.
- No dependency, COM wrapper, MCP server, or runtime script was added.
- No claim was added that AI-HYSYS-Skill can publish online models, replace Aspen OnLine/DMC3/APC/DCS, or reliably generate production HYSYS models from scratch.

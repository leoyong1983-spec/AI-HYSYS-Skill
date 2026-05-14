# CASE Heartbeat 2026-05-14 1607Z

## 1. Run Time

- Trigger time (UTC): 2026-05-14T16:07:09.805Z
- Local repository: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-14-heartbeat-1607Z
- Model execution status: not_run for all entries. No Aspen HYSYS case was opened, executed, or solved.

## 2. Searched Mine Areas

- GitHub-first search: public repositories and code-style queries for Aspen HYSYS, .hsc, .hscz, HYSYS XML, README, simulation files, optimization, and validation terms.
- Scientific data repositories: Zenodo records previously known to contain HYSYS files were rechecked for duplicate control.
- This heartbeat did not use login-gated, paid, customer-support, institutional, or private training resources.

## 3. Keywords Used

- `extension:hsc Aspen HYSYS`
- `extension:hscz Aspen HYSYS`
- `extension:xml "HYSYS XML Cases"`
- `"Aspen HYSYS" ".hsc"`
- `"Aspen HYSYS" ".hscz"`
- `"Aspen HYSYS" README`
- `"Aspen HYSYS" "simulation files"`
- `"Aspen HYSYS" "Excel validation"`
- `"Python-COM" HYSYS`
- `"Aspen HYSYS" Zenodo .hsc`
- `"HYSYS simulation" "hydrogen"`

## 4. Downloaded Case List

No new high-quality, non-duplicate Aspen HYSYS case file was downloaded in this heartbeat.

The run saved metadata artifacts only:

- GitHub candidate repository metadata and tree/readme probes.
- Zenodo record metadata for duplicate or manual-follow-up candidates.

## 5. Candidate And Duplicate Findings

| Title | Source page | Download URL | Local path | Reason | Quality | License / public access | Recommended use | Dedupe basis | Residual risk |
|---|---|---|---|---|---|---|---|---|---|
| GitHub candidate: ved10544-spec/Ved10544 | https://github.com/ved10544-spec/Ved10544 | Not downloaded | artifacts/github-ved10544-spec__Ved10544-* | Repository description references Aspen Hysys, but no model file or license was found. | D | Public metadata only; no explicit license. | Watchlist only. | source_page, title, metadata artifact SHA256. | Repository may change later. |
| GitHub candidate: shri2901/AspenHYSYS | https://github.com/shri2901/AspenHYSYS | Not downloaded | artifacts/github-shri2901__AspenHYSYS-* | Repository name matches HYSYS, but tree inspection found no model files. | D | Public metadata only; no explicit license. | Watchlist only. | source_page, title, metadata artifact SHA256. | Repository may change later. |
| GitHub candidate: miladmolaee/AspenHysys | https://github.com/miladmolaee/AspenHysys | Not downloaded | artifacts/github-miladmolaee__AspenHysys-* | Minimal README metadata only; no HYSYS model file. | D | Public metadata only; no explicit license. | Not suitable as benchmark. | source_page, title, metadata artifact SHA256. | Repository may change later. |
| GitHub candidate: abdulhafiz891/Cryogenic-Distillation-for-N2-Rejection | https://github.com/abdulhafiz891/Cryogenic-Distillation-for-N2-Rejection | Not downloaded | artifacts/github-abdulhafiz891__Cryogenic-Distillation-for-N2-Rejection-* | Relevant N2 rejection topic but no .hsc/.hscz/XML/.compound file. | D | Public metadata only; no explicit license. | Topic lead if author publishes model. | source_page, title, metadata artifact SHA256. | README alone is insufficient for archive. |
| GitHub candidate: abdulhafiz891/Optimization-in-Aspen-Hysys | https://github.com/abdulhafiz891/Optimization-in-Aspen-Hysys | Not downloaded | artifacts/github-abdulhafiz891__Optimization-in-Aspen-Hysys-* | Optimization wording, but no model file or license. | D | Public metadata only; no explicit license. | Topic lead only. | source_page, title, metadata artifact SHA256. | README alone is insufficient for archive. |
| Duplicate Zenodo: Aspen HYSYS model for the Tennessee Eastman process | https://zenodo.org/records/10966344 | Not downloaded this run | artifacts/zenodo-10966344-record.json | Already archived in CASE/2026-05-14-heartbeat-1007Z. | D | Zenodo metadata indicates CC-BY-NC-ND-4.0. | Use existing archive for TEP control/optimization smoke tests. | source_page, DOI, filename TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC. | Duplicate only; no new asset. |
| Duplicate Zenodo: Onboard carbon capture for circular marine fuels | https://zenodo.org/records/14882867 | Not downloaded this run | artifacts/zenodo-14882867-record.json | Already archived in CASE/2026-05-11-heartbeat-0026Z. | D | Zenodo metadata indicates CC-BY-4.0. | Use existing archive for onboard carbon capture and methanol/LNG cases. | source_page, DOI, known HSC filenames. | Duplicate only; no new asset. |
| Duplicate Zenodo: Modular Oxy-Combustion and Carbon Capture | https://zenodo.org/records/18806107 | Not downloaded this run | artifacts/zenodo-18806107-record.json | Already archived in CASE/2026-05-11-heartbeat-0222Z. | D | Zenodo metadata indicates CC-BY-4.0. | Use existing archive for OCC/ASU/CCS comparison. | source_page, DOI, known HSC filename. | Duplicate only; no new asset. |
| Zenodo candidate: Hydrogen Co-Firing in Gas Turbines | https://zenodo.org/records/19469917 | Not downloaded | artifacts/zenodo-19469917-record.json | Public record points to `Upload data.rar`, but payload was not safely inspected in this run. | D | Zenodo metadata indicates CC-BY-4.0. | Manual follow-up for hydrogen co-firing if safe extraction confirms HYSYS model files. | source_page, DOI, archive filename. | RAR may contain unsupported or unsafe content; needs isolated inspection. |

## 6. Structured Source File

See `sources.json` in this folder for SHA256 values and machine-readable metadata.

## 7. Follow-Up Recommendations

- Add a safe archive-inspection helper that can list `.rar` contents without executing payloads, then revisit Zenodo 19469917.
- Continue GitHub-first search, but prioritize repository tree queries that explicitly return `.hsc`, `.hscz`, `.xml`, or `.compound` paths before saving candidate metadata.
- Keep duplicate Zenodo records as no-download entries unless a record publishes a new version or additional model payload.
- Consider a small `CASE` summary index that maps DOI/source_page to existing local folders to reduce repeated duplicate triage.

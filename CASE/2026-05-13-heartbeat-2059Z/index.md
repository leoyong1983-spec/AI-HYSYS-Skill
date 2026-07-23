# HYSYS CASE Discovery Heartbeat - 2026-05-13 20:59Z

## Run Time
- Trigger UTC: 2026-05-13T20:59:50.770Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: D:\CODEX\AI-HYSYS-Skill\CASE
- Model run status: not_run for all candidates; no HYSYS model was opened or solved.

## Git Status
- Pre-run branch: main
- Pull result: git pull --ff-only origin main -> Already up to date.
- Commit policy: CASE-only changes staged and pushed after candidate metadata was written.

## Searched Mines
- GitHub repository search, primary mine for this run.
- Queries included: Aspen HYSYS, hysys license:mit, HYSYS V14 license:mit, Aspen HYSYS simulation license:mit, Aspen HYSYS case license:mit, Aspen HYSYS natural gas license:mit.
- Follow-up repository tree checks were performed for MIT and public candidate repositories.

## Downloaded Case List
No new benchmark case was downloaded this run.

Reason: all newly reviewed targets were either duplicates of existing CASE assets, lacked an explicit license, or did not contain a HYSYS model file. Per policy, unlicensed model/report files were not downloaded.

## Candidate Records
| Title | Source | Quality | Decision | Reason |
| --- | --- | --- | --- | --- |
| Mahdi-Arashian/sour-gas-sweetening-hysys | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys | D | Candidate only | Contains GTU Simulation.hsc and report, but no explicit license. |
| Jeslin-Jacob/rbf-interpolation-atmospheric-distillation | https://github.com/Jeslin-Jacob/rbf-interpolation-atmospheric-distillation | D | Candidate only | MIT repository with HYSYS-derived CSV/XLSX data, but no HYSYS model file. |
| pSantosb/Hysys-connection-Excel-Matlab-Python-Unity | https://github.com/pSantosb/Hysys-connection-Excel-Matlab-Python-Unity | D | Candidate only | Automation scripts and macro workbooks, no model file and no license. |
| snua/HYSYS-dynamic-simulation | https://github.com/snua/HYSYS-dynamic-simulation | D | Candidate only | Teaching PDFs only; no model file and no license. |
| YuniqueCore/DynPlots | https://github.com/YuniqueCore/DynPlots | D | Candidate only | MIT HYSYS dump plotting tool; no HYSYS case file. |
| naawu789/HySysID | https://github.com/naawu789/HySysID | D | Candidate only | MIT repository name collision; no Aspen HYSYS model evidence. |
| sajjad-ah/ASPEN-HYSYS | https://github.com/sajjad-ah/ASPEN-HYSYS | D | Candidate only | Automation/safety materials, no model file and no license. |

## Local Files
- Metadata artifacts: CASE/2026-05-13-heartbeat-2059Z/artifacts/
- Structured source records: CASE/2026-05-13-heartbeat-2059Z/sources.json

## Selection Rationale
The run prioritized GitHub and checked public repository metadata and trees. No newly reviewed target met the benchmark ingestion threshold of public rights plus a HYSYS model file. The only direct .hsc hit was not downloaded because the repository has no license.

## License / Public Access Notes
- MIT repositories were safe to record as metadata, but were not benchmark cases when no HYSYS model was present.
- Public repositories without a license were treated as candidate-only. Metadata was recorded; model/report files were not archived.

## Recommended Automation Use
- Use Mahdi-Arashian/sour-gas-sweetening-hysys as a manual permission-review candidate for amine sweetening tests.
- Use Jeslin-Jacob/rbf-interpolation-atmospheric-distillation as a data-only surrogate-model reference if data policy permits.
- Do not add the remaining candidates to the benchmark set unless a model file and license are identified.

## Dedupe Basis
- Existing CASE sources and filenames already include common MIT HYSYS repositories such as edgarsmdn/Aspen_HYSYS_Python, GaboTalero/HYSYS-Python-Case-Builder, shahria-sunny/Natural-Gas-Sweetening, shahria-sunny/CDU-Simulation-Optimization, 	inchofiuba/pythonHysys, and qiqiqiu/ai-hysys-autobuilder.
- This run avoided re-downloading duplicates and recorded only new metadata probes.

## Residual Risks
- GitHub repository search may miss code-search-only .hsc files because .hsc is also a Haskell extension and produces substantial noise.
- Candidate-only metadata does not prove model quality or runnability.
- No HYSYS case was loaded, executed, or solved.

## Next Suggestions
- Implement a GitHub search helper that filters .hsc by binary/content signatures and excludes Haskell source trees.
- Add a license-review queue for public but unlicensed HYSYS case repositories.
- Add a global CASE/source-index.json so future heartbeats do not repeatedly inspect already rejected candidates.

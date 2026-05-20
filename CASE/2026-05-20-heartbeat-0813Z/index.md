# Aspen HYSYS Case Discovery Heartbeat - 2026-05-20 0813Z

## Run Time

- Trigger time UTC: 2026-05-20T08:13:57.701Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-20-heartbeat-0813Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main.
- `git pull --ff-only origin main`: completed successfully; repository was already up to date.
- Working tree before CASE write: clean and synced with origin/main.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub repository search with `gh search repos`.
- GitHub tree inspection with `gh repo view` and GitHub API for selected repositories.
- Web search constrained to GitHub/GitLab/Bitbucket style targets and Aspen HYSYS file extensions.
- Existing `CASE/**/sources.json` and `CASE/**/index.md` were searched for source-page, title, filename, and model-file dedupe.

## Keywords Used

- `HYSYS pushed:>=2026-05-01`
- `Aspen HYSYS pushed:>=2026-05-01`
- `HYSYS created:>=2026-05-01`
- `hsc HYSYS`
- `site:github.com HYSYS .hsc MIT License Aspen`
- `site:gitlab.com Aspen HYSYS .hsc`
- `site:bitbucket.org Aspen HYSYS .hsc`
- `"Aspen HYSYS" ".hscz"`

## Downloaded Case List

No new HYSYS cases were downloaded. The only high-relevance `.hsc` repository found in this pass, `Mahdi-Arashian/sour-gas-sweetening-hysys`, was already recorded in prior CASE runs and still has no explicit license. Newer GitHub hits were either no-model false positives or automation-only code without a HYSYS case file.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub recent HYSYS repository sweep | https://github.com/search?q=HYSYS+pushed%3A%3E%3D2026-05-01&type=repositories | Not used | Not downloaded | Recent search was dominated by duplicates, no-license candidates, or unrelated repositories. | D | Public GitHub search only; no candidate met both model-file and archival-rights requirements. | Search-filter tuning and duplicate suppression. | Prior records in `CASE/2026-05-13-heartbeat-2059Z`, `CASE/2026-05-17-heartbeat-0709Z`, and later sweeps. | GitHub search is noisy; candidates may become usable only after license changes. |
| Mahdi-Arashian/sour-gas-sweetening-hysys | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys | Not used | Not downloaded | Repository contains `GTU Simulation.hsc`, README, and `Sour_Gas_Sweetening_Report_Mahdi_Arashian.pdf`. | D | Public GitHub repository, but no explicit license detected. Not downloaded. | Manual permission-review queue for sour-gas/DEA sweetening benchmark use. | Duplicate source_page and filename already recorded; same tree contains `GTU Simulation.hsc`. | Cannot archive or redistribute until author adds a license or grants permission. |
| JiataiLV/HYSYS_AI_Agent | https://github.com/JiataiLV/HYSYS_AI_Agent | Not used | Not downloaded | Newly created/pushed repository name matched HYSYS/AI search, but tree only contains `ai_agent.cpp`; no HYSYS model file. | D | Public GitHub repository with no explicit license and no model payload. | Exclude from CASE corpus; possible automation-code watchlist only. | New source-page candidate; filename/tree check found no `.hsc`, `.hscz`, HYSYS XML, or `.compound`. | Repository may later add model files or a license, but current state is not a benchmark case. |
| Silentx7x/HySystem | https://github.com/Silentx7x/HySystem | Not used | Not downloaded | False positive from `HYSYS` text match; repository is an employee-management Java system, not Aspen HYSYS. | D | Public GitHub repository with no explicit license; irrelevant to HYSYS cases. | Add to negative-search evidence; do not revisit unless metadata changes materially. | Tree inspection found Java/Spring files only; no HYSYS model or process-simulation content. | Name collision can keep polluting search results. |
| jjgomera/pychemqt | https://github.com/jjgomera/pychemqt | Not used | Not downloaded | GPL process-simulation package surfaced because the description says it aims to be equivalent to HYSYS; it is not an Aspen HYSYS case repository. | D | GPL-3.0 public software repository, but no Aspen HYSYS model payload. | Exclude from benchmark CASE assets; possible external simulator reference only. | Existing CASE sweeps already recorded it as a no-HYSYS-model search hit. | Useful software reference, but not suitable as an Aspen HYSYS benchmark case. |

## Source Pages Checked

- https://github.com/search?q=HYSYS+pushed%3A%3E%3D2026-05-01&type=repositories
- https://github.com/search?q=Aspen+HYSYS+pushed%3A%3E%3D2026-05-01&type=repositories
- https://github.com/search?q=HYSYS+created%3A%3E%3D2026-05-01&type=repositories
- https://github.com/search?q=hsc+HYSYS&type=repositories
- https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys
- https://github.com/JiataiLV/HYSYS_AI_Agent
- https://github.com/Silentx7x/HySystem
- https://github.com/jjgomera/pychemqt
- https://github.com/jjgomera/pychemqt/blob/master/LICENSE

## License And Public Access Notes

- No login, paid access, institutional credential, customer-support portal, or private source was used.
- Public GitHub repositories with no explicit license were not downloaded.
- `Mahdi-Arashian/sour-gas-sweetening-hysys` remains a strong technical candidate, but its HYSYS model and PDF report were not archived because the repository has no license.
- `JiataiLV/HYSYS_AI_Agent` and `Silentx7x/HySystem` had no qualifying HYSYS model payload.
- `jjgomera/pychemqt` is licensed software but not an Aspen HYSYS model case.

## Recommended Automation Uses

- Keep `Mahdi-Arashian/sour-gas-sweetening-hysys` in a manual permission-review queue for acid-gas/DEA sweetening.
- Add `JiataiLV/HYSYS_AI_Agent` to an automation-code watchlist only if it later adds HYSYS COM/API context and a license.
- Treat `Silentx7x/HySystem` and `jjgomera/pychemqt` as negative-search examples for the GitHub crawler.
- Continue prioritizing licensed repositories with visible `.hsc` or `.hscz` files plus README/report/validation data.

## Residual Risks

- GitHub search remains high-noise and duplicate-heavy.
- A no-license repository can become usable later if maintainers add a license; this run did not detect such a change for previously known high-value candidates.
- Repository descriptions can mention HYSYS while containing no Aspen HYSYS case file.

## Next Suggestions

- Maintain a durable denylist/negative list for repeated false positives such as generic software named `HySystem` and HYSYS-alternative simulators.
- Maintain a manual-permission queue for no-license `.hsc` repositories, with last-checked timestamp and visible model filenames.
- Search next for newly licensed `.hsc` payloads via GitHub code search patterns such as `extension:hsc license:mit HYSYS`, `filename:LICENSE HYSYS .hsc`, and `path:**/*.hsc Aspen`.

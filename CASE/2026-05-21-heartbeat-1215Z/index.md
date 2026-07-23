# Aspen HYSYS Case Discovery Heartbeat - 2026-05-21 1215Z

## Run Time

- Trigger time UTC: 2026-05-21T12:15:58.926Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-21-heartbeat-1215Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main.
- `git pull --ff-only origin main`: completed successfully; repository was already up to date.
- Working tree before CASE write: clean and synced with origin/main.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub code search with `gh search code` for `.hsc` and `.hscz`.
- GitHub repository search with `gh search repos` for Aspen HYSYS, `.hsc`, simulation, and recent pushed repositories.
- GitHub API tree inspection for recent or model-bearing candidates.
- Zenodo and web search checks for already-known open HYSYS dataset records.
- Existing `CASE/**/sources.json`, `CASE/**/index.md`, and `CASE/source-index.md` searched for source-page/title/file dedupe.

## Keywords Used

- `HYSYS filename:*.hsc`
- `Aspen filename:*.hsc`
- `HYSYS filename:*.hscz`
- `Aspen HYSYS`
- `HYSYS .hsc`
- `Aspen HYSYS simulation`
- `HYSYS pushed:>=2026-05-01`
- `site:github.com Aspen HYSYS .hsc`
- `site:zenodo.org Aspen HYSYS .hsc`

## Downloaded Case List

No new HYSYS cases were downloaded. Direct GitHub code search returned no `.hsc` or `.hscz` hits. Repository search found recent or model-bearing candidates, but the viable model sources were already archived or blocked by unclear/restrictive licensing. Automation-only and PDF-only repositories were not downloaded because they do not meet the HYSYS model-file requirement.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub search sweep for HYSYS `.hsc/.hscz` | https://github.com/search?q=HYSYS+filename%3A*.hsc&type=code | Not used | Not downloaded | Direct code search returned no qualifying `.hsc` or `.hscz` model-file hits; repository search still found candidates through README/metadata. | D | Public GitHub search only; no qualifying payload downloaded. | Use as negative evidence for code-search coverage and continue tree inspection. | No source_page/file/SHA256 suitable for new archive. | GitHub code search can miss binary files and repositories where only metadata mentions HYSYS. |
| Mahdi-Arashian/sour-gas-sweetening-hysys | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys | Not used | Not downloaded | Public repository contains `GTU Simulation.hsc`, report PDF, and README for DEA sour-gas sweetening, but no repository license is declared. It has already been recorded as a no-license candidate. | D | Public GitHub repository, but no explicit license; archival/download rights are unclear. | Manual permission queue only; do not include as redistributable benchmark unless license/permission is clarified. | Existing records: CASE/2026-05-11-heartbeat-0854Z, CASE/2026-05-13-heartbeat-2059Z, CASE/2026-05-14-heartbeat-2207Z. File tree includes `GTU Simulation.hsc` SHA `d0ea686ea5e94902296d666ee1940e68229f6396`. | The model may be technically useful, but redistribution risk remains unresolved. |
| iraola/tennessee-eastman-hysys | https://github.com/iraola/tennessee-eastman-hysys | Not used | Not downloaded | Public repository contains `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC` and a CC-BY-NC-ND-4.0 license. Equivalent/related Zenodo record was already archived. | D | Public GitHub repository under CC-BY-NC-ND-4.0; derivative and commercial restrictions require caution. No duplicate download made. | Use existing archived Zenodo copy for Tennessee Eastman hybrid-monitoring/fault-detection work. | Existing records: CASE/2026-05-11-heartbeat-1648Z and CASE/2026-05-14-heartbeat-1007Z; Zenodo record 10966344 already archived with SHA256 evidence. | License restrictions and HYSYS version uncertainty remain; model was not opened in this run. |
| sajjad-ah/ASPEN-HYSYS | https://github.com/sajjad-ah/ASPEN-HYSYS | Not used | Not downloaded | Recent public repository metadata mentions ASPEN-HYSYS automation, but inspected tree showed `SAFETY INSTRUMENTED SYSTEMS.pdf` only among relevant file types and no HYSYS model file. | D | Public GitHub repository with no explicit license and no qualifying model payload. | Exclude from model corpus; at most a manual literature/reference candidate. | Existing probe evidence appears in CASE/2026-05-11-heartbeat-1815Z; current tree inspection found no `.hsc/.hscz/HYSYS XML/.compound` file. | Future pushes could add a model, but current public tree is not suitable for CASE archival. |

## Source Pages Checked

- https://github.com/search?q=HYSYS+filename%3A*.hsc&type=code
- https://github.com/search?q=Aspen+filename%3A*.hsc&type=code
- https://github.com/search?q=HYSYS+filename%3A*.hscz&type=code
- https://github.com/search?q=Aspen+HYSYS&type=repositories
- https://github.com/search?q=HYSYS+.hsc&type=repositories
- https://github.com/search?q=Aspen+HYSYS+simulation&type=repositories
- https://github.com/search?q=HYSYS+pushed%3A%3E%3D2026-05-01&type=repositories
- https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys
- https://github.com/iraola/tennessee-eastman-hysys
- https://github.com/sajjad-ah/ASPEN-HYSYS
- https://zenodo.org/records/10966344

## License And Public Access Notes

- No login, paid access, institutional credential, customer-support portal, or private source was used.
- Public repositories without explicit licenses were not downloaded.
- CC-BY-NC-ND-4.0 material was not duplicated because an existing archive record already covers the Zenodo source and restrictions remain.
- Automation-only or PDF-only repositories were excluded from the model corpus.
- No executable, macro, script, HYSYS model, PDF, workbook, notebook, or unknown binary was run.

## Recommended Automation Uses

- Keep `Mahdi-Arashian/sour-gas-sweetening-hysys` in a manual-permission queue, not in redistributable benchmark assets.
- Use the existing Tennessee Eastman Zenodo archive for model-aware metadata workflows, but preserve license restriction notes.
- Treat `sajjad-ah/ASPEN-HYSYS` as a non-model candidate unless a future tree change adds a HYSYS payload.
- Continue preferring MIT/CC-BY/DOI-backed sources that expose both model payload and validation/report data.

## Residual Risks

- GitHub code search may miss binary HYSYS files.
- No-license repositories can disappear or change terms without notice.
- CC-BY-NC-ND restrictions limit reuse and derivative handling.
- Existing archived HYSYS files were not opened or solver-validated during this run.

## Next Suggestions

- Add a low-priority watchlist for no-license but model-bearing repositories and revisit only when a license appears.
- Prioritize repository tree inspection over code search for `.hsc` assets.
- Recheck Zenodo for new HYSYS records with explicit DOI/license metadata rather than relying on GitHub-only discovery.

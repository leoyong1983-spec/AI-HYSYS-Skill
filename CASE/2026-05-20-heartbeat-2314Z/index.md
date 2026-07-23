# Aspen HYSYS Case Discovery Heartbeat - 2026-05-20 2314Z

## Run Time

- Trigger time UTC: 2026-05-20T23:14:18.643Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-20-heartbeat-2314Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main.
- `git pull --ff-only origin main`: completed successfully; repository was already up to date.
- Working tree before CASE write: clean and synced with origin/main.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub code search with `gh search code` for HYSYS case extensions.
- GitHub repository search with `gh search repos` for new/recent HYSYS repositories.
- GitHub API tree inspection for selected duplicate candidates.
- Web search constrained to GitHub pages mentioning Aspen HYSYS and `.hsc/.hscz`.
- Existing `CASE/**/sources.json` and `CASE/**/index.md` searched for source-page/title/file dedupe.

## Keywords Used

- `extension:hsc HYSYS`
- `extension:hscz HYSYS`
- `extension:compound HYSYS`
- `Aspen HYSYS extension:xml`
- `Aspen HYSYS pushed:>=2026-05-20`
- `HYSYS pushed:>=2026-05-20`
- `HYSYS case file`
- `Aspen HYSYS simulation file`
- `site:github.com "Aspen HYSYS" ".hsc" "LICENSE"`
- `site:github.com "Aspen HYSYS" ".hscz"`

## Downloaded Case List

No new HYSYS cases were downloaded. GitHub code search returned no `.hsc`, `.hscz`, or `.compound` case-file hits. The XML search returned ordinary web/tag/article XML files, not HYSYS XML cases. Recent repository search returned only this repository for post-2026-05-20 HYSYS updates. The remaining candidate repositories were duplicates already recorded in prior CASE runs and lacked either a license or a HYSYS model payload.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub code search for HYSYS case extensions | https://github.com/search?q=extension%3Ahsc+HYSYS&type=code | Not used | Not downloaded | Direct code search for `.hsc`, `.hscz`, and `.compound` returned no downloadable HYSYS model candidates. XML hits were ordinary web/data XML, not HYSYS XML cases. | D | Public GitHub search only; no qualifying case payload found. | Search-filter tuning and evidence that current code search is sparse for binary HYSYS formats. | No source_page or filename suitable for CASE archival was found. | GitHub code search may omit some binary or large files; repo-level searches remain necessary. |
| leoyong1983-spec/AI-HYSYS-Skill self-hit | https://github.com/leoyong1983-spec/AI-HYSYS-Skill | Not used | Not downloaded | Recent HYSYS repository search returned only the current archive repository for `pushed:>=2026-05-20`; self-hit is not an external case source. | D | MIT repository, but it is the target archive itself, not an external source. | Exclude from discovery targets; useful only as origin/main state check. | Exact source_page is this repository and already present throughout CASE history. | Self-hits can hide external targets if recent search windows are too narrow. |
| perrywzm/hysysopt | https://github.com/perrywzm/hysysopt | Not used | Not downloaded | Repository description references optimizing HYSYS case files, but inspected tree contains Python/Jupyter code and screenshots only; no `.hsc/.hscz/HYSYS XML/.compound` payload. | D | Public GitHub repository with no explicit license. Not downloaded. | Manual automation-code watchlist only; not a benchmark CASE asset. | Duplicate source_page already recorded in prior CASE runs. | May require a private/local HYSYS case not present in the public repo. |
| GaboTalero/HYSYS-Python-Case-Builder | https://github.com/GaboTalero/HYSYS-Python-Case-Builder | Not used | Not downloaded | MIT-licensed HYSYS COM automation scripts, but inspected tree contains Python scripts and no HYSYS model payload. | D | Public MIT repository; no model file to archive as a CASE. | Reference automation-code candidate only; keep separate from model benchmark corpus. | Duplicate source_page and tree evidence already recorded in prior CASE runs. | Useful for automation patterns but not a simulation case benchmark. |

## Source Pages Checked

- https://github.com/search?q=extension%3Ahsc+HYSYS&type=code
- https://github.com/search?q=extension%3Ahscz+HYSYS&type=code
- https://github.com/search?q=extension%3Acompound+HYSYS&type=code
- https://github.com/search?q=Aspen+HYSYS+extension%3Axml&type=code
- https://github.com/search?q=Aspen+HYSYS+pushed%3A%3E%3D2026-05-20&type=repositories
- https://github.com/search?q=HYSYS+pushed%3A%3E%3D2026-05-20&type=repositories
- https://github.com/search?q=HYSYS+case+file&type=repositories
- https://github.com/search?q=Aspen+HYSYS+simulation+file&type=repositories
- https://github.com/leoyong1983-spec/AI-HYSYS-Skill
- https://github.com/perrywzm/hysysopt
- https://github.com/GaboTalero/HYSYS-Python-Case-Builder
- https://github.com/prasang-gupta/prasang-gupta.github.io
- https://github.com/petermr/CEVOpen
- https://github.com/JavierBerenguer/Trabajo-Final-de-Grado

## License And Public Access Notes

- No login, paid access, institutional credential, customer-support portal, or private source was used.
- Public GitHub repositories with no explicit license were not downloaded.
- Licensed automation-only repositories were not duplicated because they lack HYSYS model files.
- Ordinary XML/blog/article/data files were not treated as HYSYS XML cases.
- No executable, macro, script, or unknown binary was run.

## Recommended Automation Uses

- Treat `perrywzm/hysysopt` and `GaboTalero/HYSYS-Python-Case-Builder` as automation references only, not CASE benchmark assets.
- Keep searching for repositories that expose a model payload and license together; code-search alone is not sufficient for HYSYS binary formats.
- Add a stronger crawler filter for self-hits and ordinary XML tag/feed/article files.

## Residual Risks

- GitHub code search may miss binary case files or files blocked from indexing.
- Some repositories may rely on local/private HYSYS models while publishing only automation code.
- Recent-date repository searches can return mostly the archive repository itself.

## Next Suggestions

- Expand beyond exact code search into GitHub repository tree inspection for newly updated repos with `Aspen HYSYS`, `case file`, `simulation file`, and process-topic terms.
- Keep a negative list for ordinary XML repositories and self-hits.
- Recheck high-value no-license repositories only when GitHub metadata indicates license or file changes.

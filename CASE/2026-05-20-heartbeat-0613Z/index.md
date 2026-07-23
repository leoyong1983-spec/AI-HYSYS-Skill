# Aspen HYSYS Case Discovery Heartbeat - 2026-05-20 0613Z

## Run Time

- Trigger time UTC: 2026-05-20T06:13:54.479Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-20-heartbeat-0613Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main.
- `git pull --ff-only origin main`: completed successfully; repository was already up to date except for the prior local CASE commit.
- Prior local commit `4f1c8df` from the 0313Z heartbeat was pushed successfully before this run continued.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub repository search with `gh search repos`.
- GitHub tree inspection with `gh repo view` and GitHub API for selected candidates.
- Existing `CASE/**/sources.json` and `CASE/**/index.md` were searched for source-page/title/file dedupe.

## Keywords Used

- `Aspen HYSYS`
- `HYSYS automation`
- `HYSYS CO2`
- `Aspen HYSYS Python`
- `HYSYS Excel`
- `extension:hsc`
- `extension:hscz`
- `HYSYS simulation`
- `HYSYS case`
- `HYSYS README`

## Downloaded Case List

No new HYSYS cases were downloaded. The strongest GitHub hits were already archived or already recorded as no-license/manual-review candidates. Newly refreshed repositories with visible `.hsc` files still lacked explicit licenses, so downloading would violate the archival rules.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub licensed duplicate/data-only sweep | https://github.com/search?q=Aspen+HYSYS&type=repositories | Not used | Not downloaded | MIT or public results such as `edgarsmdn/Aspen_HYSYS_Python`, `GaboTalero/HYSYS-Python-Case-Builder`, `Galigeigei-Z/HDA-Surrogate-Optimization`, `shahria-sunny/Natural-Gas-Sweetening`, and `shahria-sunny/CDU-Simulation-Optimization` were rechecked. | D | Licensed entries were already archived or had no qualifying model payload in the inspected tree. | Duplicate avoidance; use existing archived copies where applicable. | Existing source_page and filename matches in CASE records. | No new model payload added. |
| GitHub no-license `.hsc` duplicate/manual-review sweep | https://github.com/search?q=Aspen+HYSYS+.hsc&type=repositories | Not used | Not downloaded | Tree/repo checks resurfaced no-license `.hsc` candidates including `Rus-tam/hysys_observer`, `kush1706/Methanol_Synthesis_Aspen_hysys`, `CristopherCano/Projects-ASPEN-HYSYS`, `Corey-McInrue/Node-C-ASPEN-HYSYS`, `royhanikbarr/Aspen-Hysys-Simulation`, and `marcellobozzini/Python-Driving-License`. | D | Public GitHub read access, but no explicit license detected for the model payloads. | Manual permission-review queue only. | Existing CASE records already contain these source pages and/or filenames. | Cannot archive or redistribute without explicit license/permission. |
| GitHub automation/no-model sweep | https://github.com/search?q=HYSYS+automation&type=repositories | Not used | Not downloaded | Rechecked automation/interface repositories including `DanielVazVaz/PySIS`, `pSantosb/Hysys-connection-Excel-Matlab-Python-Unity`, `sajjad-ah/ASPEN-HYSYS`, `Avest-AI/MemCal`, `GerasimovRM/AspenHysysReader`, and `SuradechKKPB/AutomatedHYSYS`. | D | Public GitHub read access; most have no explicit license and/or no HYSYS model file. `Avest-AI/MemCal` also exposes binary DLL/EDF files, which were not downloaded or run. | Search-filter tuning and manual-review backlog only. | Existing CASE records already list most of these repositories as candidates; tree checks found no new licensed `.hsc/.hscz` payload. | Automation code and binaries are not benchmark cases; unknown binaries must not be executed. |

## Source Pages Checked

- https://github.com/edgarsmdn/Aspen_HYSYS_Python
- https://github.com/GaboTalero/HYSYS-Python-Case-Builder
- https://github.com/Galigeigei-Z/HDA-Surrogate-Optimization
- https://github.com/shahria-sunny/Natural-Gas-Sweetening
- https://github.com/shahria-sunny/CDU-Simulation-Optimization
- https://github.com/Rus-tam/hysys_observer
- https://github.com/kush1706/Methanol_Synthesis_Aspen_hysys
- https://github.com/CristopherCano/Projects-ASPEN-HYSYS
- https://github.com/Corey-McInrue/Node-C-ASPEN-HYSYS
- https://github.com/royhanikbarr/Aspen-Hysys-Simulation
- https://github.com/marcellobozzini/Python-Driving-License
- https://github.com/DanielVazVaz/PySIS
- https://github.com/pSantosb/Hysys-connection-Excel-Matlab-Python-Unity
- https://github.com/sajjad-ah/ASPEN-HYSYS
- https://github.com/Avest-AI/MemCal
- https://github.com/GerasimovRM/AspenHysysReader
- https://github.com/SuradechKKPB/AutomatedHYSYS

## License And Public Access Notes

- No login, paid access, institutional credentials, customer-support portal, or private source was used.
- Public GitHub repositories with no explicit license were not downloaded.
- Public GitHub repositories with binaries and no license were not downloaded or run.
- Licensed repositories already present in CASE were not duplicated.

## Recommended Automation Uses

- Use existing archived licensed cases rather than re-downloading duplicates.
- Keep no-license `.hsc` repositories in the manual permission-review queue.
- Keep automation-only repositories separate from the CASE benchmark corpus unless they include a licensed model payload.

## Residual Risks

- Some no-license repositories may become usable if maintainers later add a license; this run did not detect such a change.
- GitHub search remains duplicate-heavy; direct model discovery would improve if a durable denylist/manual-review index is added.
- Binary extension repositories may be relevant to HYSYS workflows, but they are outside the safe automatic download scope.

## Next Suggestions

- Add a generated no-license/manual-review index for repeated GitHub `.hsc` candidates.
- Continue checking for license changes on `Rus-tam/hysys_observer`, `kush1706/Methanol_Synthesis_Aspen_hysys`, and `CristopherCano/Projects-ASPEN-HYSYS`.
- Prioritize new MIT/Apache/BSD repositories with visible `.hsc` or `.hscz` files and README/validation data.

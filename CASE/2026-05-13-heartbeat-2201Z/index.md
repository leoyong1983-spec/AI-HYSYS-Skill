# HYSYS CASE Discovery Heartbeat - 2026-05-13 22:01Z

## Run Time
- Trigger UTC: 2026-05-13T22:01:18.010Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: D:\CODEX\AI-HYSYS-Skill\CASE
- Model run status: not_run for all candidates.

## Git Status
- Branch: main
- Pull result: git pull --ff-only origin main -> Already up to date.

## Searched Mines
- Primary mine: GitHub repository search and GitHub tree inspection.
- Queries included: Aspen-HYSYS, Aspen HYSYS simulation, HYSYS simulation license:mit, HYSYS Aspen file, Hysys simulation file, Aspen Hysys project, Aspen HYSYS dynamics, plus topic probes for Apache/GPL licensed HYSYS repositories.

## Downloaded Case List
No new benchmark case was downloaded this run.

Reason: newly reviewed repositories with HYSYS model files did not provide explicit licenses, and licensed repositories did not contain HYSYS model files. Per policy, unlicensed model files were not archived.

## Candidate Records
| Title | Source | Quality | Decision | Reason |
| --- | --- | --- | --- | --- |
| Corey-McInrue/Node-C-ASPEN-HYSYS | https://github.com/Corey-McInrue/Node-C-ASPEN-HYSYS | D | Candidate only | Contains NODECFINAL.hsc, but no license. |
| JeePeiQi0101/Aspen.HYSYS | https://github.com/JeePeiQi0101/Aspen.HYSYS | D | Candidate only | Contains three HYSYS XML-named simulation files and a report, but no license. |
| marcellobozzini/Python-Driving-License | https://github.com/marcellobozzini/Python-Driving-License | D | Candidate only | Contains Separazione_reattori.hsc and a notebook, but no license. |
| Amansurana2005/Oil-Well-Simulation-for-Gas-oil-separation-Using-Conceptual-Design-Builder-In-Aspen-HYSYS-Simulation | https://github.com/Amansurana2005/Oil-Well-Simulation-for-Gas-oil-separation-Using-Conceptual-Design-Builder-In-Aspen-HYSYS-Simulation | D | Candidate only | README-only tree; no model file found. |
| DanielVazVaz/PySIS | https://github.com/DanielVazVaz/PySIS | D | Candidate only | HYSYS Python abstraction layer; no model file and no license. |
| Avest-AI/MemCal | https://github.com/Avest-AI/MemCal | D | Candidate only | HYSYS membrane extension context; no model file and no license. |
| vminasid/Hysys-Unisis2Matlab | https://github.com/vminasid/Hysys-Unisis2Matlab | D | Candidate only | GPL automation code, no model file. |

## Local Files
- Metadata artifacts: CASE/2026-05-13-heartbeat-2201Z/artifacts/
- Structured source records: CASE/2026-05-13-heartbeat-2201Z/sources.json

## License / Public Access Notes
- Public GitHub visibility alone was not treated as permission to archive models.
- Repositories without explicit licenses were recorded as candidate-only.
- GPL code was recorded as metadata only because it contained no case model and has reuse obligations.

## Recommended Automation Use
- Corey-McInrue/Node-C-ASPEN-HYSYS, JeePeiQi0101/Aspen.HYSYS, and marcellobozzini/Python-Driving-License should enter a manual license/author-permission queue.
- DanielVazVaz/PySIS and minasid/Hysys-Unisis2Matlab may inform automation-interface design, not benchmark ingestion.

## Dedupe Basis
- Checked existing CASE sources.json source pages and download URLs before candidate recording.
- Previously archived or candidate-reviewed repositories were not re-downloaded.

## Residual Risks
- GitHub .hsc discovery remains noisy because .hsc is also used by Haskell and game script files.
- Candidate-only records do not validate model quality or runnability.
- No HYSYS model was opened, loaded, or solved.

## Next Suggestions
- Add a dedicated GitHub discovery script that filters .hsc by repository context and excludes Haskell/game-script false positives.
- Add a manual license queue for public repos with HYSYS files but no license.
- Prefer repositories with explicit MIT/Apache/BSD license and actual HYSYS model files for future downloads.

# HYSYS CASE Discovery Heartbeat - 2026-05-14 11:07Z

## Run Time
- Trigger UTC: 2026-05-14T11:07:01.384Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: D:\CODEX\AI-HYSYS-Skill\CASE
- Model run status: not_run.

## Git Status
- Branch: main
- Pull result: git pull --ff-only origin main -> Already up to date.

## Searched Mines
- GitHub repository search and tree inspection for unrecorded Aspen/HYSYS repositories.
- Zenodo API inspection for HYSYS-related records not already in CASE.
- Keywords included: Aspen HYSYS, .hsc, simulation file, case, hydrogen, refinery, and related repository names.

## Downloaded Case List
No new benchmark case was downloaded this run.

Reason: visible GitHub model files lacked explicit repository licenses; Zenodo candidates did not expose a confirmed supported HYSYS model file in safely inspectable form.

## Candidate Records
| Title | Source | Quality | Decision | Reason |
| --- | --- | --- | --- | --- |
| Paryazdan/Aspen-HYSYS-Projects | https://github.com/Paryazdan/Aspen-HYSYS-Projects | D | Candidate only | Contains .hsc and PDF but no license. |
| cityfamer/HyPy | https://github.com/cityfamer/HyPy | D | Candidate only | HYSYS Python interface package; no model file and no license. |
| GerasimovRM/AspenHysysReader | https://github.com/GerasimovRM/AspenHysysReader | D | Candidate only | Reader script and XLSX summary; no model file and no license. |
| Shreya88876/Aspen_file_shreya | https://github.com/Shreya88876/Aspen_file_shreya | D | Candidate only | Description mentions HYSYS, but tree metadata did not reveal model files. |
| sanjay-saran/dme-production-methanol | https://github.com/sanjay-saran/dme-production-methanol | D | Candidate only | README-only tree; no model file and no license. |
| Hydrogen Co-Firing in Gas Turbines | https://zenodo.org/records/19469917 | D | Candidate only | CC-BY RAR package; archive contents could not be safely listed in current environment. |
| Role of biogenic CO2 in refinery decarbonization | https://zenodo.org/records/15476366 | D | Candidate only | CC-BY record but files are .lnr/DOCX, not supported HYSYS cases. |

## Local Files
- Metadata artifacts: CASE/2026-05-14-heartbeat-1107Z/artifacts/
- Structured records: CASE/2026-05-14-heartbeat-1107Z/sources.json

## License / Public Access Notes
- Public GitHub repositories without explicit licenses were not downloaded as model artifacts.
- Zenodo CC-BY metadata was recorded. The RAR package was not committed because the environment cannot list RAR contents safely.

## Recommended Automation Use
- Put Paryazdan/Aspen-HYSYS-Projects into manual license review; it may be useful if permission is confirmed.
- Add RAR listing support to safely inspect Zenodo package candidates.
- Use interface-only repos (HyPy, AspenHysysReader) as possible automation-code references, not benchmark cases.

## Dedupe Basis
- Existing CASE/**/sources.json entries were read before this run.
- Previously recorded candidate pages were avoided where possible; repeated no-license examples were not downloaded.

## Residual Risks
- Some GitHub repositories may hide model files behind nonstandard names or empty default trees.
- RAR package contents remain unknown.
- No HYSYS model was loaded, solved, or validated.

## Next Suggestions
- Install or bundle a safe archive listing tool for .rar to classify Zenodo packages without extraction.
- Add a manual license queue for public GitHub repositories with HYSYS model files but no license.
- Build a global CASE/source-index.json to avoid repeated candidate probes.

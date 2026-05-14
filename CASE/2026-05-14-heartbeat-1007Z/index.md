# HYSYS CASE Discovery Heartbeat - 2026-05-14 10:07Z

## Run Time
- Trigger UTC: 2026-05-14T10:07:00.526Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: D:\CODEX\AI-HYSYS-Skill\CASE
- Model run status: not_run. No HYSYS model was opened or solved.

## Git Status
- Branch: main
- Pull result: git pull --ff-only origin main -> Already up to date.

## Searched Mines
- Primary: GitHub repository search and tree inspection.
- Secondary: Zenodo API search for Aspen HYSYS, .hsc, case, iles, and supplementary terms.
- GitHub candidates checked included Anikesh31/simulator_codingplatform_integration, oyhanikbarr/Aspen-Hysys-Simulation, cityfamer/HyPy, GerasimovRM/AspenHysysReader, oraclesep/Aspen, and other unrecorded Aspen/HYSYS repositories.

## Downloaded Case List
| Title | Source | Download URL | Local path | Quality |
| --- | --- | --- | --- | --- |
| Aspen HYSYS model for the Tennessee Eastman process | https://zenodo.org/records/10966344 | https://zenodo.org/api/records/10966344/files/TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC/content | CASE/2026-05-14-heartbeat-1007Z/artifacts/Zenodo_2024_Tennessee_Eastman_Iraola/TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC | B |

## Downloaded Artifacts
- TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC - SHA256 4adf908a6bf0e36d058453bcddd2cdf0b857324ff8ba5bdd0817261edab5d3b6
- ecord-10966344.json - SHA256 1a52c810794fe65957edb4075ee069b9f1a1239d037c55484a23148dd901a244

## Selection Rationale
The Zenodo record is an open model dataset with DOI 10.5281/zenodo.10966344, explicit license metadata, named creator, and a direct Aspen HYSYS .HSC model file. It is suitable as a benchmark candidate, although it lacks validation data in the record and the HYSYS version is not declared.

## Candidate Records Not Downloaded
| Title | Source | Reason |
| --- | --- | --- |
| Anikesh31/simulator_codingplatform_integration | https://github.com/Anikesh31/simulator_codingplatform_integration | Contains .hsc and automation scripts but no explicit license. |
| royhanikbarr/Aspen-Hysys-Simulation | https://github.com/royhanikbarr/Aspen-Hysys-Simulation | Contains .hsc and PDF report but no explicit license. |

## License / Public Access Notes
- Zenodo case: cc-by-nc-nd-4.0; keep original file unmodified and observe non-commercial/no-derivatives constraints.
- GitHub candidates without explicit license were metadata-only and not archived as model files.

## Recommended Automation Use
- Use the Tennessee Eastman model for future HYSYS case opening smoke tests, COM lifecycle checks, fault-detection data pipeline scaffolding, and dynamic/process monitoring workflows after manual load authorization.
- Keep GitHub no-license model repositories in a manual permission queue.

## Dedupe Basis
- Existing CASE/**/sources.json and index.md were checked for 10966344, TENNESSEE_EASTMAN_PROCESS_HYSYS, and related source URLs before download.
- No existing local match was found for the Zenodo DOI or filename.

## Residual Risks
- HYSYS version is unknown.
- CC-BY-NC-ND licensing limits reuse; do not modify or commercially redistribute.
- The model has not been loaded or solved locally.

## Next Suggestions
- Add Zenodo DOI/source IDs to a global dedupe index.
- Build a license-review queue for GitHub repositories with visible .hsc files but no license.
- Add a HYSYS-version metadata extractor that reads safe file headers without launching HYSYS.

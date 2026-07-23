# Aspen HYSYS Case Discovery Heartbeat - 2026-05-20 0213Z

## Run Time

- Trigger time UTC: 2026-05-20T02:13:47.614Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-20-heartbeat-0213Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main
- Start gate: repository confirmed on main and initial `git pull --ff-only origin main` completed with no incoming changes.
- End rule: only this run's CASE files are eligible for staging.

## Search Mines

- GitHub and GitHub code/repository search via `gh`.
- Web search targeting GitHub HYSYS `.hsc` and `.hscz` assets.
- Data repository probes: Zenodo, Figshare, and DataCite keyword searches for Aspen HYSYS cases and supplementary materials.

## Keywords Used

- `extension:hsc HYSYS`
- `extension:hsc Aspen`
- `extension:hsc "Aspen HYSYS"`
- `Aspen HYSYS .hsc`
- `HYSYS .hsc`
- `Aspen HYSYS simulation`
- `HYSYS automation`
- `HYSYS Excel VBA`
- `Aspen HYSYS supplementary material`
- `Aspen HYSYS Zenodo case`

## Downloaded Case List

No new case files were downloaded. The strongest licensed `.hsc` hit found in this sweep was already archived, and the newly observed non-duplicate GitHub projects did not expose a HYSYS model file or had no explicit license.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Duplicate strong hit: edgarsmdn/Aspen_HYSYS_Python | https://github.com/edgarsmdn/Aspen_HYSYS_Python | https://codeload.github.com/edgarsmdn/Aspen_HYSYS_Python/zip/refs/heads/main | Not downloaded this run | Public MIT repository with `Test_1.hsc`, README, and Python automation scripts. | D | MIT license, but already archived. | Use existing CASE/2026-05-11-heartbeat-1057Z copy for HYSYS-Python spreadsheet and COM smoke tests. | Existing source_page, codeload URL, filename `Test_1.hsc`, and prior archive path. | Re-downloading would duplicate existing payloads and hashes. |
| Duplicate no-license HSC leads: Zinatullin76/Python-Hysys and Facul-101/PY-HYSYS | https://github.com/Zinatullin76/Python-Hysys; https://github.com/Facul-101/PY-HYSYS | Not used | Not downloaded this run | Both expose `.hsc` files and HYSYS-Python bridge material, but no explicit license was detected. | D | Public GitHub read access; no explicit license, so archival rights remain unclear. | Manual license-review backlog only. | Already recorded in CASE/2026-05-17-heartbeat-0709Z. | Needs maintainer license clarification before downloading or redistributing. |
| atlanticbhandari07/CCS_code | https://github.com/atlanticbhandari07/CCS_code | Not used | Not downloaded this run | Recent CO2 capture HYSYS automation thesis scripts; repository tree exposes Python scripts and README only. | D | Public GitHub read access; no explicit license detected. | Possible keyword lead for future CCUS automation patterns if a model is later published. | New source_page; tree files checked: README and Python scripts only; no `.hsc`, `.hscz`, HYSYS XML, or `.compound`. | No HYSYS model and no license; not suitable for CASE archival. |
| hairizuanbinnoorazman/HYSYS-to-Excel | https://github.com/hairizuanbinnoorazman/HYSYS-to-Excel | Not used | Not downloaded this run | VBA bridge for extracting HYSYS values into Excel; README says it targets HYSYS 7.2. | D | Public GitHub read access; no explicit license detected. | Historical HYSYS 7.2 Excel automation reference only if license is clarified. | New source_page; tree files checked: README and VBA samples only; no HYSYS model. | No model file and no license; VBA should not be executed automatically. |
| italosichi/HYSYS_data_import | https://github.com/italosichi/HYSYS_data_import | Not used | Not downloaded this run | Notebook for organizing standard Aspen HYSYS reports and exergy calculations. | D | Public GitHub read access; no explicit license detected. | Possible report-postprocessing reference after license review. | New source_page; tree files checked: README and notebook only; no HYSYS model. | No model file, no license, and no validation payload. |
| fellipe-carvalho-de-oliveira/matlab_to_hysys | https://github.com/fellipe-carvalho-de-oliveira/matlab_to_hysys | Not used | Not downloaded this run | HYSYS/MATLAB unit-operation integration lead, but repository includes binaries and no case file. | D | Public GitHub read access; no explicit license detected. | Do not use without manual security and license review. | New source_page; tree files checked: README, VB project files, DLL/EXE binaries, and `teste.bk0`; no `.hsc` model. | Contains executable/binary payloads and no license; skipped by safety rules. |

## Source Pages Checked

- https://github.com/edgarsmdn/Aspen_HYSYS_Python
- https://github.com/Zinatullin76/Python-Hysys
- https://github.com/Facul-101/PY-HYSYS
- https://github.com/atlanticbhandari07/CCS_code
- https://github.com/hairizuanbinnoorazman/HYSYS-to-Excel
- https://github.com/italosichi/HYSYS_data_import
- https://github.com/fellipe-carvalho-de-oliveira/matlab_to_hysys

## License And Public Access Notes

- Only `edgarsmdn/Aspen_HYSYS_Python` had a detected MIT license, but it is already archived in CASE/2026-05-11-heartbeat-1057Z.
- `Zinatullin76/Python-Hysys` and `Facul-101/PY-HYSYS` expose HYSYS case files but still have no explicit license in the previously recorded evidence.
- The newly reviewed repositories are publicly readable but do not provide both a HYSYS model and an explicit license.
- No login, payment, institutional access, customer-support portal, or private resource was used.

## Recommended Automation Uses

- Continue using the existing archived `edgarsmdn/Aspen_HYSYS_Python` copy for lightweight Python-HYSYS spreadsheet bridge tests.
- Keep `Zinatullin76/Python-Hysys` and `Facul-101/PY-HYSYS` on the manual license-review backlog.
- Treat `atlanticbhandari07/CCS_code` as a future CCUS automation lead only if the author publishes a model and a license.
- Do not run or import code from no-license repositories or repositories containing binaries.

## Residual Risks

- GitHub code search returned no direct new `.hsc` results during this run; web search mainly resurfaced already archived licensed cases.
- Some useful HYSYS models may exist behind repository archives, releases, or supplementary ZIP files that were not downloaded because the visible metadata did not meet license and model criteria.
- Data repository keyword searches remain noisy because "Aspen" frequently matches non-HYSYS terms.
- Manual license clarification is still required before any no-license GitHub repository can be archived.

## Next Suggestions

- Search GitHub for newly pushed repositories weekly with `HYSYS`, `Aspen HYSYS`, `HYSYS automation`, and `HYSYS Excel`.
- Add a license-contact backlog item for `Zinatullin76/Python-Hysys` and `Facul-101/PY-HYSYS`.
- Try targeted queries for exact filenames from papers, for example `"HYSYS" "Data Availability" ".hsc"` and `"Aspen HYSYS" "supplementary" "zip"`.
- Continue prioritizing GitHub results with explicit OSI licenses and visible `.hsc` or `.hscz` files.

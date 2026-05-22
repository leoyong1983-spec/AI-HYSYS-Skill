# CASE heartbeat 2026-05-22 0818Z

- Run time (UTC): 2026-05-22T08:18:34.136Z
- Agent role: Discovery & Fetch Agent for public Aspen HYSYS cases
- Repository gate: `main`, clean worktree, `git pull --ff-only origin main` already up to date
- Run directory: `CASE/2026-05-22-heartbeat-0818Z/`
- Artifacts directory: not created; no files were downloaded in this run
- Model run status: not_run for every entry; no Aspen HYSYS model was opened, executed, or solved

## Search Mines

- GitHub code search: `.hsc`, `.hscz`, `.xml`, `.compound`
- GitHub repository-tree checks for recent and high-relevance Aspen HYSYS repositories
- Mendeley Data public pages and prior public API targets
- Zenodo public records API
- Figshare, Harvard Dataverse, GitLab, and open-web search pages

## Keywords

- `extension:hsc`, `extension:hscz`, `extension:xml`, `extension:compound`
- `"Aspen HYSYS" ".hsc"`, `"Aspen HYSYS" ".hscz"`, `"HYSYS XML"`
- `"Aspen HYSYS" "simulation files"`, `"Aspen HYSYS" "supplementary"`
- `"Aspen HYSYS" "Mendeley Data" "HYSYS files"`
- `"Aspen HYSYS" "Zenodo" "HSC"`
- `Python COM MATLAB Excel automation HYSYS`

## Download Summary

No new HYSYS case was downloaded. The run found no clearly licensed, nonduplicate HYSYS main model that satisfied the archive rules.

| Case / sweep | Source page | Download URL | Local path | Selection reason | Quality |
|---|---|---|---|---|---|
| GitHub licensed duplicate / no-case sweep | https://github.com/search?q=Aspen+HYSYS&type=repositories | Not used | Not downloaded | Recent MIT/public repositories were either already archived (`shahria-sunny/Natural-Gas-Sweetening`, `shahria-sunny/CDU-Simulation-Optimization`) or automation/data repositories without a qualifying HYSYS case file (`GaboTalero/HYSYS-Python-Case-Builder`, `Galigeigei-Z/HDA-Surrogate-Optimization`, `edgarsmdn/Aspen_HYSYS_Python`). | D |
| GitHub no-license `.hsc` and HYSYS XML sweep | https://github.com/SinaGhanbarii/HDA-Plant-Simulation ; https://github.com/royhanikbarr/Gas-Turbine-Hysys ; https://github.com/JeePeiQi0101/Aspen.HYSYS ; https://github.com/masoud-abdi/The-simulation-of-Acetic-Acid-process | Raw and codeload URLs not used | Not downloaded | Multiple public repositories expose `.hsc` or HYSYS-named `.xml` files, but no explicit license was detected and the source pages/filenames are already present in prior CASE candidate records. | D |
| Mendeley Data HYSYS dataset sweep | https://data.mendeley.com/datasets/8r8ztbkfjj/1 ; https://data.mendeley.com/datasets/r3875vhrjs/1 ; https://data.mendeley.com/datasets/wzd6j2pd4v/1 ; https://data.mendeley.com/datasets/g5k7tndk77 ; https://data.mendeley.com/datasets/9384yj4xg3/5 | Mendeley public file URLs not used | Not downloaded | Model-bearing LNG/BOG and ASU datasets are already recorded or archived. Other Mendeley records were previously logged as metadata/no-model or not HYSYS-main-case payloads. | D |
| Zenodo HYSYS record sweep | https://zenodo.org/records/10966344 ; https://zenodo.org/records/18806107 ; https://zenodo.org/records/7787405 ; https://zenodo.org/records/15476366 | https://zenodo.org/api/records/?q=%22Aspen%20HYSYS%22%20hsc&size=10 | Not downloaded | Known HYSYS model records are duplicates; other records expose PDFs, spreadsheets, documents, or `.lnr` files rather than HYSYS `.hsc/.hscz` cases. | D |
| Figshare / Dataverse / GitLab / OA supplementary sweep | Public search pages | Not used | Not downloaded | No no-login, clearly licensed, nonduplicate HYSYS `.hsc`, `.hscz`, HYSYS XML, `.compound`, or model-bearing archive was confirmed. | D |

## License And Public Access Notes

- MIT/public GitHub model repositories already archived in CASE were not downloaded again.
- No-license GitHub repositories were treated as manual permission candidates only.
- Mendeley `8r8ztbkfjj` is public and metadata-declared CC BY 4.0, but already represented by prior CASE metadata.
- Mendeley `r3875vhrjs` is public and CC BY-NC 3.0, but already archived in `CASE/2026-05-22-heartbeat-0618Z/`; commercial reuse remains restricted.
- Zenodo `10966344` is public with CC BY-NC-ND 4.0 metadata and already archived; no-derivatives and non-commercial restrictions remain.
- Zenodo `18806107` is public with CC BY 4.0 metadata and already archived.

## Recommended Automation Use

- Use existing archived copies for natural-gas sweetening, CDU, ASU, LNG/BOG, Tennessee Eastman, and OCC/ASU/CCS tests.
- Use this run as a search-filter and duplicate-control record.
- Keep no-license `.hsc` and HYSYS XML repositories in a manual author-permission queue.

## Dedupe Basis

- Existing CASE records matched by source page, repository URL, download URL, title, and filenames.
- Duplicate or already logged HYSYS filenames include `Gas Sweetening.hsc`, `project.hsc`, `GTU Simulation.hsc`, `Test_file_hysys_python.hsc`, `NODECFINAL.hsc`, `1-HDA-Setup.hsc`, `Separazione_reattori.hsc`, `GROUP_17.hsc.hsc`, `Aspen HYSYS simulation file_Parallel.xml`, `Gas Turbine Power Plant Simulation.hsc`, `Simulation Production Butyl Chloride.hsc`, `acetic fin.hsc`, `April to October.hsc`, `November to March.hsc`, `HYSYS simulation of 40 bara GOX 95 purity.hsc`, `HYSYS simulation of 40 bara LOX 95 purity.hsc`, `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC`, and `7. Sistema Integrado OCC,ASU,CCS.hsc`.
- GitHub tree checks found no new licensed model-bearing repository outside the existing archive and manual-review queues.

## Residual Risks

- No model was loaded in Aspen HYSYS; version metadata is repository- or record-derived only.
- GitHub code search may miss binary files; repository-tree checks were used for high-relevance repositories to reduce this gap.
- Some public records mention Aspen HYSYS but expose only papers, reports, screenshots, spreadsheets, scripts, or non-HYSYS case formats.
- No-license public `.hsc` files may be technically useful, but rights for archival and redistribution remain unresolved.

## Follow-Up Recommendations

1. Keep the existing duplicate allowlist for Mendeley `8r8ztbkfjj`, Mendeley `r3875vhrjs`, Zenodo `10966344`, Zenodo `14882867`, and Zenodo `18806107`.
2. Re-check high-value no-license GitHub repositories only if a license file appears or author permission is obtained.
3. Prioritize future searches on new DOI-backed Mendeley/Zenodo/Figshare records with direct `.hsc` or `.hscz` files.
4. Continue recording no-model and duplicate sweeps to prevent repeated downloads.

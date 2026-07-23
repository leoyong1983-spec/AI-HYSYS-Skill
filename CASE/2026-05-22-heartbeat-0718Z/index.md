# CASE heartbeat 2026-05-22 0718Z

- Run time (UTC): 2026-05-22T07:18:33.188Z
- Agent role: Discovery & Fetch Agent for public Aspen HYSYS cases
- Repository gate: `main`, clean worktree, `git pull --ff-only origin main` already up to date
- Run directory: `CASE/2026-05-22-heartbeat-0718Z/`
- Artifacts directory: not created; no files were downloaded in this run
- Model run status: not_run for every entry; no Aspen HYSYS model was opened, executed, or solved

## Search Mines

- GitHub code search and repository-tree checks
- Mendeley Data public dataset pages and public API checks
- Zenodo public records API
- Figshare, Harvard Dataverse, GitLab, and open web search checks

## Keywords

- `extension:hsc`, `extension:hscz`, `extension:xml`, `extension:compound`
- `"Aspen HYSYS" ".hsc"`, `"Aspen HYSYS" ".hscz"`, `"HYSYS XML"`
- `"Aspen HYSYS" "Mendeley Data"`, `"Aspen HYSYS" "Zenodo"`
- `LNG BOG recondensation HYSYS files`, `cryogenic air separation HYSYS simulation`
- `Python COM MATLAB Excel automation HYSYS`

## Download Summary

No new HYSYS case was downloaded. The strongest model-bearing hits were duplicates already represented in CASE, or public repositories without explicit redistribution licenses.

| Case / sweep | Source page | Download URL | Local path | Selection reason | Quality |
|---|---|---|---|---|---|
| Mendeley LNG/BOG recondensation duplicate | https://data.mendeley.com/datasets/8r8ztbkfjj/1 | https://data.mendeley.com/public-files/datasets/8r8ztbkfjj/files/939edba8-4b16-441d-b0bc-7609c2688f18/file_downloaded | Not downloaded | Public Mendeley record says it contains two HYSYS `.hsc` files for LNG terminal BOG recondensation, but the source page, title, and filenames are already recorded in prior CASE metadata. | D |
| Mendeley cryogenic ASU duplicate | https://data.mendeley.com/datasets/r3875vhrjs/1 | Mendeley public file URLs for the GOX and LOX `.hsc` models | Not downloaded | This is a high-quality ASU dataset with two `.hsc` files, but it was downloaded in `CASE/2026-05-22-heartbeat-0618Z/`. | D |
| GitHub licensed duplicates | https://github.com/shahria-sunny/Natural-Gas-Sweetening ; https://github.com/shahria-sunny/CDU-Simulation-Optimization | codeload zip URLs | Not downloaded | Both MIT repositories expose `.hsc` models, reports, README, and license files, but both were already archived in `CASE/2026-05-11-heartbeat-0741Z/`. | D |
| GitHub no-license model candidates | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys ; https://github.com/Anikesh31/simulator_codingplatform_integration ; https://github.com/Corey-McInrue/Node-C-ASPEN-HYSYS | Raw `.hsc` URLs not used | Not downloaded | Trees expose `.hsc` files, but repository licenses are absent and the candidates are already in the manual permission queue. | D |
| Zenodo HYSYS sweep | https://zenodo.org/records/10966344 ; https://zenodo.org/records/18806107 ; https://zenodo.org/records/7787405 ; https://zenodo.org/records/15476366 | Zenodo record file APIs | Not downloaded | Known model-bearing records were duplicates; other results were PDF, spreadsheet, document, or non-HYSYS model payloads. | D |
| Figshare / Dataverse / GitLab / OA web sweep | Public search pages | Not used | Not downloaded | No new, no-login, clearly licensed Aspen HYSYS `.hsc`, `.hscz`, HYSYS XML, or `.compound` case package was found. | D |

## License And Public Access Notes

- Mendeley `8r8ztbkfjj` is public and metadata-declared CC BY 4.0, but it is a duplicate record for this archive.
- Mendeley `r3875vhrjs` is public and CC BY-NC 3.0; it was already downloaded in the prior 0618Z run. Commercial reuse remains restricted.
- `shahria-sunny/Natural-Gas-Sweetening` and `shahria-sunny/CDU-Simulation-Optimization` are public MIT repositories and already archived.
- `Mahdi-Arashian/sour-gas-sweetening-hysys`, `Anikesh31/simulator_codingplatform_integration`, and `Corey-McInrue/Node-C-ASPEN-HYSYS` are public GitHub repositories, but no explicit license was detected; no model download was performed.
- Zenodo `10966344` is public with CC BY-NC-ND 4.0 metadata, and Zenodo `18806107` is public with CC BY 4.0 metadata; both are already represented in CASE.

## Recommended Automation Use

- Use existing archived ASU, LNG/BOG, gas sweetening, crude distillation, Tennessee Eastman, and OCC/ASU/CCS packages for automation tests.
- Use this run as a duplicate-control and search-filter audit entry.
- Keep no-license `.hsc` repositories in a manual permission queue; do not treat them as redistributable benchmarks.

## Dedupe Basis

- Existing CASE records matched by source page, download URL, title, and model filenames.
- Known duplicate filenames include `April to October.hsc`, `November to March.hsc`, `HYSYS simulation of 40 bara GOX 95 purity.hsc`, `HYSYS simulation of 40 bara LOX 95 purity.hsc`, `Gas Sweetening.hsc`, `project.hsc`, `GTU Simulation.hsc`, `Test_file_hysys_python.hsc`, `NODECFINAL.hsc`, `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC`, and `7. Sistema Integrado OCC,ASU,CCS.hsc`.
- Mendeley and Zenodo duplicate source pages were already present in `CASE/**/sources.json` and `CASE/**/index.md`.

## Residual Risks

- No model was loaded in Aspen HYSYS; HYSYS versions are inferred only from repository or record metadata where available.
- GitHub code search may miss binary files or files hidden in release assets, so repository-tree checks were used for recent high-relevance repositories.
- Some public pages describe Aspen HYSYS use but expose only papers, spreadsheets, screenshots, or scripts, not a redistributable HYSYS case.
- No-license public GitHub `.hsc` files may be technically useful, but redistribution rights remain unresolved.

## Follow-Up Recommendations

1. Keep `8r8ztbkfjj`, `r3875vhrjs`, Zenodo `10966344`, `14882867`, and `18806107` on the duplicate allowlist.
2. Prioritize future searches on newly published Mendeley/Zenodo records with DOI, explicit license, and direct `.hsc` or `.hscz` files.
3. Consider contacting authors of no-license GitHub `.hsc` repositories if those cases are important enough to include.
4. Continue avoiding metadata-only, PDF-only, installer-only, and no-license case packages.

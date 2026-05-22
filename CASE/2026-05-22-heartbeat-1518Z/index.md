# CASE heartbeat 2026-05-22 1518Z

- Run time (UTC): 2026-05-22T15:18:56.088Z
- Agent role: Discovery & Fetch Agent for public Aspen HYSYS cases
- Repository gate: `main`, clean worktree, previous 0818Z local commit pushed successfully, `git pull --ff-only origin main` already up to date
- Run directory: `CASE/2026-05-22-heartbeat-1518Z/`
- Artifacts directory: not created; no files were downloaded in this run
- Model run status: not_run for every entry; no Aspen HYSYS model was opened, executed, or solved

## Search Mines

- GitHub repository search sorted by recent update
- GitHub code search for `.hsc` and `.hscz`
- GitHub tree inspection for the newly touched `edgarsmdn/Aspen_HYSYS_Python` repository
- Zenodo public records API with `Aspen HYSYS`, `hsc`, `hscz`, `simulation files`, and `HYSYS files`
- Mendeley Data, Figshare, Harvard Dataverse, GitLab, and open web search checks

## Keywords

- `extension:hsc`, `extension:hscz`, `extension:xml`, `extension:compound`
- `"Aspen HYSYS" ".hsc"`, `"Aspen HYSYS" ".hscz"`, `"HYSYS XML Cases"`
- `"Aspen HYSYS" "simulation files"`, `"Aspen HYSYS" "HYSYS files"`
- `"Aspen HYSYS" "Mendeley Data"`, `"Aspen HYSYS" "Zenodo"`
- `Python COM MATLAB Excel automation HYSYS`

## Download Summary

No new HYSYS case was downloaded. The run found no clearly licensed, nonduplicate HYSYS main model that satisfied the archive rules.

| Case / sweep | Source page | Download URL | Local path | Selection reason | Quality |
|---|---|---|---|---|---|
| Prior 0818Z commit recovery | local git commit `3ab2d64` | origin/main push | Not a download | The previous heartbeat's CASE index was successfully pushed before this run continued. | D |
| GitHub recent Aspen HYSYS sweep | https://github.com/search?q=Aspen+HYSYS&type=repositories | Not used | Not downloaded | Recent repo search returned known model archives, automation-only repos, or no-license candidates already represented in CASE. | D |
| `edgarsmdn/Aspen_HYSYS_Python` updatedAt recheck | https://github.com/edgarsmdn/Aspen_HYSYS_Python | https://codeload.github.com/edgarsmdn/Aspen_HYSYS_Python/zip/refs/heads/main | Not downloaded | MIT repo still contains `Test_1.hsc` plus Python scripts; this exact source and file are already archived. `pushedAt` remained old while `updatedAt` changed, so no new payload was found. | D |
| GitHub no-license `.hsc` candidate sweep | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys ; https://github.com/SinaGhanbarii/HDA-Plant-Simulation ; https://github.com/royhanikbarr/Gas-Turbine-Hysys ; https://github.com/masoud-abdi/The-simulation-of-Acetic-Acid-process | Raw/codeload URLs not used | Not downloaded | These public repositories expose `.hsc` or HYSYS-named XML files but lack explicit licenses and are already in the manual permission queue. | D |
| Zenodo HYSYS/hsc/hscz sweep | https://zenodo.org/records/10966344 ; https://zenodo.org/records/18806107 ; https://zenodo.org/records/19469917 ; https://zenodo.org/records/15476366 | https://zenodo.org/api/records/?q=%22Aspen%20HYSYS%22%20hsc&size=10 | Not downloaded | Known HYSYS model records were duplicates; several fresh `hsc` hits were astronomy HSC, PDF-only, spreadsheet-only, `.lnr`, or RAR records without confirmed redistributable HYSYS main case payload. | D |
| Mendeley/Figshare/Dataverse/GitLab/open-web sweep | Public search pages | Not used | Not downloaded | No no-login, clearly licensed, nonduplicate `.hsc`, `.hscz`, HYSYS XML, `.compound`, or model-bearing archive was confirmed. | D |

## License And Public Access Notes

- `edgarsmdn/Aspen_HYSYS_Python` is public MIT, but `Test_1.hsc` is already archived.
- `shahria-sunny/Natural-Gas-Sweetening` and `shahria-sunny/CDU-Simulation-Optimization` remain public MIT duplicates.
- No-license GitHub `.hsc` repositories were not downloaded because redistribution rights are unclear.
- Zenodo `10966344` is public with CC BY-NC-ND 4.0 metadata and already archived; derivative and commercial restrictions remain.
- Zenodo `18806107` is public with CC BY 4.0 metadata and already archived.
- Zenodo `19469917` has CC BY 4.0 metadata and a RAR upload, but no qualifying HYSYS main file was confirmed in this run and it has been treated previously as a no-model/unclear payload target.

## Recommended Automation Use

- Use existing archived copies for Python-COM/spreadsheet bridge, gas sweetening, CDU, ASU, LNG/BOG, Tennessee Eastman, and OCC/ASU/CCS tests.
- Treat this run as duplicate-control and latest-search evidence.
- Keep no-license `.hsc` candidates in manual permission review only.

## Dedupe Basis

- Existing CASE records matched by source page, repository URL, download URL, title, and filenames.
- Duplicate or already logged model names include `Test_1.hsc`, `Gas Sweetening.hsc`, `project.hsc`, `GTU Simulation.hsc`, `1-HDA-Setup.hsc`, `Separazione_reattori.hsc`, `GROUP_17.hsc.hsc`, `Gas Turbine Power Plant Simulation.hsc`, `Simulation Production Butyl Chloride.hsc`, `acetic fin.hsc`, `April to October.hsc`, `November to March.hsc`, `HYSYS simulation of 40 bara GOX 95 purity.hsc`, `HYSYS simulation of 40 bara LOX 95 purity.hsc`, `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC`, and `7. Sistema Integrado OCC,ASU,CCS.hsc`.
- GitHub code search for `HYSYS` with `.hsc` and `.hscz` returned no new indexed code hits.
- Zenodo `hsc` hits were filtered to avoid astronomy HSC and PDF-only false positives.

## Residual Risks

- No model was loaded in Aspen HYSYS; version metadata is inferred only from repository or record text where available.
- GitHub code search may miss binary payloads; repository search and targeted tree checks were used to reduce the gap.
- Some Zenodo and paper records mention HYSYS but expose only papers, tables, RAR files, `.lnr` files, or ambiguous supplemental data.
- No-license public model files may be technically relevant but cannot be safely archived without explicit permission.

## Follow-Up Recommendations

1. Keep the existing duplicate allowlist for `edgarsmdn/Aspen_HYSYS_Python`, Mendeley `8r8ztbkfjj`, Mendeley `r3875vhrjs`, Zenodo `10966344`, Zenodo `14882867`, and Zenodo `18806107`.
2. Re-check no-license model repositories only when a license file or author permission appears.
3. For Zenodo `19469917`, only revisit if a future API/file inspection confirms a safe, non-executable `.hsc/.hscz` payload inside the archive; do not download ambiguous RAR content by default.
4. Continue prioritizing DOI-backed records with explicit licenses and direct `.hsc` or `.hscz` files.

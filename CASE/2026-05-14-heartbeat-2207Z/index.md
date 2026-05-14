# CASE Heartbeat 2026-05-14 2207Z

## 1. Run Time

- Trigger UTC time: 2026-05-14T22:07:13.077Z
- Local workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-14-heartbeat-2207Z
- Artifacts directory: CASE/2026-05-14-heartbeat-2207Z/artifacts
- Model run status: not_run for all entries; no HYSYS model was opened, executed, solved, or validated.

## 2. Searched Mining Areas

- GitHub repository search: primary pass over HYSYS, Aspen HYSYS, HYSYS Python, HYSYS MATLAB, HYSYS automation, HYSYS simulation, and HYSYS optimization.
- GitHub code search: extension:hsc, extension:hscz, extension:compound, HYSYS XML Cases, win32com and MATLAB automation queries. The code index returned no qualifying model-file hits, likely because these extensions are binary or not indexed.
- Zenodo API targeted sweep: Aspen HYSYS hsc, hscz, case file, simulation file, HYSYS XML Cases, CO2 capture supplementary, and LNG supplementary.
- Web search spot-check: GitHub and Zenodo high-signal HYSYS model queries were used to confirm known duplicates and candidate visibility.

## 3. Keywords Used

- `HYSYS`, `Aspen HYSYS`, `HYSYS automation`, `HYSYS Python`, `HYSYS MATLAB`, `HYSYS simulation`, `HYSYS optimization`
- `HYSYS extension:hsc`, `Aspen HYSYS extension:hsc`, `HYSYS extension:hscz`, `HYSYS extension:compound`, `HYSYS XML Cases extension:xml`
- `Aspen HYSYS hsc`, `Aspen HYSYS hscz`, `Aspen HYSYS case file`, `Aspen HYSYS simulation file`, `Aspen HYSYS supplementary material CO2 capture`, `Aspen HYSYS LNG supplementary`

## 4. Downloaded Case List

No new HYSYS model payload was downloaded in this run.

Reason: the best newly discovered GitHub candidates contain `.hsc` files and companion materials, but GitHub API did not detect a license. The only clearly public/licensed Zenodo hit with HYSYS `.hsc` files was already archived in the existing CASE library, so duplicate payload download was skipped.

## 5. Candidate Findings

### D - SinaGhanbarii/HDA-Plant-Simulation

- Source page: https://github.com/SinaGhanbarii/HDA-Plant-Simulation
- Download URL considered: https://github.com/SinaGhanbarii/HDA-Plant-Simulation
- Local evidence: `artifacts/github-SinaGhanbarii__HDA-Plant-Simulation-repo.json`, `artifacts/github-SinaGhanbarii__HDA-Plant-Simulation-tree.json`
- HYSYS files found in tree: 10 `.hsc` files under `HDA 2024 Aspen/`
- Companion material: `HDA Report.pdf`, 3 Excel workbooks, MATLAB scripts, README
- Selection reason: strongest new GitHub candidate for reaction/separation/heat-exchanger workflow testing.
- License/public access note: public repository metadata is accessible, but no License was detected; no payload downloaded.
- Recommended automation use: after permission review, use for staged HDA model loading, sensitivity and optimization integration tests.
- Dedupe basis: new source URL and candidate title; no model SHA calculated because model payload was not downloaded.
- Residual risk: license/redistribution rights unresolved; scripts were not executed.

### D - masoud-abdi/The-simulation-of-Acetic-Acid-process

- Source page: https://github.com/masoud-abdi/The-simulation-of-Acetic-Acid-process
- Download URL considered: https://github.com/masoud-abdi/The-simulation-of-Acetic-Acid-process
- Local evidence: `artifacts/github-masoud-abdi__The-simulation-of-Acetic-Acid-process-repo.json`, `artifacts/github-masoud-abdi__The-simulation-of-Acetic-Acid-process-tree.json`
- HYSYS files found in tree: `acetic fin.hsc`
- Companion material: `HYSYS-Print.pdf`, `Acid-Material.pdf`, README
- Selection reason: README/description explicitly mention ASPEN HYSYS v10 and stream/PFD material.
- License/public access note: public repository metadata is accessible, but no License was detected; no payload downloaded.
- Recommended automation use: after permission review, use for HYSYS V10 compatibility and report-to-case comparison.
- Dedupe basis: source URL, title and filename candidate; no model SHA calculated.
- Residual risk: license unresolved; path contains spaces and should be covered by later automation tests.

### D - Mahdi-Arashian/sour-gas-sweetening-hysys

- Source page: https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys
- Download URL considered: https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys
- Local evidence: `artifacts/github-Mahdi-Arashian__sour-gas-sweetening-hysys-repo.json`, `artifacts/github-Mahdi-Arashian__sour-gas-sweetening-hysys-tree.json`
- HYSYS files found in tree: `GTU Simulation.hsc`
- Companion material: sour gas sweetening PDF report and README
- Selection reason: strong fit for natural gas processing and DEA acid-gas removal testing.
- License/public access note: public repository metadata is accessible, but no License was detected; no payload downloaded.
- Recommended automation use: after permission review, use for amine sweetening and gas treating benchmarks.
- Dedupe basis: source URL, title and filename candidate; no model SHA calculated.
- Residual risk: license unresolved.

### D - royhanikbarr/Aspen-Hysys-Simulation

- Source page: https://github.com/royhanikbarr/Aspen-Hysys-Simulation
- Download URL considered: https://github.com/royhanikbarr/Aspen-Hysys-Simulation
- Local evidence: `artifacts/github-royhanikbarr__Aspen-Hysys-Simulation-repo.json`, `artifacts/github-royhanikbarr__Aspen-Hysys-Simulation-tree.json`
- HYSYS files found in tree: `Design Simulation Production Butyl Chloride/Simulation Production Butyl Chloride.hsc`
- Companion material: paper PDF and README
- Selection reason: has HYSYS case plus report-like material for organic chemical process simulation.
- License/public access note: public repository metadata is accessible, but no License was detected; no payload downloaded.
- Recommended automation use: after permission review, use for organic process case loading and report extraction tests.
- Dedupe basis: source URL, title and filename candidate; no model SHA calculated.
- Residual risk: license unresolved.

### D - ArturTask/HysysExcel

- Source page: https://github.com/ArturTask/HysysExcel
- Download URL considered: https://github.com/ArturTask/HysysExcel
- Local evidence: `artifacts/github-ArturTask__HysysExcel-repo.json`, `artifacts/github-ArturTask__HysysExcel-tree.json`
- HYSYS files found in tree: `Test_1.hsc`
- Companion material: Excel workbook, README, Python automation scripts
- Selection reason: relevant to Excel/Python-HYSYS bridge and Spreadsheet object handling.
- License/public access note: public repository metadata is accessible, but no License was detected; no payload downloaded.
- Recommended automation use: after permission review, use for COM object lifecycle, Spreadsheet release and duplicate filename tests.
- Dedupe basis: filename overlaps existing `Test_1.hsc` archives; SHA was not calculated because the model was not downloaded.
- Residual risk: license unresolved and possible duplicate lineage.

## 6. Duplicate / Skipped Licensed Hits

- Zenodo 14882867, `Dataset for publication "Onboard carbon capture for circular marine fuels"`, is public CC-BY-4.0 and includes HYSYS `.hsc` files, but it is already present in the CASE archive. No duplicate download.
- `GaboTalero/HYSYS-Python-Case-Builder` is MIT-licensed automation code, but no `.hsc/.hscz/HYSYS XML/.compound` model exists in the tree.
- `oscarcontrerasnavas/hysys-to-excel-intro` is GPL-3.0 and contains an Excel macro workbook, but no HYSYS model exists; no workbook was executed.

## 7. Quality Ratings

- A duplicate: Zenodo 14882867 remains high-quality but already archived.
- D candidates: newly discovered GitHub `.hsc` repositories without detected License or without qualifying model payload.
- No B/C new downloads were added because the license/redistribution boundary was not clear.

## 8. Safety Notes

- No executable, macro, script, workbook or HYSYS model was run.
- No `.hsc`, `.pdf`, `.xlsx`, `.xlsm`, `.m` or `.py` candidate payloads were downloaded from unlicensed repositories.
- Only public API/search metadata and repository tree metadata were archived.

## 9. Residual Risks

- GitHub search may miss binary model files because code search did not index `.hsc/.hscz/.compound` content.
- Some no-license repositories may be usable only after author permission or later license addition.
- Tree metadata confirms filenames, not model integrity or HYSYS version, because payloads were not downloaded.

## 10. Follow-up Recommendations

1. Add a manual-permission queue for `SinaGhanbarii/HDA-Plant-Simulation`, `masoud-abdi/The-simulation-of-Acetic-Acid-process`, `Mahdi-Arashian/sour-gas-sweetening-hysys`, and `royhanikbarr/Aspen-Hysys-Simulation`.
2. Add an allowlist/blocklist to suppress repeated no-license candidates until repository license changes.
3. Keep Zenodo 14882867 as duplicate-allowlist entry to avoid repeated rediscovery.
4. Continue GitHub-first discovery using repository-tree inspection rather than relying on GitHub code search for `.hsc` binaries.

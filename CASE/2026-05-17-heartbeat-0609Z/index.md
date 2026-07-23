# Discovery Heartbeat 2026-05-17 0609Z

## Run Time

- Trigger UTC: 2026-05-17T06:09:04.385Z
- Workspace: D:/CODEX/AI-HYSYS-Skill
- Output directory: CASE/2026-05-17-heartbeat-0609Z
- Model run status: not_run; no Aspen HYSYS model was opened, executed, or solved.

## Repository Gate

- Confirmed Git repository: yes
- Confirmed branch: main
- `git pull --ff-only origin main`: succeeded, already up to date
- Existing dedupe baseline: 197 structured source entries, 1084 filenames, 1081 SHA256 values

## Search Mines

- GitHub code search: `.hsc`, `.hscz`, `.compound`, HYSYS XML, Aspen HYSYS README, HYSYS automation, HYSYS MATLAB, HYSYS Excel
- GitHub repository search: Aspen HYSYS case/project, HYSYS simulation, HYSYS automation, HYSYS MATLAB, HYSYS LNG, HYSYS CO2 capture
- Secondary metadata: Zenodo, GitLab, Harvard Dataverse
- No ordinary broad web scraping was used.

## Keywords Used

- `Aspen HYSYS case`
- `Aspen HYSYS project`
- `HYSYS simulation`
- `HYSYS automation`
- `HYSYS MATLAB`
- `HYSYS LNG`
- `HYSYS CO2 capture`
- `HYSYS` with file extensions `.hsc`, `.hscz`, `.compound`, `.xml`
- `Aspen HYSYS .hsc` on Zenodo

## Downloaded Case List

No new case files were downloaded in this run.

Reason: all confirmed HYSYS model-bearing hits were already represented in existing CASE dedupe keys, or were no-license candidates already recorded previously. No new non-duplicate, clearly licensed benchmark package was confirmed.

## GitHub Model-Bearing Hits Checked

- afabrild/HYSYS-MATLAB-LINK: Distill_Example.hsc; license=none; duplicate_source_page=True
- AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR: Project-PR/hyApp.hsc; license=none; duplicate_source_page=True
- Corey-McInrue/Node-C-ASPEN-HYSYS: NODECFINAL.hsc; license=none; duplicate_source_page=True
- edgarsmdn/Aspen_HYSYS_Python: Test_1.hsc; license=MIT; duplicate_source_page=True
- Paryazdan/Aspen-HYSYS-Projects: YazdanihaPHw3aSim.hsc; license=none; duplicate_source_page=True
- royhanikbarr/Aspen-Hysys-Simulation: Design Simulation Production Butyl Chloride/Simulation Production Butyl Chloride.hsc; license=none; duplicate_source_page=True
- bpalotai/Flowsheet-toolbox: Cases/HX-model-V1/HysysModel/SampleModel_V2.hsc; license=none; duplicate_source_page=True
- Pouria-MK/_Jan.2024_Simulation-and-Economic-Evaluation-of-Syngas-Generation-Plant-using-DMR-and-SMR-Reactors: SIM/SynGas-SMR-DMR(integration).hsc, SIM/SynGas-SMR-DMR(main).hsc; license=none; duplicate_source_page=True
- SinaGhanbarii/HDA-Plant-Simulation: HDA 2024 Aspen/1-HDA-Setup.hsc, HDA 2024 Aspen/2-HDA-InletPFR.hsc, HDA 2024 Aspen/3-HDA-OutletPFR.hsc, HDA 2024 Aspen/READY_HDA-Setup.hsc, HDA 2024 Aspen/Working_HDA-Setup.hsc, HDA 2024 Aspen/Working_HDA-Setup_10_Shortcut_Column.hsc, HDA 2024 Aspen/Working_HDA-Setup_11_Recycle_Column.hsc, HDA 2024 Aspen/Working_HDA-Setup_12_Toluene_Recycle.hsc, HDA 2024 Aspen/Working_HDA-Setup_8_ProductColumn.hsc, HDA 2024 Aspen/Working_HDA-Setup_8_Stabilizer.hsc; license=none; duplicate_source_page=True
- marcellobozzini/Python-Driving-License: Separazione_reattori.hsc; license=none; duplicate_source_page=True

## Zenodo Model-Bearing Hits Checked

- Aspen HYSYS model for the Tennessee Eastman process (10.5281/zenodo.10966344): files=TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC; duplicate in existing CASE dedupe keys
- Calculation and Simulation Data for Modular Oxy-Combustion and Carbon Capture in Associated Petroleum Gas Valorization (10.5281/zenodo.18806107): files=1. Análisis Multicriterio.xlsx, 3. Calculo del poder calorifico de los bloques.xlsx, 6. Temperatura de salida de los gases de combustion.EES, 7. Sistema Integrado OCC,ASU,CCS.hsc, 5. Poder calorifico por bloques final.EES, 2. Calculo de la Potencia nominal.xlsx, 4. Balance estequiometrico para el proceso combustion.EES; duplicate in existing CASE dedupe keys

## Source Pages And Download URLs

- GitHub search evidence: see `artifacts/github-0609-code-normalized.json`, `artifacts/github-0609-repo-search-normalized.json`, and `artifacts/github-0609-inspection-summary.json`
- Zenodo records screened: https://zenodo.org/records/10966344 and https://zenodo.org/records/18806107
- Duplicate Zenodo download URLs observed:
  - https://zenodo.org/api/records/10966344/files/TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC/content
  - https://zenodo.org/api/records/18806107/files/7.%20Sistema%20Integrado%20OCC,ASU,CCS.hsc/content

## Local Paths

- `CASE/2026-05-17-heartbeat-0609Z/index.md`
- `CASE/2026-05-17-heartbeat-0609Z/sources.json`
- `CASE/2026-05-17-heartbeat-0609Z/artifacts/`

## Selection Rationale

- GitHub remained the primary search target as requested.
- Repositories were not downloaded unless they contained a HYSYS model and passed dedupe and license checks.
- Zenodo HYSYS model records were not downloaded because they were existing duplicates.
- No scripts, macros, executables, or models were run.

## Quality Ratings

- New benchmark downloads: none
- GitHub duplicate/no-license evidence: D
- Zenodo duplicate evidence: D
- External negative search evidence: D

## License And Public Access Notes

- `edgarsmdn/Aspen_HYSYS_Python` is MIT licensed but already present in CASE.
- Zenodo record 10966344 is open with CC BY-NC-ND 4.0 metadata but already present in CASE.
- Zenodo record 18806107 is open with CC BY 4.0 metadata but already present in CASE.
- Multiple GitHub model repositories lack explicit licenses, so they remain candidate-only unless already archived under prior rules.

## Recommended Automation Uses

- Use this run as freshness and dedupe evidence.
- Continue using existing archived copies of Zenodo 10966344, Zenodo 18806107, and prior GitHub model packages for benchmark evaluation.
- Do not run any candidate model without a separate HYSYS runtime authorization and sandboxed execution plan.

## Dedupe Basis

- Existing source pages matched for model-bearing GitHub repositories.
- Existing source pages and filenames matched for Zenodo 10966344 and 18806107.
- Existing filename keys matched for multiple `.hsc` files such as `Test_1.hsc`, `Distill_Example.hsc`, and `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC`.

## Residual Risks

- GitHub code search treats `.hsc` as Haskell in many false positives.
- GitHub repositories without licenses may later add a license or change contents; future runs should re-check metadata.
- External repository APIs can miss files embedded inside archives or supplementary landing pages.
- No HYSYS runtime validation was performed.

## Follow-Up Suggestions

- Add a query filter or postprocessor that distinguishes Aspen HYSYS `.hsc` binaries from Haskell `.hsc` source files using repository context and file size.
- Maintain a candidate watchlist for no-license high-value GitHub repositories: `bpalotai/Flowsheet-toolbox`, `SinaGhanbarii/HDA-Plant-Simulation`, and Pouria-MK syngas DMR/SMR project.
- Consider a manual license review workflow for no-license academic GitHub repositories before any archival download.

# CASE discovery heartbeat 2026-05-22 0618Z

- Run time UTC: 2026-05-22T06:18:32.238Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-22-heartbeat-0618Z
- Model run status: not_run
- Git gate: main branch, `git pull --ff-only origin main` already up to date before discovery.

## Search mines

- GitHub code/repository search: `.hsc`, `.hscz`, `.compound`, HYSYS XML, "Aspen HYSYS" repositories, Python-COM and automation leads.
- Open data search: Zenodo API, Mendeley Data, Figshare/Harvard Dataverse/GitLab web search.
- Existing CASE dedupe inputs: all `CASE/**/index.md` and `sources.json` records; dedupe keys included source page, download URL, title, SHA256, and filenames.

## Keywords

- `Aspen HYSYS .hsc`
- `Aspen HYSYS .hscz`
- `HYSYS XML case`
- `Aspen HYSYS supplementary simulation files`
- `cryogenic air separation HYSYS hsc`
- `Python COM HYSYS automation`
- `Zenodo Aspen HYSYS hscz`
- `Mendeley Data Aspen HYSYS hsc`

## Downloaded cases

| Title | Source page | Download URL | Local path | Reason selected | Quality |
| --- | --- | --- | --- | --- | --- |
| Data for: Comparisons of thermodynamic and economic performances of cryogenic air separation plants designed for external and internal compression of oxygen | https://data.mendeley.com/datasets/r3875vhrjs/1 | https://data.mendeley.com/public-files/datasets/r3875vhrjs/files/b26e403f-de22-4b01-8924-f9575858f968/file_downloaded ; https://data.mendeley.com/public-files/datasets/r3875vhrjs/files/bf511dc5-75a5-4720-9753-627668f42047/file_downloaded | CASE/2026-05-22-heartbeat-0618Z/artifacts/MendeleyData_2019_CryogenicAirSeparation_SinglaChowdhury/ | Nonduplicate Mendeley Data record with DOI, clear public page, CC BY-NC 3.0 license, related Applied Thermal Engineering DOI, and two Aspen HYSYS `.hsc` files for 40 bara oxygen production by GOX compression and LOX pumping. | A |

### Downloaded artifact checksums

| File | Bytes | SHA256 | Source SHA256 match |
| --- | ---: | --- | --- |
| artifacts/MendeleyData_2019_CryogenicAirSeparation_SinglaChowdhury/HYSYS simulation of 40 bara GOX 95 purity.hsc | 1409549 | 7d8c91e7ba89327ef65d17504b33aea260b268e0ce584d0bb195371d04356428 | yes |
| artifacts/MendeleyData_2019_CryogenicAirSeparation_SinglaChowdhury/HYSYS simulation of 40 bara LOX 95 purity.hsc | 1481350 | bb743de844307e822d5f9ad92121e8a1991be968508e4829d5343130669340ee | yes |

## License and public access

- Mendeley Data record DOI: 10.17632/r3875vhrjs.1.
- Related article DOI: 10.1016/j.applthermaleng.2019.114025.
- Public access note: Mendeley Data page and DataCite metadata identify the dataset as public/open after the 2019-05-28 embargo date.
- License note: CC BY-NC 3.0. The license allows copying and redistribution with attribution for non-commercial use. Commercial reuse remains restricted, so keep this marked as non-commercial research/archive material.

## Recommended automation use

- Cryogenic air separation benchmark for HYSYS file loading, inventory extraction, and stream/equipment table readback.
- Comparison workflow for external gas oxygen compression versus liquid oxygen pumping at 40 bara and 95 percent oxygen purity.
- Candidate for sensitivity, optimization, and surrogate-model feature extraction after manual HYSYS version confirmation.

## Candidate and duplicate notes

| Candidate | Source page | Status | Reason | Quality |
| --- | --- | --- | --- | --- |
| Zenodo: Calculation and Simulation Data for Modular Oxy-Combustion and Carbon Capture in Associated Petroleum Gas Valorization | https://zenodo.org/records/18806107 | Not downloaded | Zenodo record contains `7. Sistema Integrado OCC,ASU,CCS.hsc`, DOI, and CC BY-4.0, but the same record and HYSYS file are already archived in prior CASE records. | D |
| Zenodo: Aspen HYSYS model for the Tennessee Eastman process | https://zenodo.org/records/10966344 | Not downloaded | Zenodo record contains `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC`, but it is already archived; license is CC BY-NC-ND 4.0, requiring caution for derivatives and commercial use. | D |
| GitHub licensed duplicates: shahria-sunny/Natural-Gas-Sweetening and shahria-sunny/CDU-Simulation-Optimization | https://github.com/shahria-sunny/Natural-Gas-Sweetening ; https://github.com/shahria-sunny/CDU-Simulation-Optimization | Not downloaded | Both MIT repositories contain `.hsc` models and reports, but both source pages and files are already present in previous CASE records. | D |
| GitHub no-license model candidates: Mahdi-Arashian/sour-gas-sweetening-hysys and marcellobozzini/Python-Driving-License | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys ; https://github.com/marcellobozzini/Python-Driving-License | Not downloaded | Trees contain `.hsc` files, but repository license is absent and both are already in the manual permission queue. | D |
| GitHub XML/HSCZ/compound sweep including JavierBerenguer/Trabajo-Final-de-Grado | https://github.com/JavierBerenguer/Trabajo-Final-de-Grado | Not downloaded | `ComponentDataBase.xml` is not a confirmed HYSYS XML case; `.hscz` and `.compound` searches found no qualifying new HYSYS model payload. | D |

## Dedupe basis

- New Mendeley Data source did not match existing CASE records by source page, DOI, title, or the two SHA256 values.
- Duplicate Zenodo/GitHub items matched prior records by source page, DOI, title, filename, or recorded model SHA.
- No compressed packages were downloaded; no executables, macros, scripts, or installers were run.

## Residual risks

- Aspen HYSYS version is unknown; the files were downloaded and hashed only.
- Models were not opened, solved, or validated in Aspen HYSYS.
- CC BY-NC 3.0 limits reuse to non-commercial contexts; downstream automation examples should keep attribution and non-commercial constraints visible.
- Mendeley Data does not expose a separate README in the dataset file list; process details are inferred from the dataset metadata, file names, and related article DOI.

## Follow-up recommendations

1. In a real HYSYS environment, open copies read-only and record version, solve state, stream table availability, and key oxygen/nitrogen product conditions.
2. Add this ASU pair to an automation smoke-test queue for file enumeration and non-solving metadata extraction.
3. Keep no-license GitHub `.hsc` repositories in the manual permission queue; do not archive them until a license or author permission is available.
4. Continue using Mendeley Data and Zenodo API filters for DOI-backed process datasets, because GitHub `.hscz` and HYSYS XML searches remain noisy.

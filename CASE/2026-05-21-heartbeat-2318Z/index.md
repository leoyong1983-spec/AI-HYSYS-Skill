# HYSYS Case Discovery Heartbeat - 2026-05-21 23:18Z

## Run Context

- Automation ID: `ai-hysys-case-2`
- Trigger time (UTC): `2026-05-21T23:18:25.261Z`
- Local folder: `CASE/2026-05-21-heartbeat-2318Z/`
- Repository gate: `main` branch confirmed; `git pull --ff-only origin main` completed before this run's CASE write.
- Model run status: no HYSYS models were opened, executed, solved, or validated.

## Search Mines

- GitHub code and repository search
- Zenodo record search
- Local CASE archive dedupe scan

## Keywords And Query Patterns

- `extension:hsc Aspen HYSYS`
- `extension:hscz Aspen HYSYS`
- `Aspen HYSYS README`
- `Aspen HYSYS simulation files`
- `HYSYS XML Cases`
- `Aspen HYSYS .hsc`
- `Aspen HYSYS Python`
- `HYSYS simulation optimization`
- `Zenodo Aspen HYSYS hsc`

## Downloaded Cases

No cases were downloaded in this run. The candidates found either lacked an explicit redistribution/license basis, were duplicates of prior CASE records, or did not contain a qualifying HYSYS main simulation file.

## Candidate Records

| Title | Source Page | Download URL | Local Path | Quality | Selection Reason | License/Public Access | Recommended Automation Use | Dedupe Basis | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bpalotai/Flowsheet-toolbox | https://github.com/bpalotai/Flowsheet-toolbox | https://codeload.github.com/bpalotai/Flowsheet-toolbox/zip/refs/heads/main | Not downloaded | D | Public repository contains a HYSYS `.hsc` sample model plus Excel and surrogate-model artifacts, but no explicit license was found. | Public GitHub page; no explicit license observed, so archival download was skipped. | Candidate for heat-exchanger surrogate/calibration workflow review only after permission or license clarification. | Existing CASE candidate: `CASE/2026-05-11-heartbeat-1411Z`; key file `Cases/HX-model-V1/HysysModel/SampleModel_V2.hsc`. | License ambiguity; model version unknown; no local HYSYS validation. |
| Gallo05952/Articolo_energies | https://github.com/Gallo05952/Articolo_energies | https://codeload.github.com/Gallo05952/Articolo_energies/zip/refs/heads/main | Not downloaded | D | Public repository contains `.hsc` files and Excel/CSV sensitivity data, but no explicit license was found and prior CASE evidence already recorded it. | Public GitHub page; no explicit license observed, so archival download was skipped. | Candidate for manual literature/source review if license can be clarified. | Existing CASE evidence: `CASE/2026-05-17-heartbeat-1611Z/artifacts/github-1611-model-bearing-repositories.json`; key files `50kmol_h_ALIM_N2_H2S_O2_Hashemi.hsc`, `Articolo_energies.hsc`. | License ambiguity; process/version metadata unclear; no local HYSYS validation. |
| dpatel322853/Lumped-dynamic-model-for-PST-calculation | https://github.com/dpatel322853/Lumped-dynamic-model-for-PST-calculation | https://codeload.github.com/dpatel322853/Lumped-dynamic-model-for-PST-calculation/zip/refs/heads/main | Not downloaded | D | Public repository appears related to HYSYS/PST workflow code but no `.hsc`, `.hscz`, HYSYS XML case, or `.compound` file was found. | Public GitHub page; no explicit license observed; no qualifying HYSYS model found. | Candidate only for possible automation-method notes, not for model archive. | Dedupe by repository URL and absence of qualifying model filenames in current search results. | May rely on external/private HYSYS files not included in the repository; license unclear. |
| atlanticbhandari07/CCS_Git_test_01 | https://github.com/atlanticbhandari07/CCS_Git_test_01 | https://codeload.github.com/atlanticbhandari07/CCS_Git_test_01/zip/refs/heads/main | Not downloaded | D | Public repository appears to contain CCS/HYSYS automation scripts, but no HYSYS main simulation file was found. | Public GitHub page; no explicit license observed; no qualifying HYSYS model found. | Candidate only for future Python-COM/CCS workflow pattern review if a licensed model source appears. | Dedupe by repository URL and absence of qualifying model filenames in current search results. | Automation code may require private local case files; license unclear; no local HYSYS validation. |

## Safety Notes

- No archive files were downloaded.
- No executable, macro, script, installer, or HYSYS model was run.
- No SHA256 values were generated because no new artifacts were saved.
- No existing CASE assets were removed, moved, or overwritten.

## Follow-Up Suggestions

- Keep model-bearing but unlicensed GitHub repositories in a manual-permission queue instead of archiving them.
- Continue prioritizing sources with explicit license/DOI plus downloadable `.hsc` or `.hscz` files.
- Tighten future GitHub searches with both license filters and tree-level extension checks before considering downloads.
- Continue Zenodo searches, but exclude PDF-only records unless their supplemental files include a HYSYS main model.

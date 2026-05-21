# HYSYS Case Discovery Run - 2026-05-21 22:18Z

## Run Status

- Automation ID: `ai-hysys-case-2`
- Trigger time UTC: `2026-05-21T22:18:26.234Z`
- Target directory: `CASE/2026-05-21-heartbeat-2218Z/`
- Repository gate: `main`, `git pull --ff-only origin main` completed successfully.
- Downloaded new HYSYS artifacts: 0
- HYSYS model execution status: not run. No HYSYS files, scripts, macros, or archives were opened or executed.

## Search Mines

- GitHub code and repository search for `.hsc`, `.hscz`, HYSYS XML, COM automation, README, and license combinations.
- GitLab and Bitbucket web search for public HYSYS model repositories.
- Zenodo API and public search for Aspen HYSYS records with DOI, license, and attached files.
- Figshare, Mendeley Data, Harvard Dataverse, and open-access supplement searches.
- Local `CASE/**/index.md` and `CASE/**/sources.json` dedupe by source page, download URL, title, DOI, filenames, and prior artifact paths.

## Keywords

- `extension:hsc`
- `extension:hscz`
- `"Aspen HYSYS" ".hsc"`
- `"Aspen HYSYS" ".hscz"`
- `"HYSYS XML Cases"`
- `"Aspen HYSYS" README license`
- `"Aspen HYSYS" supplementary simulation files`
- `"Python COM" HYSYS`
- `"Aspen HYSYS" Zenodo dataset`

## Download Case List

No new files were downloaded. The best public model-bearing hits were already archived in prior CASE folders, and the remaining title-relevant records did not expose a qualifying HYSYS main simulation file.

| Title | Source page | Download URL | Local path this run | Selection reason | Quality | License/public access | Recommended use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset for publication "Onboard carbon capture for circular marine fuels" | https://zenodo.org/records/14882867 | https://zenodo.org/api/records/14882867/files | Not downloaded | High-quality CC-BY-4.0 Zenodo dataset with DOI, HYSYS `.hsc` files, spreadsheets, notebooks, and related article. Already archived. | A | Open Zenodo record, DOI `10.5281/zenodo.14882867`, CC-BY-4.0. | Use existing archive for onboard carbon capture, methanol production, LNG support data, and spreadsheet-validation workflows. | Existing source page, DOI, title, and filenames in `CASE/2026-05-11-heartbeat-0026Z/`. | HYSYS version remains unknown because no model was opened in this run. |
| Calculation and Simulation Data for Modular Oxy-Combustion and Carbon Capture in Associated Petroleum Gas Valorization | https://zenodo.org/records/18806107 | https://zenodo.org/api/records/18806107/files | Not downloaded | Open Zenodo dataset with DOI, CC-BY-4.0, HYSYS v12.1 `.hsc`, Excel files, and EES calculations. Already archived. | A | Open Zenodo record, DOI `10.5281/zenodo.18806107`, CC-BY-4.0. | Use existing archive for OCC, ASU, CCS, APG valorization, and energy/exergy workflow tests. | Existing source page, DOI, title, and `7. Sistema Integrado OCC,ASU,CCS.hsc` in `CASE/2026-05-11-heartbeat-0222Z/`. | HYSYS model was not run; reported version is metadata-derived. |
| Hydrogen Co-Firing in Gas Turbines package candidate | https://zenodo.org/records/19469917 | https://zenodo.org/api/records/19469917/files/Upload%20data.rar/content | Not downloaded | Public CC-BY-4.0 record, but prior safe listing found only PNG/XLSX content and no HYSYS main file. | D | Open Zenodo record, DOI `10.5281/zenodo.19469917`, CC-BY-4.0. | Keep as a no-model exclusion example unless authors publish `.hsc`, `.hscz`, or HYSYS XML files. | Existing source page, DOI, title, archive filename, and prior listing in `CASE/2026-05-16-heartbeat-0608Z/`. | RAR package was not re-downloaded or re-inspected in this run. |
| Role of biogenic CO2 in refinery decarbonization. A case study of Colombian refineries | https://zenodo.org/records/15476366 | https://zenodo.org/api/records/15476366/files | Not downloaded | Public CC-BY-4.0 record references Aspen HYSYS V14 process simulation data, but files are `.lnr` and DOCX supplementary material, not HYSYS case files. Already recorded as a candidate. | D | Open Zenodo record, DOI `10.5281/zenodo.15476366`, CC-BY-4.0. | Metadata-only follow-up for refinery decarbonization literature; do not use as a HYSYS case corpus item. | Existing source page, DOI, title, and candidate note in `CASE/2026-05-14-heartbeat-1107Z/`. | No qualifying `.hsc`, `.hscz`, HYSYS XML, or `.compound` payload confirmed. |

## License And Public Access Notes

- No login, paywall, customer support, commercial training, or institution-only source was used.
- No archive was downloaded this run, so no new SHA256 hashes were produced.
- Existing duplicate records are public, but their archived copies should remain the canonical local artifacts.
- Candidate-only records are not recommended for benchmark ingestion until a real HYSYS main file is published.

## Recommended Automation Uses

- Reuse `CASE/2026-05-11-heartbeat-0026Z/artifacts/zenodo-14882867/` for CCUS, methanol, LNG, spreadsheet-validation, and DOI-backed source-quality tests.
- Reuse `CASE/2026-05-11-heartbeat-0222Z/artifacts/zenodo-18806107/` for APG valorization, oxy-combustion, ASU/CCS, and HYSYS v12.1 metadata tests.
- Keep Zenodo `19469917` and `15476366` in exclusion or candidate filters to avoid non-model downloads.

## Residual Risks

- Source metadata can change after this run; future runs should re-check Zenodo file lists before changing status.
- Duplicate decisions rely on local CASE indexes and sources files; no model was opened for binary-level inspection.
- Some public records contain large or compressed packages; archive inspection must remain listing-only and non-executing.

## Follow-Up Suggestions

1. Keep Zenodo `14882867` and `18806107` on the duplicate allowlist.
2. Keep Zenodo `19469917` and `15476366` on the no-model or candidate-only list unless qualifying HYSYS files appear.
3. Prioritize new searches toward repositories or DOI datasets exposing explicit `.hsc`, `.hscz`, or HYSYS XML filenames plus license text.

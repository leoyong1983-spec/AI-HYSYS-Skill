# HYSYS Case Discovery Heartbeat - 2026-05-22 03:18Z

## Run Context

- Automation ID: `ai-hysys-case-2`
- Trigger time (UTC): `2026-05-22T03:18:29.231Z`
- Local folder: `CASE/2026-05-22-heartbeat-0318Z/`
- Repository gate: `main` branch confirmed; `git pull --ff-only origin main` returned already up to date.
- Model run status: no HYSYS models were opened, executed, solved, or validated.

## Search Mines

- GitHub repository and code search
- GitHub tree-level file inspection
- Zenodo record API
- Figshare API
- Harvard Dataverse API
- Mendeley Data public search page
- Existing local CASE archive dedupe scan

## Keywords And Query Patterns

- `Aspen HYSYS`
- `Aspen HYSYS README`
- `extension:hsc Aspen HYSYS`
- `Aspen HYSYS .hsc`
- `Aspen HYSYS .hscz`
- `HYSYS XML Cases`
- `Aspen HYSYS simulation files`
- `Aspen HYSYS hsc hscz`
- `Aspen HYSYS Mendeley Data hsc`

## Downloaded Cases

No cases were downloaded in this run. Search results were either duplicates of existing CASE records, lacked explicit licenses for model-bearing repositories, or contained no qualifying HYSYS main simulation file.

## Candidate Records

| Title | Source Page | Download URL | Local Path | Quality | Selection Reason | License/Public Access | Recommended Automation Use | Dedupe Basis | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub no-license `.hsc` duplicate sweep | https://github.com/search?q=Aspen+HYSYS&type=repositories | not_downloaded_duplicate_or_no_license | Not downloaded | D | Tree checks resurfaced model-bearing public repositories such as `royhanikbarr/Gas-Turbine-Hysys`, `marcellobozzini/Python-Driving-License`, and `kush1706/Methanol_Synthesis_Aspen_hysys`, but all lack explicit repository licenses and are already represented in prior CASE records. | Public GitHub read access; no explicit license detected for model payloads. | Manual permission queue only; not suitable for automated ingestion. | Existing source pages and filenames in prior CASE records: `Gas Turbine Power Plant Simulation.hsc`, `Separazione_reattori.hsc`, `GROUP_17.hsc.hsc`. | License ambiguity; no local HYSYS validation; duplicates already logged. |
| GitHub no-model / empty-repository sweep | https://github.com/search?q=Aspen+HYSYS&type=repositories | not_downloaded_no_qualifying_hysys_model | Not downloaded | D | Rechecked recent or previously weak HYSYS keyword hits including `ved10544-spec/Ved10544`, `miladmolaee/AspenHysys`, `Amansurana2005/Oil-Well-Simulation-for-Gas-oil-separation-Using-Conceptual-Design-Builder-In-Aspen-HYSYS-Simulation`, `Ankesh-cloud/Simulation-of-Acid-Gas-Removal-Unit-using-ASPEN-HYSYS`, `Shreya88876/Aspen_file_shreya`, `shri2901/AspenHYSYS`, `DanielVazVaz/PySIS`, and `GaboTalero/HYSYS-Python-Case-Builder`. Tree checks found empty repos, README/PDF-only repos, or automation code without model payloads. | Mixed public GitHub access; most have no explicit license; `GaboTalero/HYSYS-Python-Case-Builder` is MIT but contains no HYSYS case file. | Use only as search-filter tuning or automation-reference context; do not archive as CASE benchmarks. | Existing CASE records already cover most of these repositories; this run reconfirmed no new qualifying payload. | Keyword matches are noisy; some repositories may change later. |
| Zenodo recent Aspen HYSYS sweep | https://zenodo.org/api/records/?q=%22Aspen%20HYSYS%22&size=25&sort=mostrecent | not_downloaded_duplicate_or_pdf_only | Not downloaded | D | Recent Zenodo query returned known model-bearing records already archived or logged (`14882867`, `18806107`, `10966344`) plus many PDF-only records. No new nonduplicate licensed `.hsc/.hscz` package was found. | Public Zenodo metadata; licenses vary from CC BY 4.0 to CC BY-NC-ND 4.0. No new files downloaded. | Use as duplicate avoidance and DOI backlog only. | `14882867` and `18806107` already have CASE records with `.hsc` artifacts; `10966344` is already logged and has CC BY-NC-ND restrictions. | Some PDF-only papers imply HYSYS use but do not expose models. |
| Figshare / Dataverse / Mendeley sweep | https://api.figshare.com/v2/articles/search; https://dataverse.harvard.edu/api/search; https://data.mendeley.com/research-data/?search=Aspen%20HYSYS%20hsc | not_downloaded_no_confirmed_open_hysys_model | Not downloaded | D | Figshare, Dataverse, and Mendeley public searches did not reveal a new open, clearly licensed HYSYS main model package in this run. | Only public metadata/search pages were inspected. No files downloaded. | Continue as lower-priority discovery channel; require file-list proof before any download. | Query terms and platform URLs; no qualifying new source_page found for ingestion. | Search interfaces may hide files behind dynamic UI; manual follow-up may be needed if a specific DOI appears. |

## Safety Notes

- No archive files were downloaded.
- No executable, macro, script, installer, or HYSYS model was run.
- No SHA256 values were generated because no new artifacts were saved.
- No existing CASE assets were removed, moved, or overwritten.

## Follow-Up Suggestions

- Maintain suppression/watchlist rules for known no-license `.hsc` repositories until authors add explicit license terms.
- Treat MIT automation repositories without `.hsc/.hscz/HYSYS XML/.compound` as automation references, not model cases.
- For Zenodo, prioritize records with exposed `.hsc` or `.hscz` files and skip PDF-only paper records.
- For Figshare/Mendeley/Dataverse, require an explicit file list before considering any download.

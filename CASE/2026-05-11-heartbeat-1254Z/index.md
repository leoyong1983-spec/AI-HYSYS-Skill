# CASE Heartbeat 2026-05-11 1254Z

## Run Metadata
- Run time (UTC): 2026-05-11T13:14:56Z
- Heartbeat folder: $hb
- Objective: Discover 1-3 new high-quality, non-duplicate, publicly archivable Aspen HYSYS benchmark cases.

## Search Mines
- Scientific repositories: Figshare API, Mendeley public dataset/API docs, OSF public search API, Zenodo API (attempted; timeout).
- Code hosting: GitHub repository search API + direct codeload package inspection.
- Official/community lane: no new openly downloadable official Aspen/PSE case package with explicit archive permission found in this run window.

## Keywords Used
- Aspen HYSYS case file, Aspen HYSYS .hsc, HYSYS XML, process simulation, supplementary material, model validation, Excel data, CO2, LNG, methanol.

## Downloaded Cases (This Run)
- New high-quality non-duplicate cases downloaded: **0**
- Reason: no newly discovered source satisfied all of: (a) contains HYSYS model/package, (b) non-duplicate against existing CASE baseline, (c) clear public-access/licensing for safe repository archiving.

## Candidate / Skip List
1. chickenhgbla/gaussian-process-rto
- Source page: https://github.com/chickenhgbla/gaussian-process-rto
- Download URL checked: https://codeload.github.com/chickenhgbla/gaussian-process-rto/zip/refs/heads/master
- Local evidence: rtifacts/chickenhgbla__gaussian-process-rto-master-zip-listing.txt
- Selection rationale: contains 	esting.hsc + CSV + Python scripts (automation potential).
- Quality rating: D (license unclear; not archived).
- Public access / license note: repository is public but no explicit LICENSE found in snapshot.
- Recommended automation use: pending maintainer license clarification.
- Dedupe basis: source_page and download_url not present in existing CASE baseline.

2. Figshare 25202060 (SO2 abatement control)
- Source page: https://researchdata.up.ac.za/articles/dataset/Evaluation_of_plantwide_control_strategies_implemented_for_an_SO2_abatement_plant/25202060
- Download URL: https://api.figshare.com/v2/articles/25202060/files
- Selection rationale: valid HYSYS case exists but already archived.
- Quality rating: D (duplicate skip).
- Public access / license note: CC BY 4.0, already captured in CASE/2026-05-11-heartbeat-0854Z.
- Dedupe basis: exact source_page + file names matched existing baseline.

3. sanjay-saran/dme-production-methanol
- Source page: https://github.com/sanjay-saran/dme-production-methanol
- Download URL checked: https://codeload.github.com/sanjay-saran/dme-production-methanol/zip/refs/heads/main
- Local evidence: rtifacts/sanjay-saran__dme-production-methanol-main-zip-listing.txt
- Selection rationale: topic-relevant but no .hsc/.xml detected.
- Quality rating: D (insufficient model artifact).
- Public access / license note: no explicit LICENSE found.
- Dedupe basis: source is new but fails minimum HYSYS model requirement.

## Dedupe Method
- Loaded all existing CASE/*/sources.json and deduped by source_page, download_url, title, file names, and known SHA256 where available.

## Residual Risks
- Zenodo API queries intermittently timed out (504), reducing recall for potential new .hsc records.
- Public repository visibility does not guarantee redistribution rights without explicit license.
- No local Aspen HYSYS runtime execution was performed; all model_run_status remain 
ot_run.

## Next Suggestions
- Add authenticated GitHub code search token for higher-precision extension:hsc discovery.
- Retry Zenodo iles.key search with backoff and smaller page sizes.
- Prioritize sources with explicit CC/MIT/BSD licensing to avoid archive-right ambiguity.

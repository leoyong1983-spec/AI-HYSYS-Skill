# CASE Heartbeat 2026-05-11 1521Z

- Run time (UTC): 2026-05-11T15:23:43Z
- Heartbeat folder: CASE/2026-05-11-heartbeat-1521Z
- Retrieval zones targeted: Mendeley Data API (/api/research-data/search + /public-api/datasets/{id}), prior CASE dedupe baseline (CASE/*/sources.json)
- Keywords used: Aspen HYSYS, HYSYS case file, LNG HYSYS, CO2 capture HYSYS, hydrogen liquefaction HYSYS

## Downloaded Cases (non-duplicate)

1. **Stratified Tank and Solar Collector using Aspen Custom Modeler (ACM)** (Quality **C**)
   - Source page: https://data.mendeley.com/datasets/pv4znnnv3j/1
   - Download URL (primary HYSYS case): https://data.mendeley.com/public-files/datasets/pv4znnnv3j/files/65ede85b-938e-4d46-831c-ddd7e183bffc/file_downloaded
   - Local path: CASE/2026-05-11-heartbeat-1521Z/artifacts/1000 KG DRYER.HSC
   - Why selected: public DOI-backed dataset, direct .HSC model file, non-duplicate by source/download/title/filename/SHA256.
   - License/public access: CC BY 4.0 (Mendeley Data, DOI 10.17632/pv4znnnv3j.1)
   - Recommended automation use: COM handover/smoke tests, parsing robustness tests, static integrity checks.

## Candidate-only (not downloaded as CASE model package)

1. **Mixed-integer optimization of distillation sequences with Aspen Plus** (Quality **D**)
   - Source: https://data.mendeley.com/datasets/wp9srb96th/1
   - Reason not downloaded: package focuses on Aspen Plus files, not confirmed HYSYS case coverage.

2. **LN2 precooling dual-pressure Claude cycle for hydrogen liquefaction** (Quality **D**)
   - Source: https://data.mendeley.com/datasets/wzd6j2pd4v/1
   - Reason not downloaded: metadata-exposed artifact does not include .hsc or HYSYS XML case files.

## Dedupe Evidence

- Dedupe keys checked against all existing CASE/*/sources.json: source_page, download_url, title, filenames, sha256.
- New source pv4znnnv3j was absent from existing records.
- Existing high-overlap IDs such as 8r8ztbkfjj and 9384yj4xg3 were detected as previously recorded and skipped.

## Safety and Residual Risks

- No model execution performed; model_run_status=not_run for all entries.
- MSI binaries (StratTank.msi, UTTSC.msi) were archived only and not executed.
- Supporting report/readme context is limited for the downloaded package, so benchmark context confidence is moderate.

## Next Suggestions

1. Prioritize queries combining HYSYS + DOI + supplementary case across Zenodo/Dataverse to find a second non-duplicate .hsc source.
2. For ACM/HYSYS mixed packages, prefer those that include README or validation tables to raise quality from C to B/A.

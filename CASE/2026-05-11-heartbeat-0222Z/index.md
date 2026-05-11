# Aspen HYSYS CASE Heartbeat - 2026-05-11-0222Z

## Run Metadata
- Run time (UTC): 2026-05-11T02:35:46Z
- Heartbeat folder: `CASE/2026-05-11-heartbeat-0222Z`
- Existing CASE dedupe baseline scanned: `CASE/2026-05-11-heartbeat-0026Z/index.md`, `CASE/2026-05-11-heartbeat-0026Z/sources.json`

## Search Mines and Focus Keywords
- Priority mines searched:
  - Zenodo (API + record pages)
  - Mendeley Data (targeted web checks)
  - Figshare (targeted web checks)
  - OSF (targeted web checks)
  - GitHub/GitLab/Bitbucket (targeted web checks and GitHub API probes)
  - PSE Community public pages
- Core keywords:
  - `Aspen HYSYS case file`
  - `Aspen HYSYS .hsc`
  - `HYSYS XML cases .xml`
  - `supplementary material`
  - `process simulation flowsheet`
  - `model validation experimental data Excel data`
  - domain themes: `hydrogen`, `CO2 capture`, `LNG`, `ammonia`, `methanol`

## Downloaded Cases (Non-duplicate)

### 1) Calculation and Simulation Data for Modular Oxy-Combustion and Carbon Capture in Associated Petroleum Gas Valorization (Zenodo 18806107)
- Quality: **B**
- Source page: https://zenodo.org/records/18806107
- Download URL: https://zenodo.org/api/records/18806107/files
- Local path: `CASE/2026-05-11-heartbeat-0222Z/artifacts/zenodo-18806107/`
- Why selected:
  - Contains explicit HYSYS model file `7. Sistema Integrado OCC,ASU,CCS.hsc`
  - Includes paired engineering spreadsheets and calculation files for cross-validation context
  - Clear DOI-backed source with public access and CC-BY-4.0 license
- License/public access note: Open access, CC-BY-4.0, DOI `10.5281/zenodo.18806107`
- Recommended automation uses:
  - HYSYS model ingestion regression
  - COM automation smoke tests (open/read/introspection only)
  - Sensitivity/optimization scaffolding with spreadsheet-linked parameters
- Dedupe basis:
  - `source_page`/`download_url` not present in existing CASE sources
  - `.hsc` filename and SHA256 do not match previous CASE artifacts

## Candidate Records (Not promoted to benchmark this run)

### A) Hydrogen Co-Firing in Gas Turbines... (Zenodo 19469917)
- Quality: **D** (candidate-only)
- Source page: https://zenodo.org/records/19469917
- Download URL: https://zenodo.org/api/records/19469917/files
- Local path: `CASE/2026-05-11-heartbeat-0222Z/artifacts/zenodo-19469917/`
- Static archive safety listing result:
  - RAR listing shows figures and spreadsheets only; no `.hsc` / HYSYS XML model file found
- Decision: keep as candidate evidence only, not promoted to benchmark case
- Residual risk: compressed package scope may be incomplete without deeper/manual inspection

### B) Aspen HYSYS model for the Tennessee Eastman process (Zenodo 10966344)
- Quality: **D** (candidate-only)
- Source page: https://zenodo.org/records/10966344
- Download URL: https://zenodo.org/api/records/10966344/files
- Local path: `CASE/2026-05-11-heartbeat-0222Z/artifacts/zenodo-10966344-candidate/record-10966344.json`
- Decision: metadata only, model file not downloaded this run
- Reason:
  - License is `CC-BY-NC-ND-4.0`; redistribution into public mixed-use benchmark repo needs maintainer/legal confirmation

## Security and Handling Notes
- No `.exe`, macros, scripts, or binaries from downloaded archives were executed.
- Archive handling was static (download + hash + safe listing only).
- No HYSYS runtime opening/solving was performed; no solver validation claim is made.

## Residual Risks
- Only one newly confirmed high-quality HYSYS model case was added this run.
- Some promising records are blocked by licensing ambiguity or missing model evidence in archive listing.
- Model compatibility with local Aspen HYSYS version remains unverified.

## Next Suggestions
1. Prioritize additional open-license (`CC-BY`/MIT) records with explicit `.hsc` file manifests.
2. Add a tiny manifest scanner that rejects candidate archives lacking `.hsc/.xml` in listing stage.
3. For `CC-BY-NC-ND` candidates, open a maintainer decision issue on redistribution policy.

# Aspen HYSYS CASE Heartbeat - 2026-05-11-0026Z

## Run Metadata
- Run time (UTC): 2026-05-11T00:33:08Z
- Heartbeat folder: `CASE/2026-05-11-heartbeat-0026Z`
- Search mines used: Zenodo, GitHub, targeted Zenodo restricted-candidate check
- Keywords used: `Aspen HYSYS case file`, `Aspen HYSYS .hsc`, `HYSYS XML cases`, `supplementary material`, `process simulation`, `model validation`, `Excel data`

## Downloaded Cases (Non-duplicate)

### 1) Zenodo 14882867 - Onboard carbon capture for circular marine fuels
- Quality: A
- Source page: https://zenodo.org/records/14882867
- Download API: https://zenodo.org/api/records/14882867/files
- Local path: `CASE/2026-05-11-heartbeat-0026Z/artifacts/zenodo-14882867/`
- Selection rationale: Open-access DOI dataset with multiple `.hsc` files + supporting Excel + explicit publication linkage.
- License/public access: `access_right=open`, license `cc-by-4.0` in record metadata.
- Recommended automation uses:
  - HYSYS case loading and parsing smoke tests
  - Parameter/sensitivity scaffolding from paired spreadsheet data
  - Baseline for CO2 capture / marine-fuel workflows
- Dedupe basis:
  - No matching `source_page` or `download_url` found in existing CASE assets.
  - No filename collision against existing CASE files.
  - New SHA256 set does not match previously stored CASE community sample hashes.

### 2) GitHub andr1976/dwsim-paper - HYSYS + DWSIM comparative package
- Quality: B
- Source page: https://github.com/andr1976/dwsim-paper
- Download URL: https://codeload.github.com/andr1976/dwsim-paper/zip/refs/heads/main
- Local path: `CASE/2026-05-11-heartbeat-0026Z/artifacts/github-andr1976-dwsim-paper/`
- Selection rationale: Public repository includes two `.hsc` files, matching `.xml` exports, automation scripts, CSV results, README, and MIT license.
- License/public access: MIT license included in repository snapshot.
- Recommended automation uses:
  - HYSYS case mutation + script automation regression
  - HYSYS-vs-DWSIM cross-tool benchmark harness
  - CSV-based output validation fixtures
- Dedupe basis:
  - Existing CASE only had `Test_1.hsc` from a different repository; no overlapping filenames or hashes.

## Candidate Not Downloaded

### Zenodo 15338007 - Flexible DME design/optimization software package
- Quality: D (candidate only)
- Source page: https://zenodo.org/records/15338007
- Download endpoint checked: https://zenodo.org/api/records/15338007/files
- Result: metadata accessible, but `access_right=restricted`, anonymous file list empty.
- Action: recorded metadata only (`artifacts/zenodo-15338007-metadata.json`), no package download.
- Follow-up: manual permission request needed before archival ingestion.

## Residual Risks
- No HYSYS runtime execution was performed; all model run statuses remain `not_run`.
- Downloaded archives were not executed (no scripts/macros/binaries run), only stored and hashed.
- Mixed-simulator repositories require downstream filtering to avoid accidental non-HYSYS ingestion.

## Next Suggestions
1. Add a lightweight parser check that inventories only `.hsc/.xml` and rejects unsupported binaries.
2. Prioritize next heartbeat on Zenodo/Figshare records with open file manifests containing `.hsc`.
3. For restricted candidates, track author contact workflow and legal/access decision log.

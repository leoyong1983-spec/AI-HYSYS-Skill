# CASE Heartbeat 2026-05-11-1057Z

## Run Metadata
- Run UTC time: 2026-05-11T11:00:04Z
- Heartbeat folder: CASE/2026-05-11-heartbeat-1057Z
- Artifact directory: CASE/2026-05-11-heartbeat-1057Z/artifacts
- Repository gate: git repo=true, branch=main, git pull --ff-only origin main succeeded.

## Search Mines Covered (Priority First)
1. GitHub public repositories (high-signal filtering): license-aware repository search + file-tree inspection for .hsc and automation assets.
2. Zenodo structured query checks for Aspen HYSYS datasets/supplementary packages (no new non-duplicate download candidate passing quality/licensing threshold this run).
3. Figshare API scan for Aspen HYSYS terms and attached files (no new confirmed .hsc/.xml package beyond previously indexed records).

## Query Keywords Used
- "Aspen HYSYS" "case file"
- "Aspen HYSYS" ".hsc"
- "HYSYS XML Cases" ".xml"
- "Aspen HYSYS" supplementary material
- extension:hsc "Aspen HYSYS" (conceptual GitHub advanced search, implemented via repository/tree API due unauthenticated code-search limits)
- Aspen HYSYS in:name,description,readme
- HYSYS simulation in:name,description,readme

## Downloaded Cases (Non-duplicate)
1. **Aspen HYSYS Python Spreadsheet Connection Test Case (GitHub)**
- Quality: **B**
- Source page: https://github.com/edgarsmdn/Aspen_HYSYS_Python
- Download URL: https://codeload.github.com/edgarsmdn/Aspen_HYSYS_Python/zip/refs/heads/main
- Local path: CASE/2026-05-11-heartbeat-1057Z/artifacts/Aspen_HYSYS_Python-main.zip and extracted companion files under .../Aspen_HYSYS_Python-main/
- Why selected: includes .hsc model (Test_1.hsc), Python automation scripts, README, and MIT license.
- License/public-access note: MIT license in repo; public download without login.
- Recommended automation use: spreadsheet-link COM automation smoke tests and solver-toggle interaction regression.
- Dedupe basis: new source_page, new download_url, new SHA256 set, filenames not present in previous sources.json indices.

2. **ap-python Aspen HYSYS Automation Test Case (GitHub)**
- Quality: **B**
- Source page: https://github.com/bsha0/ap-python
- Download URL: https://codeload.github.com/bsha0/ap-python/zip/refs/heads/master
- Local path: CASE/2026-05-11-heartbeat-1057Z/artifacts/ap-python-master.zip and extracted companion files under .../ap-python-master/
- Why selected: includes .hsc test case (Atmospheric Crude Tower.hsc), explicit HYSYS automation scripts, README, and MIT license.
- License/public-access note: MIT license in repo; public download without login.
- Recommended automation use: COM variable-path read/write regression and open/save path validation for test harnesses.
- Dedupe basis: new source_page, new download_url, new SHA256 set, filenames not present in previous sources.json indices.

## Candidate-only Records (Not Downloaded)
1. https://github.com/ArturTask/HysysExcel (Quality D)
- Reason not downloaded: no explicit license file detected; redistribution/archive rights unclear.

2. https://github.com/guillemrh/TFG (Quality D)
- Reason not downloaded: no explicit license file detected; redistribution/archive rights unclear.

3. https://github.com/afabrild/HYSYS-MATLAB-LINK (Quality D)
- Reason not downloaded: no explicit license file detected; redistribution/archive rights unclear.

## Dedupe Method Used
- Loaded all existing CASE/**/sources.json and compared these keys before download:
  - source_page
  - download_url
  - 	itle
  - local_artifacts[].filename
  - local_artifacts[].sha256
- Existing baseline before this run: 15 unique source pages / 15 unique download URLs / 87 filenames / 88 SHA256 values.

## Residual Risks
- No local Aspen HYSYS execution was performed; all models remain model_run_status=not_run.
- GitHub unauthenticated code-search endpoint returned 401 and later API rate limiting occurred; repository/tree endpoint evidence was used as fallback.
- Downloaded archives include script files (.py, .bat) and binary data; files were inventoried and hashed but not executed.

## Next Suggestions
1. Re-run with authenticated GitHub token (higher API limits) to widen license-aware mining.
2. Expand to OSF/Dataverse with metadata-first screening for explicit open licenses and attached .hsc/.xml.
3. If maintainer approves, contact candidate repo authors for explicit licensing to unlock additional D->B/C promotions.

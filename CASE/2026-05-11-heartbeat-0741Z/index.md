# Aspen HYSYS CASE Discovery Index

## Run Metadata
- run_utc: 2026-05-11T07:51:12Z
- run_local: 2026-05-11T15:51:12+08:00
- heartbeat_folder: `CASE/2026-05-11-heartbeat-0741Z`
- artifacts_dir: `CASE/2026-05-11-heartbeat-0741Z/artifacts`
- agent_mode: Discovery & Fetch (no local HYSYS execution)

## Mining Zones Queried
1. GitHub public repositories and codeload archives (priority high-quality source used this run).
2. Zenodo API and web search were attempted; endpoints were unstable/timeouts in this run and not used for final downloads.
3. Candidate-only checks for public HYSYS-related repositories with/without explicit license.

## Keywords Used
- `Aspen HYSYS`
- `extension:hsc`
- `HYSYS case`
- `natural gas sweetening`
- `CDU simulation`
- `pressure drop`
- `README license`

## Downloaded Cases (3)

### 1) Pressure Drop Estimation in Pipelines (GitHub)
- quality: **B**
- source_page: https://github.com/kavinrajachakravarthy/Pressure-Drop-Estimation-in-Pipelines
- download_url: https://codeload.github.com/kavinrajachakravarthy/Pressure-Drop-Estimation-in-Pipelines/zip/refs/heads/main
- local_path:
  - `CASE/2026-05-11-heartbeat-0741Z/artifacts/Pressure-Drop-Estimation-in-Pipelines-main.zip`
  - `CASE/2026-05-11-heartbeat-0741Z/artifacts/Pressure-Drop-Estimation-in-Pipelines-main/`
- selected_because:
  - Contains HYSYS case (`.hsc`) plus report, Excel, Python, MATLAB counterparts for cross-tool validation.
  - MIT license present with public repo access.
- license_public_access_note: MIT license in repository; public access without login.
- recommended_automation_use: Pipeline pressure-drop regression tests, I/O parsing checks, and cross-solver benchmark baselines.

### 2) Natural Gas Sweetening — DEA Absorption Simulation (GitHub)
- quality: **B**
- source_page: https://github.com/shahria-sunny/Natural-Gas-Sweetening
- download_url: https://codeload.github.com/shahria-sunny/Natural-Gas-Sweetening/zip/refs/heads/main
- local_path:
  - `CASE/2026-05-11-heartbeat-0741Z/artifacts/Natural-Gas-Sweetening-main.zip`
  - `CASE/2026-05-11-heartbeat-0741Z/artifacts/Natural-Gas-Sweetening-main/`
- selected_because:
  - Direct `.hsc` with process report and detailed README (states Aspen HYSYS V14).
  - Priority domain match: natural gas sweetening / acid gas removal.
  - MIT license present with public repo access.
- license_public_access_note: MIT license in repository; public access without login.
- recommended_automation_use: Absorber-regenerator automation smoke tests, parameter sweeps, and convergence guardrail tests.

### 3) Crude Oil Atmospheric Distillation: Simulation & Energy Optimization (GitHub)
- quality: **B**
- source_page: https://github.com/shahria-sunny/CDU-Simulation-Optimization
- download_url: https://codeload.github.com/shahria-sunny/CDU-Simulation-Optimization/zip/refs/heads/main
- local_path:
  - `CASE/2026-05-11-heartbeat-0741Z/artifacts/CDU-Simulation-Optimization-main.zip`
  - `CASE/2026-05-11-heartbeat-0741Z/artifacts/CDU-Simulation-Optimization-main/`
- selected_because:
  - Contains `.hsc` and report with explicit HYSYS version mention in README.
  - Useful for distillation and energy optimization benchmarking.
  - MIT license present with public repo access.
- license_public_access_note: MIT license in repository; public access without login.
- recommended_automation_use: Distillation benchmark for optimization loops and report extraction checks.

## Safety Check (Archive Inspection)
- compressed packages inspected by extension and listing only.
- no `.exe`, `.dll`, macro-enabled office files, or runnable binary payloads were executed.
- no HYSYS model was opened or solved in this run.

## Deduplication Basis
- Existing dedupe universe loaded from all historical `CASE/**/sources.json`.
- Checked keys: `source_page`, `download_url`, `title`, per-file `filename`, per-file `sha256`.
- Result:
  - `source_page` duplicates: none.
  - `download_url` duplicates: none.
  - `title` duplicates: none.
  - Common generic filenames (e.g., `README.md`, `LICENSE`) appeared across repos but were not treated as duplicates without matching source/download/sha context.

## Candidate-Only / Skipped Items
- `https://github.com/snua/HYSYS-dynamic-simulation`
  - reason_not_downloaded: repository contains `solutions.rar` and no explicit license metadata; redistribution/archival permission is unclear.
- `https://github.com/GaboTalero/HYSYS-Python-Case-Builder`
  - reason_not_downloaded: no `.hsc/.xml` case file found; scripts-only package.

## Residual Risks
- Case files were not executed in Aspen HYSYS in this run, so numerical convergence and solver status are unverified.
- README claims and report values were not independently recalculated.
- GitHub repos can change over time; this run archived point-in-time zip snapshots and SHA256 hashes to mitigate drift.

## Next-Step Suggestions
1. Prioritize next run on Zenodo/Figshare records with explicit downloadable `.hsc/.xml` in API file list and DOI metadata.
2. Add optional `license gate` policy flag: auto-skip repositories without explicit open license for archive redistribution.
3. Add lightweight parser check that confirms at least one `.hsc` is present before download to reduce candidate churn.

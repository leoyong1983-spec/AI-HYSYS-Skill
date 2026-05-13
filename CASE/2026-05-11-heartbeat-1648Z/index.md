# Aspen HYSYS CASE Heartbeat - 2026-05-11-1648Z

## Run Metadata
- Run time (UTC): 2026-05-11T16:48:47Z
- Heartbeat folder: `CASE/2026-05-11-heartbeat-1648Z`
- Search mines: Zenodo API, GitHub repository API, Mendeley/OSF/Figshare targeted web probes
- Keywords: `Aspen HYSYS case file`, `Aspen HYSYS .hsc`, `HYSYS XML`, `supplementary material`, `model validation`, `Excel data`, `process simulation`

## Downloaded Cases
- New A/B/C cases downloaded this run: 0
- Reason: no new non-duplicate package met both model-file and license/public-archive safety constraints.

## Candidate Records (Not Downloaded as CASE Packages)

### 1) iraola/tennessee-eastman-hysys
- Quality: D (license-boundary candidate)
- Source page: https://github.com/iraola/tennessee-eastman-hysys
- Download URL (not executed for full package): https://codeload.github.com/iraola/tennessee-eastman-hysys/zip/refs/heads/main
- Evidence saved: `artifacts/github-iraola-tennessee-eastman-hysys/` (`repo.json`, `tree.json`, `README.md`, `LICENSE`)
- Why not downloaded: contains `.HSC`, but LICENSE is CC BY-NC-ND 4.0; redistribution boundary needs manual policy decision for this open benchmark repo.
- Recommended use: legal review first; keep as metadata pointer candidate.

### 2) GaboTalero/HYSYS-Python-Case-Builder
- Quality: D (no model file candidate)
- Source page: https://github.com/GaboTalero/HYSYS-Python-Case-Builder
- Download URL (not executed for full package): https://codeload.github.com/GaboTalero/HYSYS-Python-Case-Builder/zip/refs/heads/main
- Evidence saved: `artifacts/github-GaboTalero-HYSYS-Python-Case-Builder/` (`repo.json`, `tree.json`, `README.md`, `LICENSE`)
- Why not downloaded: MIT license is permissive, but repository tree shows scripts only and no `.hsc/.xml` case file.
- Recommended use: automation script reference only.

### 3) Galigeigei-Z/HDA-Surrogate-Optimization
- Quality: D (interface demo candidate)
- Source page: https://github.com/Galigeigei-Z/HDA-Surrogate-Optimization
- Download URL (not executed for full package): https://codeload.github.com/Galigeigei-Z/HDA-Surrogate-Optimization/zip/refs/heads/main
- Evidence saved: `artifacts/github-Galigeigei-Z-HDA-Surrogate-Optimization/` (`repo.json`, `tree.json`, `README.md`, `LICENSE`)
- Why not downloaded: MIT license is permissive, but no `.hsc/.xml` in repository tree (code + workbook demo only).
- Recommended use: COM/workbook scaffold reference, not baseline case asset.

## Dedupe Basis
- Loaded and checked all existing `CASE/*/sources.json`.
- Existing known sources from prior runs (Zenodo 14882867/18806107/10966344, Figshare 25202060, multiple GitHub repositories) were not re-downloaded.
- This run only recorded new source pages not previously indexed, and only metadata evidence files were stored.

## Residual Risks
- No new benchmark-grade package was added; case corpus growth paused this run.
- Candidate-1 license interpretation (NC-ND) may require legal/policy confirmation before any artifact ingestion.
- No HYSYS runtime execution performed.

## Next Suggestions
1. Add a policy whitelist/blacklist for acceptable licenses (`MIT`, `BSD`, `Apache-2.0`, `CC-BY`) to automate candidate filtering.
2. Prioritize direct outreach or issue requests to script-only repos asking maintainers to publish minimal `.hsc` cases.
3. Continue high-yield mining on Zenodo/Figshare only when API file manifests explicitly expose `.hsc/.xml`.

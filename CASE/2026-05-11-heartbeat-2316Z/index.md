# Aspen HYSYS CASE Heartbeat - 2026-05-11-2316Z

## Run Metadata
- Run time (UTC): 2026-05-11T23:16:46Z
- Heartbeat folder: `CASE/2026-05-11-heartbeat-2316Z`
- Search mines: Zenodo API, GitHub repository API, Figshare API, Mendeley/OSF/Dataverse targeted probes
- Keywords: `Aspen HYSYS case file`, `Aspen HYSYS .hsc`, `HYSYS XML Cases`, `supplementary material`, `process simulation`, `model validation`, `Excel data`, `flowsheet`

## Downloaded Cases
- New A/B/C cases downloaded this run: 0
- Cause: no newly discovered non-duplicate source simultaneously satisfied `public model artifact (.hsc/.xml)` and `archive-safe license clarity`.

## Dedupe Findings (Before Download)
- Existing CASE index/sources baseline loaded from all prior heartbeat folders.
- Zenodo `hysys` mining returned only previously indexed records and was skipped as duplicate source pages:
  - `https://zenodo.org/records/18806107`
  - `https://zenodo.org/records/14882867`
  - `https://zenodo.org/records/10966344`
- No duplicate downloads were performed.

## Candidate Records (Not Downloaded)

### 1) oscarcontrerasnavas/hysys-to-excel-intro
- Quality: D
- Source page: https://github.com/oscarcontrerasnavas/hysys-to-excel-intro
- Download URL (not executed for full package): https://codeload.github.com/oscarcontrerasnavas/hysys-to-excel-intro/zip/refs/heads/master
- Local metadata evidence: `artifacts/github-oscarcontrerasnavas-hysys-to-excel-intro/`
- Selection reason: public repo, explicit HYSYS-Excel bridge context.
- Why not downloaded: no `.hsc/.xml` case file in repo tree; only `.xlsm` + script.
- License/public access note: GPL-3.0, public repository.
- Recommended automation use: Excel bridge pattern reference only.

### 2) perrywzm/hysysopt
- Quality: D
- Source page: https://github.com/perrywzm/hysysopt
- Download URL (not executed for full package): https://codeload.github.com/perrywzm/hysysopt/zip/refs/heads/master
- Local metadata evidence: `artifacts/github-perrywzm-hysysopt/`
- Selection reason: HYSYS optimization framework context.
- Why not downloaded: no `.hsc/.xml` model assets; license not declared.
- License/public access note: public repo, SPDX unknown.
- Recommended automation use: optimization wrapper design reference.

### 3) aqiqiqiu/ai-hysys-autobuilder
- Quality: D
- Source page: https://github.com/aqiqiqiu/ai-hysys-autobuilder
- Download URL (not executed for full package): https://codeload.github.com/aqiqiqiu/ai-hysys-autobuilder/zip/refs/heads/dryrun
- Local metadata evidence: `artifacts/github-aqiqiqiu-ai-hysys-autobuilder/`
- Selection reason: active HYSYS COM automation implementation.
- Why not downloaded: no `.hsc/.xml` model files in tree.
- License/public access note: MIT.
- Recommended automation use: script architecture reference, not case corpus source.

## Residual Risks
- Case corpus did not expand this run because candidate quality/license/model-file constraints were not met.
- No HYSYS runtime verification was performed; all statuses remain `not_run`.

## Next Suggestions
1. Continue hourly sweep with stricter first-pass filter: only sources exposing `.hsc/.xml` in file manifest.
2. Add license acceptance policy gates (`MIT/BSD/Apache/CC-BY`) before download stage.
3. For script-only repositories, track as tooling references and request maintainers to publish minimal public case files.

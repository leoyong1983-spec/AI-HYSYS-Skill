# CASE Heartbeat 2026-05-14 2107Z

## 1. Run Time

- Trigger time (UTC): 2026-05-14T21:07:12.138Z
- Local repository: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-14-heartbeat-2107Z
- Model execution status: not_run for all entries. No Aspen HYSYS case was opened, executed, or solved.

## 2. Searched Mine Areas

- GitHub-first license-filtered repository search: HYSYS with MIT/GPL-3.0/Apache-2.0 filters and Aspen HYSYS GPL filter.
- GitHub tree inspection for licensed hits and name-collision candidates.
- Zenodo API targeted search for Aspen HYSYS license/HSC/black-oil/DWSIM terms.
- No login-gated, paid, customer-support, institutional, private training, executable, macro, or unknown binary payload was used.

## 3. Keywords Used

- `HYSYS license:gpl-3.0`
- `HYSYS license:mit`
- `HYSYS license:apache-2.0`
- `Aspen HYSYS license:gpl-3.0`
- `"Aspen HYSYS" "MIT" ".hsc"`
- `"Aspen HYSYS" "black oil"`
- `"Aspen HYSYS" "DWSIM"`
- `"HYSYS" "case" "license"`

## 4. Downloaded Case List

No new high-quality, non-duplicate Aspen HYSYS case file was downloaded in this heartbeat.

Reason: the best licensed HYSYS model hits, `andr1976/dwsim-paper` and `tinchofiuba/pythonHysys`, are already archived in prior CASE folders. Other licensed hits did not contain qualifying HYSYS case files.

## 5. Candidate And Duplicate Findings

| Title | Source page | Download URL | Local path | Reason | Quality | License / public access | Recommended use | Dedupe basis | Residual risk |
|---|---|---|---|---|---|---|---|---|---|
| Duplicate: andr1976/dwsim-paper | https://github.com/andr1976/dwsim-paper | Not downloaded this run | artifacts/github-andr1976__dwsim-paper-* | MIT repository with HYSYS cases, data, paper, and scripts, already archived in CASE/2026-05-11-heartbeat-0026Z. | D | MIT; duplicate of existing archive. | Use existing archive for HYSYS-vs-DWSIM comparisons. | source_page, filenames, prior archive. | Re-downloading would duplicate existing assets. |
| Duplicate: tinchofiuba/pythonHysys | https://github.com/tinchofiuba/pythonHysys | Not downloaded this run | artifacts/github-tinchofiuba__pythonHysys-* | MIT repository with HYSYS cases and Python access code, already archived in CASE/2026-05-11-heartbeat-2213Z. | D | MIT; duplicate of existing archive. | Use existing archive for Python-HYSYS access tests. | source_page, filenames, prior archive. | Re-downloading would duplicate existing assets. |
| YuniqueCore/DynPlots | https://github.com/YuniqueCore/DynPlots | Not downloaded | artifacts/github-YuniqueCore__DynPlots-* | MIT HYSYS dump plotting tool, no Aspen HYSYS case file. | D | MIT; no model payload. | Post-processing reference only. | source_page, metadata SHA256. | Not a benchmark case. |
| aqiqiqiu/ai-hysys-autobuilder | https://github.com/aqiqiqiu/ai-hysys-autobuilder | Not downloaded | artifacts/github-aqiqiqiu__ai-hysys-autobuilder-* | MIT automation code, no model file; already triaged previously. | D | MIT; no model payload. | COM automation pattern reference only. | source_page, metadata SHA256. | Not a benchmark case. |
| naawu789/HySysID | https://github.com/naawu789/HySysID | Not downloaded | artifacts/github-naawu789__HySysID-* | MIT name collision/system-identification material, no Aspen HYSYS evidence. | D | MIT; no model payload. | No HYSYS benchmark use. | source_page, metadata SHA256. | Name collision. |
| stonedingwt/HYSys | https://github.com/stonedingwt/HYSys | Not downloaded | artifacts/github-stonedingwt__HYSys-* | Apache-2.0 name collision, large UI/source tree, no Aspen HYSYS model file. | D | Apache-2.0; no model payload. | Suppress as name collision. | source_page, metadata SHA256. | Not a benchmark case. |
| punkeel/HySystemdNotifier | https://github.com/punkeel/HySystemdNotifier | Not downloaded | artifacts/github-punkeel__HySystemdNotifier-* | GPL-3.0 systemd notifier, no Aspen HYSYS model file. | D | GPL-3.0; no model payload. | Suppress as name collision. | source_page, metadata SHA256. | Not a benchmark case. |
| GitHub license-filter sweep | https://github.com/search?q=HYSYS+license&type=repositories | Not downloaded | artifacts/github-search-* | No new licensed, non-duplicate HYSYS model payload found. | D | Search metadata only. | Query audit evidence. | artifact SHA256. | GitHub search is not exhaustive for binaries. |
| Zenodo license-targeted sweep | https://zenodo.org/search?q=Aspen%20HYSYS%20license%20hsc | Not downloaded | artifacts/zenodo-license-targeted-search-results.json | Known duplicates or non-model records. | D | Search metadata only; individual records vary. | Duplicate-control evidence. | artifact SHA256. | Search aggregate contains false positives. |

## 6. Structured Source File

See `sources.json` in this folder for SHA256 values and machine-readable metadata.

## 7. Follow-Up Recommendations

- Add `andr1976/dwsim-paper` and `tinchofiuba/pythonHysys` to a high-confidence duplicate allowlist so future heartbeats do not re-evaluate them as possible downloads.
- Treat `stonedingwt/HYSys`, `punkeel/HySystemdNotifier`, and `naawu789/HySysID` as name collisions unless their trees later add Aspen HYSYS model files.
- Continue license-filtered GitHub search, but suppress already-archived MIT/GPL model repositories before tree inspection.

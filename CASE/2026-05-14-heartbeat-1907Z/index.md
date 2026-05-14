# CASE Heartbeat 2026-05-14 1907Z

## 1. Run Time

- Trigger time (UTC): 2026-05-14T19:07:10.263Z
- Local repository: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-14-heartbeat-1907Z
- Model execution status: not_run for all entries. No Aspen HYSYS case was opened, executed, or solved.

## 2. Searched Mine Areas

- GitHub-first repository search: HYSYS case, Aspen HYSYS case file, HYSYS COM, HYSYS MATLAB, HYSYS optimization, HYSYS license:mit.
- GitHub tree inspection for six code/document candidates surfaced by repository search.
- Zenodo API targeted search for case-file, supplementary-material, LNG, and methanol combinations.
- No login-gated, paid, customer-support, institutional, private training, executable, or unknown binary payload was used.

## 3. Keywords Used

- `HYSYS case`
- `Aspen HYSYS case file`
- `HYSYS COM`
- `HYSYS MATLAB`
- `HYSYS optimization`
- `HYSYS license:mit`
- `"Aspen HYSYS" "case file"`
- `"Aspen HYSYS" "supplementary material" ".hsc"`
- `"Aspen HYSYS" "LNG" "supplementary"`
- `"Aspen HYSYS" "methanol" "supplementary"`

## 4. Downloaded Case List

No new high-quality, non-duplicate Aspen HYSYS case file was downloaded in this heartbeat.

Reason: inspected GitHub candidates were code/document resources without HYSYS model files, and model-bearing candidates found in prior runs were already recorded or blocked by missing licenses.

## 5. Candidate And Duplicate Findings

| Title | Source page | Download URL | Local path | Reason | Quality | License / public access | Recommended use | Dedupe basis | Residual risk |
|---|---|---|---|---|---|---|---|---|---|
| pSantosb/Hysys-connection-Excel-Matlab-Python-Unity | https://github.com/pSantosb/Hysys-connection-Excel-Matlab-Python-Unity | Not downloaded | artifacts/github-pSantosb__Hysys-connection-Excel-Matlab-Python-Unity-* | Multi-language HYSYS connection scripts, but no model file and no explicit license. | D | Public metadata only; no license detected. | Automation pattern reference after manual license review. | source_page, metadata SHA256. | Not a benchmark case. |
| snua/HYSYS-dynamic-simulation | https://github.com/snua/HYSYS-dynamic-simulation | Not downloaded | artifacts/github-snua__HYSYS-dynamic-simulation-* | Slides/worksheet only; no model file and no explicit license. | D | Public metadata only; no license detected. | Dynamic-simulation teaching reference if license clarified. | source_page, metadata SHA256. | Not a benchmark case. |
| sajjad-ah/ASPEN-HYSYS | https://github.com/sajjad-ah/ASPEN-HYSYS | Not downloaded | artifacts/github-sajjad-ah__ASPEN-HYSYS-* | Automation/PDF material, but no HYSYS model file and no explicit license. | D | Public metadata only; no license detected. | Script idea reference after manual review. | source_page, metadata SHA256. | Not a benchmark case. |
| cityfamer/HyPy | https://github.com/cityfamer/HyPy | Not downloaded | artifacts/github-cityfamer__HyPy-* | Python wrapper skeleton only; no model file and no explicit license. | D | Public metadata only; no license detected. | API-wrapper pattern reference only. | source_page, metadata SHA256. | Not a benchmark case. |
| DanielVazVaz/PySIS | https://github.com/DanielVazVaz/PySIS | Not downloaded | artifacts/github-DanielVazVaz__PySIS-* | Python abstraction/docs only; no model file and no explicit license. | D | Public metadata only; no license detected. | API abstraction reference only. | source_page, metadata SHA256. | Not a benchmark case. |
| robfox92/matlab-fitness-hysys | https://github.com/robfox92/matlab-fitness-hysys | Not downloaded | artifacts/github-robfox92__matlab-fitness-hysys-* | MATLAB optimization README only; no model file and no explicit license. | D | Public metadata only; no license detected. | MATLAB optimization coupling lead only. | source_page, metadata SHA256. | Not a benchmark case. |
| GitHub search sweep | https://github.com/search?q=HYSYS&type=repositories | Not downloaded | artifacts/github-search-* | Search found no new licensed, non-duplicate HYSYS model repository. | D | Search metadata only. | Query audit evidence. | artifact SHA256. | GitHub search is not exhaustive for binaries. |
| Zenodo targeted search sweep | https://zenodo.org/search?q=Aspen%20HYSYS%20case%20file | Not downloaded | artifacts/zenodo-targeted-search-results.json | Known duplicates or non-model records; no new HYSYS model payload. | D | Search metadata only; individual records vary. | Duplicate-control evidence. | artifact SHA256, known DOI/source pages. | Search aggregate contains false positives. |

## 6. Structured Source File

See `sources.json` in this folder for SHA256 values and machine-readable metadata.

## 7. Follow-Up Recommendations

- Avoid re-recording previously known unlicensed HSC repositories unless their license state changes.
- Add an automated prior-source filter before candidate emission so repeated no-license repositories are suppressed earlier.
- Keep GitHub-first search, but require `tree` evidence of `.hsc`, `.hscz`, HYSYS XML, or `.compound` before considering payload download.
- Continue checking Zenodo for new versions of known DOI-backed records rather than redownloading duplicates.

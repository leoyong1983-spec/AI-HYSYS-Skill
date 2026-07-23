# CASE Heartbeat 2026-05-14 2007Z

## 1. Run Time

- Trigger time (UTC): 2026-05-14T20:07:11.182Z
- Local repository: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-14-heartbeat-2007Z
- Model execution status: not_run for all entries. No Aspen HYSYS case was opened, executed, or solved.

## 2. Searched Mine Areas

- GitHub-first repository search: broad HYSYS and Aspen-HYSYS queries plus license-filtered searches.
- GitHub tree inspection for candidate repositories surfaced by broad search.
- GitLab project search API and Bitbucket repository API probes.
- Zenodo API targeted search for Aspen HYSYS case/supplementary/HSC terms.
- No login-gated, paid, customer-support, institutional, private training, executable, macro, or unknown binary payload was used.

## 3. Keywords Used

- `HYSYS`
- `Aspen-HYSYS`
- `HYSYS license:mit`
- `HYSYS license:gpl-3.0`
- `"Aspen HYSYS" "case file"`
- `"Aspen HYSYS" ".hsc"`
- `"HYSYS simulation" "optimization"`
- `"Aspen HYSYS" "supplementary" "case"`

## 4. Downloaded Case List

No new high-quality, non-duplicate Aspen HYSYS case file was downloaded in this heartbeat.

Reason: new HSC-bearing GitHub candidates lacked explicit license; the licensed HSC-bearing GitHub hit was already archived; GitLab/Bitbucket API probes did not yield accessible downloadable model targets; Zenodo returned known duplicates or non-model records.

## 5. Candidate And Duplicate Findings

| Title | Source page | Download URL | Local path | Reason | Quality | License / public access | Recommended use | Dedupe basis | Residual risk |
|---|---|---|---|---|---|---|---|---|---|
| IcedCoffeeBoy/PSO_hysys_optimisation | https://github.com/IcedCoffeeBoy/PSO_hysys_optimisation | Not downloaded | artifacts/github-IcedCoffeeBoy__PSO_hysys_optimisation-* | Contains `PG_separation_Optimisation_Sample.hsc` and PSO scripts, but no explicit license. | D | Public metadata only; no license detected. | Manual permission candidate for HYSYS PSO optimization tests. | source_page, filename, metadata SHA256. | Cannot archive model without license/author permission. |
| theodoreOnzGit/hysys-tutorials | https://github.com/theodoreOnzGit/hysys-tutorials | Not downloaded | artifacts/github-theodoreOnzGit__hysys-tutorials-* | Contains many `.hsc` tutorial files and an Excel workbook, but no explicit license. | D | Public metadata only; no license detected. | Manual permission candidate for tutorial-scale HEN/fuel-cell examples. | source_page, representative filenames, metadata SHA256. | Cannot archive model without license/author permission. |
| may3rd/COSMO | https://github.com/may3rd/COSMO | Not downloaded this run | artifacts/github-may3rd__COSMO-* | GPL-3.0 repository with `Test_1.hsc`, but already archived in earlier CASE runs. | D | GPL-3.0; duplicate of existing archive. | Use existing archived COSMO/Test_1.hsc for optimization tests. | source_page, filename, prior archive. | Re-downloading would duplicate existing CASE assets. |
| SuradechKKPB/AutomatedHYSYS | https://github.com/SuradechKKPB/AutomatedHYSYS | Not downloaded | artifacts/github-SuradechKKPB__AutomatedHYSYS-* | Automation scripts only; no model file and no explicit license. | D | Public metadata only; no license detected. | Automation pattern reference only. | source_page, metadata SHA256. | Not a benchmark case. |
| bobpullem/C-Python-and-HYSYS | https://github.com/bobpullem/C-Python-and-HYSYS | Not downloaded | artifacts/github-bobpullem__C-Python-and-HYSYS-* | C#/Python optimization scripts only; no model file and no explicit license. | D | Public metadata only; no license detected. | GA/optimization pattern reference only. | source_page, metadata SHA256. | Not a benchmark case. |
| vminasid/Hysys-Unisis2Matlab | https://github.com/vminasid/Hysys-Unisis2Matlab | Not downloaded | artifacts/github-vminasid__Hysys-Unisis2Matlab-* | GPL-3.0 code with UniSim `.usc`, but no Aspen HYSYS model file. | D | GPL-3.0; not a HYSYS case payload. | UniSim/HYSYS-adjacent MATLAB optimization reference only. | source_page, metadata SHA256. | Not a HYSYS benchmark case. |
| GitHub broad search sweep | https://github.com/search?q=HYSYS&type=repositories | Not downloaded | artifacts/github-search-* | No new licensed non-duplicate HYSYS benchmark payload found. | D | Search metadata only. | Query audit evidence. | artifact SHA256. | GitHub search is not exhaustive for binaries. |
| GitLab/Bitbucket/Zenodo external sweep | multiple external search APIs | Not downloaded | artifacts/gitlab-*, artifacts/bitbucket-*, artifacts/zenodo-targeted-search-results.json | GitLab returned 401, Bitbucket returned 410, Zenodo had known duplicates/non-model records. | D | Search metadata only; individual records vary. | External sweep audit evidence. | artifact SHA256. | External API coverage incomplete. |

## 6. Structured Source File

See `sources.json` in this folder for SHA256 values and machine-readable metadata.

## 7. Follow-Up Recommendations

- Put `IcedCoffeeBoy/PSO_hysys_optimisation` and `theodoreOnzGit/hysys-tutorials` into the manual license/author-permission queue before any model payload download.
- Suppress already-known unlicensed or duplicate HSC repositories earlier in the heartbeat pipeline to reduce repeated candidate churn.
- Keep `may3rd/COSMO` as duplicate-only unless upstream publishes materially new model files.
- Revisit GitLab/Bitbucket with a different public search path if their APIs remain blocked.

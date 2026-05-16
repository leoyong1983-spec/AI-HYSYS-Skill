# Aspen HYSYS Case Discovery Heartbeat - 2026-05-16 1108Z

## Run Metadata

- Automation ID: ai-hysys-case-2
- Trigger time UTC: 2026-05-16T11:08:17.262Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Run directory: CASE/2026-05-16-heartbeat-1108Z
- Artifact directory: CASE/2026-05-16-heartbeat-1108Z/artifacts
- HYSYS model run status: not_run

## Repository Gate

- Confirmed Git repository on branch `main`.
- `git pull --ff-only origin main` completed successfully before the sweep.
- Only this run directory is intended for staging.

## Searched Mines

- GitHub repository search and code search, prioritized over other sources.
- GitLab and Bitbucket public search APIs.
- Zenodo, Figshare, Harvard Dataverse, and Mendeley/DataCite metadata searches.
- Candidate logic focused on public, attributable, non-duplicate resources with Aspen HYSYS `.hsc`, `.hscz`, HYSYS XML `.xml`, or `.compound` payloads.

## Keywords Used

- `extension:hsc HYSYS`
- `extension:hscz HYSYS`
- `extension:xml "Aspen HYSYS"`
- `"Aspen HYSYS" ".hsc"`
- `"Aspen HYSYS" ".hscz"`
- `"HYSYS XML Cases"`
- `"Aspen HYSYS" README`
- `"Aspen HYSYS" "case file"`
- `"Aspen HYSYS" "simulation files"`
- `"HYSYS" "MATLAB"`
- `"HYSYS" "Python COM"`
- `"HYSYS" "Excel" "validation"`

## Downloaded Case List

No new HYSYS model payload was downloaded or retained in this heartbeat.

The sweep found one new public GitHub candidate with a visible `.hsc` path, but the repository has no explicit license, so it was recorded as quality `D` and left for manual license review instead of being archived.

## Candidate Findings

| Title | Source page | Download URL / payload URL | Local evidence | Selection reason | Quality | License / access note | Recommended use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR candidate: `Project-PR/hyApp.hsc` | https://github.com/AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR | https://github.com/AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR/blob/main/Project-PR/hyApp.hsc | `artifacts/github-inspect-AtabakBahadornia__1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR.json` | Contains a visible `.hsc` case and MATLAB companion files for a supersonic separator workflow. | D | Public repo, but no license metadata or license file; not downloaded. | Manual permission/license review candidate for future HYSYS/MATLAB coupling benchmark. | Source page and filename were not present in prior source-page/title/file dedupe sets. | No reuse rights, unknown HYSYS version, minimal provenance. |
| GitHub duplicate and automation-reference sweep | https://github.com/search?q=Aspen+HYSYS+case+file&type=repositories | not_downloaded_duplicate_or_no_confirmed_model | `artifacts/github-inspected-repo-summary.json` | Rechecked known no-license `.hsc` repos and automation-only repos. | D | Public metadata only; license gaps or no model payload. | Search-filter tuning and duplicate avoidance. | Prior records already cover `afabrild/HYSYS-MATLAB-LINK`, `marcellobozzini/Python-Driving-License`, and automation references. | Some no-license cases may become usable only if permission is obtained later. |
| Zenodo targeted sweep: duplicates and no-model records | https://zenodo.org/search?q=%22Aspen%20HYSYS%22 | not_downloaded_duplicate_or_no_hysys_model | `artifacts/zenodo-1108-targeted-search-results.json` | Rechecked high-quality repository metadata; known HYSYS model records were duplicates and new hits lacked confirmed HYSYS model payloads. | D | Public metadata; duplicate records already archived or no model files confirmed. | Duplicate controls and no-model filter tuning. | Record IDs and filenames matched prior archive/no-model notes. | Archive contents can require manual review unless already inventoried. |
| Secondary platform sweep | multi_platform_targeted_search | not_downloaded_no_confirmed_hysys_model | Figshare, Dataverse, Mendeley/DataCite, GitLab, Bitbucket JSON artifacts | No confirmed downloadable HYSYS case payload. | D | Public search metadata only. | Improve platform-specific filters. | No download URL, SHA256, or filename met the HYSYS payload rule. | Search APIs may miss supplements exposed only through article landing pages. |

## Dedupe Summary

Existing CASE history read before this run:

- `sources.json` files: 32
- `index.md` files: 32
- Source entries: 165
- Known source pages: 113
- Known download URLs: 92
- Known titles: 223
- Known SHA256 hashes: 581
- Known filenames: 622
- Bad `sources.json` files: 0

## Safety Notes

- No `.hsc`, `.hscz`, `.compound`, archive, executable, macro-enabled workbook, or script payload was retained from external sources.
- Search and inspection artifacts are JSON metadata only.
- No HYSYS model was opened, loaded, run, or solved.
- No downloaded code, scripts, macros, notebooks, executables, or unknown binaries were run.

## Residual Risks

- The strongest new GitHub candidate lacks an explicit license, so it cannot be safely redistributed or archived without permission.
- GitHub code search returned XML keyword noise; no HYSYS XML case was confirmed.
- Public data repositories continue to surface records that mention Aspen HYSYS but do not include HYSYS case files.

## Follow-Up Recommendations

1. Manually contact or inspect `AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR` for licensing before any payload download.
2. Add a durable no-license candidate registry so repeated GitHub `.hsc` hits are suppressed before deep inspection.
3. Split GitHub search into two tiers: licensed repositories first, then no-license candidates only as metadata.
4. Add targeted searches for `filename:*.hsc` and `path:Project-PR` equivalents if GitHub search API quota allows.
5. Continue prioritizing GitHub, but keep Zenodo duplicate IDs as negative controls for the filter.

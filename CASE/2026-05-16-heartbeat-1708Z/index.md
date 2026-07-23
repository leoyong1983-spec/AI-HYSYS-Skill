# Aspen HYSYS Case Discovery Heartbeat - 2026-05-16 1708Z

## Run Metadata

- Automation ID: ai-hysys-case-2
- Trigger time UTC: 2026-05-16T17:08:29.396Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Run directory: CASE/2026-05-16-heartbeat-1708Z
- Artifact directory: CASE/2026-05-16-heartbeat-1708Z/artifacts
- HYSYS model run status: not_run

## Repository Gate

- Confirmed this directory is a Git repository on branch `main`.
- `git status` was clean before this heartbeat.
- `git pull --ff-only origin main` completed successfully before discovery.
- Only this run directory is intended for staging.

## Searched Mines

- GitHub code search and repository search were prioritized.
- GitLab and Bitbucket public repository search were checked as secondary code-hosting channels.
- Zenodo, Figshare, Harvard Dataverse, and DataCite/Mendeley-style metadata were checked for DOI-backed datasets.
- A supplemental web search checked GitHub, Zenodo, and Figshare landing-page visibility.

## Keywords Used

- `extension:hsc HYSYS`
- `extension:hsc Aspen HYSYS`
- `extension:hscz HYSYS`
- `extension:compound HYSYS`
- `extension:xml HYSYS XML Cases`
- `extension:xml Aspen HYSYS`
- `HYSYS in:name,description,readme`
- `Aspen HYSYS in:readme,description`
- `HYSYS case file in:readme,description`
- `HYSYS simulation files in:readme,description`
- `HYSYS Python COM in:readme,description`
- `HYSYS MATLAB in:readme,description`
- `HYSYS Excel validation in:readme,description`
- `HYSYS LNG in:readme,description`
- `HYSYS CO2 capture in:readme,description`

## Downloaded Case List

No new HYSYS model payload was downloaded or retained in this heartbeat.

Reason: all high-confidence public HYSYS model hits were already archived in earlier CASE runs, and the only `.hsc` path found in newly inspected GitHub metadata was a duplicate no-license candidate.

## Candidate Findings

| Title | Source page | Download URL | Local evidence | Selection reason | Quality | License / access note | Recommended use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Duplicate licensed GitHub HYSYS case records | https://github.com/search?q=Aspen+HYSYS+.hsc+case+file&type=repositories | not_downloaded_duplicate_existing_case_archive | artifacts/github-repo-search-summary.json; artifacts/web-search-supplement.json | Rediscovered known MIT/GPL/CC-compatible case repositories already archived. | D | Public licenses exist in prior archives, but no duplicate download was needed. | Use existing archived copies for COM bridge, HYSYS-vs-DWSIM, V14 sweetening, and V14 CDU tests. | source_page, filenames, historical CASE records. | Remote repos may have drifted since archive; this run did not re-download. |
| AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR | https://github.com/AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR | https://github.com/AtabakBahadornia/1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR/blob/main/Project-PR/hyApp.hsc | artifacts/github-inspect-AtabakBahadornia__1D-HYSYS-MATLAB-SUPERSONIC-SEPARATOR.json | Contains visible `.hsc` plus MATLAB companion files, but it is already recorded and has no license. | D | Public repository with no explicit license; payload not downloaded. | Manual permission/license review only. | source_page, filename `hyApp.hsc`, prior 1108Z candidate record. | Not safe to archive without permission; HYSYS version unknown. |
| GitHub broad sweep | https://github.com/search?q=HYSYS&type=repositories | not_downloaded_no_new_qualifying_payload | artifacts/github-code-search-summary.json; artifacts/github-inspected-repo-summary.json | 85 merged repositories, 21 inspected trees, no new licensed non-duplicate HYSYS payload. | D | Public metadata only. | Improve filters and suppress profile/resume/XML noise. | no qualifying new source_page/download_url/SHA256. | Tree inspection was capped after API timeout. |
| Secondary repository and data-platform sweep | multi_platform_targeted_search_zenodo_figshare_dataverse_mendeley_gitlab_bitbucket | not_downloaded_no_nonduplicate_hysys_model | artifacts/external-search-summary.json | Zenodo returned known duplicates/no-model hits; other platforms did not yield confirmed model payloads. | D | Public metadata only; Bitbucket public search returned HTTP 410. | Keep duplicate IDs and API failures as filter controls. | source_page and known filename duplicate checks. | Some supplements may only be visible through article pages. |

## Dedupe Summary

Existing CASE history read before this run:

- `sources.json` files: 33
- `index.md` files: 33
- Source entries: 169
- Known source pages: 157
- Known download URLs: 96
- Known titles: 230
- Known SHA256 hashes: 599
- Known filenames: 700
- Bad `sources.json` files: 0

## Search Summary

- GitHub code search: direct `.hsc`, `.hscz`, and `.compound` queries returned 0 items; XML keyword queries returned 30 items each but did not confirm HYSYS XML cases.
- GitHub repository search: 85 unique repositories merged; 21 trees inspected before API timeout; 1 HYSYS-like `.hsc` repo found and it was the already recorded no-license Atabak candidate.
- Zenodo: 20 public metadata hits for `Aspen HYSYS`; high-value HYSYS records matched existing duplicate archives.
- Figshare: 0 selected hits through API search.
- Harvard Dataverse: 1 metadata hit, no confirmed HYSYS model payload.
- DataCite/Mendeley-style metadata: 50 metadata hits, no selected HYSYS case payload.
- GitLab: 0 selected hits.
- Bitbucket: public repository search endpoint returned HTTP 410.

## Safety Notes

- No `.hsc`, `.hscz`, `.compound`, archive, executable, macro-enabled workbook, or script payload was retained from external sources.
- Search and inspection artifacts are JSON/TXT metadata only.
- No HYSYS model was opened, loaded, run, or solved.
- No downloaded code, scripts, macros, notebooks, executables, or unknown binaries were run.

## Residual Risks

- GitHub tree inspection was partially capped after an API timeout, so the broad search should be treated as a strong but not exhaustive sweep.
- No-license `.hsc` repositories can only move into the benchmark library after author permission or license clarification.
- Some open-access paper supplements may require article-page-specific scraping that was outside this heartbeat scope.

## Follow-Up Recommendations

1. Add a durable duplicate allowlist for the already archived licensed GitHub repositories.
2. Add a durable no-license denylist/manual-review list for Atabak, afabrild, marcellobozzini, and similar `.hsc` candidates.
3. Replace broad GitHub XML searches with narrower filename/path filters to avoid generic XML noise.
4. Add retry/backoff and per-repository tree size caps to avoid future batch inspection timeouts.
5. Keep using GitHub as the first source, with Zenodo only for clearly licensed DOI-backed HYSYS payloads.

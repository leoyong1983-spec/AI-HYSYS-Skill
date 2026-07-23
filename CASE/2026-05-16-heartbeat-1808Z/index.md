# Aspen HYSYS Case Discovery Heartbeat - 2026-05-16 1808Z

## Run Metadata

- Automation ID: ai-hysys-case-2
- Trigger time UTC: 2026-05-16T18:08:27.681Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Run directory: CASE/2026-05-16-heartbeat-1808Z
- Artifact directory: CASE/2026-05-16-heartbeat-1808Z/artifacts
- HYSYS model run status: not_run

## Repository Gate

- Confirmed Git repository on branch `main`.
- `git pull --ff-only origin main` completed successfully.
- The prior 17:08Z local commit was still ahead by 1 at start; it was pushed successfully before this run continued.
- Only this run directory is intended for staging.

## Searched Mines

- GitHub repository search was prioritized and targeted at Aspen HYSYS, HYSYS automation, HYSYS simulation, HYSYS case, and HYSYS LNG/CO2 terms.
- GitHub repository trees were inspected for likely case/project repositories.
- Zenodo, Figshare, Harvard Dataverse, DataCite/Mendeley-style DOI metadata, GitLab, and Bitbucket were checked as secondary sources.

## Keywords Used

- `Aspen HYSYS`
- `HYSYS automation`
- `HYSYS simulation`
- `HYSYS case`
- `HYSYS LNG CO2`
- `Aspen HYSYS .hsc`
- `Aspen HYSYS simulation`

## Downloaded Case List

No new HYSYS model payload was downloaded or retained in this heartbeat.

Reason: this run found many GitHub `.hsc` candidates, but the repositories lacked explicit licenses or were marked as `NOASSERTION`. Licensed MIT repositories inspected in this run did not expose a qualifying HYSYS model payload.

## Candidate Findings

| Title | Source page | Download URL | Local evidence | Selection reason | Quality | License / access note | Recommended use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub no-license `.hsc` candidate cluster | https://github.com/search?q=Aspen+HYSYS&type=repositories | not_downloaded_no_explicit_license | `artifacts/github-targeted-inspection-summary.json` | 12 inspected repositories contained `.hsc` or HYSYS-like XML paths. | D | Public repositories, but no explicit license or `NOASSERTION`; no payload retained. | Manual license queue; prioritize ammonia, HDA, Tennessee Eastman, acetic acid, methanol, and gas turbine candidates if permission is obtained. | source_page, filenames, prior CASE duplicate checks. | No redistribution rights; provenance/version mostly unknown. |
| JeePeiQi0101/Aspen.HYSYS XML candidate | https://github.com/JeePeiQi0101/Aspen.HYSYS | not_downloaded_no_explicit_license | `artifacts/github-inspect-JeePeiQi0101__Aspen.HYSYS.json` | Three files named as Aspen HYSYS simulation XML. | D | No explicit license; XML files not downloaded. | Possible future parser/import test after license review. | source_page and XML filenames. | Filename inference only; contents not inspected. |
| Licensed GitHub automation/data references without model payload | https://github.com/search?q=Aspen+HYSYS+automation&type=repositories | not_downloaded_no_hysys_model_payload | `artifacts/github-search-summary.json`; `artifacts/github-targeted-inspection-summary.json` | MIT repositories mention Aspen HYSYS but no case file was exposed. | D | Public MIT metadata, but not valid HYSYS benchmark cases. | Automation/data-processing reference only. | no `.hsc/.hscz/.compound/HYSYS XML` payload found. | Derived data must not be relabeled as HYSYS-native cases. |
| Secondary platform sweep | multi_platform_targeted_search_2026-05-16T18:08Z | not_downloaded_no_nonduplicate_hysys_model | `artifacts/external-search-summary.json` | No new non-duplicate HYSYS payload found outside GitHub. | D | Public metadata only; known Zenodo model records are duplicates. | Filter tuning and duplicate controls. | source_page and known filename duplicate checks. | Some article supplements may require manual review. |

## Dedupe Summary

Existing CASE history read before this run:

- `sources.json` files: 34
- `index.md` files: 34
- Source entries: 173
- Known source pages: 162
- Known download URLs: 99
- Known titles: 235
- Known SHA256 hashes: 614
- Known filenames: 711
- Bad `sources.json` files: 0

## Search Summary

- GitHub search artifacts: 45 `Aspen HYSYS` repository hits, 3 `HYSYS automation`, 6 `HYSYS simulation`, 3 `HYSYS case`, 0 `HYSYS LNG CO2`.
- Targeted GitHub tree inspection: 25 repositories inspected; 12 exposed `.hsc` or HYSYS-like XML paths; 0 were eligible for download due to license or payload rules.
- Zenodo: 20 metadata hits; known HYSYS payloads matched existing duplicate archives.
- Figshare: 0 selected hits.
- Harvard Dataverse: 1 metadata hit, no confirmed HYSYS model payload.
- DataCite/Mendeley-style metadata: 50 metadata hits, no selected case payload.
- GitLab: 0 selected hits.
- Bitbucket: public repository search endpoint returned HTTP 410.

## Safety Notes

- No `.hsc`, `.hscz`, `.compound`, archive, executable, macro-enabled workbook, notebook, or script payload was retained from external sources.
- Search and inspection artifacts are JSON/TXT metadata only.
- No HYSYS model was opened, loaded, run, or solved.
- No downloaded code, scripts, macros, notebooks, executables, or unknown binaries were run.

## Residual Risks

- Many promising `.hsc` repositories have no license; they need manual permission before archival.
- Some repositories may be coursework or personal project material with unclear provenance.
- GitHub tree metadata identifies filenames but not HYSYS internal version unless README or description states it.
- DOI and data-platform metadata may miss supplemental materials exposed only through article pages.

## Follow-Up Recommendations

1. Create a durable manual-license-review queue for the no-license `.hsc` cluster found in this run.
2. Add a no-license skip list so future hourly runs do not repeatedly inspect the same GitHub candidates.
3. Add a licensed-only GitHub search lane first, then a no-license metadata-only lane.
4. Consider a maintainer-approved policy for contacting authors of high-value no-license HYSYS repositories.
5. Continue not downloading no-license HYSYS payloads until permission is explicit.

# Aspen HYSYS Case Discovery Heartbeat - 2026-05-16 0908Z

## Run Time

- Trigger time UTC: 2026-05-16T09:08:15.440Z
- Repository: D:\CODEX\AI-HYSYS-Skill
- Branch gate: main confirmed; git status clean before work; git pull --ff-only origin main succeeded.
- Safety posture: no HYSYS model was opened, run, solved, or automated. No scripts, notebooks, macros, executables, archives, or unknown binaries were executed.

## Search Mines

- GitHub code search, repository search, selected repository tree metadata, and release metadata.
- GitLab and Bitbucket public project/repository search.
- Zenodo public records API.
- Figshare public articles API.
- Harvard Dataverse public search API.
- DataCite query restricted to Mendeley Data client ID.

## Keywords

- HYSYS --extension hsc
- Aspen HYSYS --extension hsc
- HYSYS --extension hscz
- Aspen HYSYS --extension hscz
- HYSYS --extension compound
- HYSYS XML Cases --extension xml
- Aspen HYSYS --extension xml
- HYSYS
- "Aspen HYSYS"
- "HYSYS" "simulation"
- "HYSYS" "case file"
- "HYSYS" ".hsc"
- "HYSYS" ".hscz"
- "HYSYS" "Python" "COM"
- "HYSYS" "MATLAB"
- "HYSYS" "Excel" "validation"
- Aspen HYSYS supplementary material hsc
- Aspen HYSYS CO2 capture hsc
- Aspen HYSYS LNG hsc
- Aspen HYSYS hydrogen hsc
- Aspen HYSYS ammonia hsc
- Aspen HYSYS methanol hsc

## Download Case List

| Item | Source URL | Download URL | Local path | Quality |
|---|---|---|---|---|
| GitHub broad/deep sweep | https://github.com/search?q=HYSYS&type=repositories | Not downloaded - no licensed new HYSYS model | artifacts/github-*.json | D |
| Zenodo duplicate/no-model sweep | https://zenodo.org/search?q=Aspen%20HYSYS%20hsc | Not downloaded - duplicates or no model | artifacts/zenodo-0908-targeted-search-results.json | D |
| Secondary platforms | GitLab / Bitbucket / Figshare / Harvard Dataverse / Mendeley DataCite | Not downloaded - no confirmed model | artifacts/*-0908-*.json | D |

No new HYSYS case payloads were downloaded or retained in this run.

## Findings

- GitHub code search returned no .hsc, .hscz, or .compound results. Aspen HYSYS XML results were not confirmed as HYSYS XML case files.
- GitHub repository search produced 85 merged repositories. Selected deep scan covered likely HYSYS automation/simulation leads including sajjad-ah/ASPEN-HYSYS, snua/HYSYS-dynamic-simulation, SuradechKKPB/AutomatedHYSYS, and related repositories. No new licensed HYSYS model payload was confirmed.
- MIT/GPL/Apache repositories in the deep scan were automation or unrelated code references, not benchmark case packages.
- Zenodo rediscovered known case records 10966344, 14882867, and 18806107; they were treated as duplicates.
- Zenodo 19469917 and 6621128 are title-relevant but no HYSYS model payload was confirmed in this run.
- GitLab, Bitbucket, and Mendeley/DataCite returned no actionable model hit. Figshare and Harvard Dataverse remained noisy.

## Selection Reasons

- New retained case count is 0 because no source met all lock criteria: public/legal storage rights, non-duplicate status, and confirmed HYSYS model payload.
- Candidate/search metadata was retained because it documents negative coverage and helps future query suppression.

## Quality Ratings

- All entries are D: candidate, duplicate, rejected, or search metadata only.

## License And Public Access Notes

- Only public APIs and public GitHub metadata were used.
- No login-required, paid, customer-support, institution-only, or commercial training resource was accessed.
- No payload was downloaded from no-license repositories.

## Recommended Automation Uses

- Keep GitHub as the primary mine, but split automation-reference repositories from benchmark case candidates.
- Maintain a no-license watchlist for repositories that look relevant but cannot be archived.
- Keep Zenodo 10966344, 14882867, and 18806107 on the duplicate allowlist.
- Keep Zenodo 19469917 on the no-model exclusion list unless a real HYSYS case file appears.

## Dedupe Basis

- Existing CASE/**/sources.json and CASE/**/index.md were scanned before discovery.
- Dedupe keys used: source_page, download_url, title, SHA256, and filename.
- Dedupe summary: 31 sources.json files, 31 index.md files, 162 structured source entries, 109 seen source pages, 91 seen download URLs, 217 seen titles, 553 seen SHA256 values, and 597 seen filenames.

## Residual Risks

- GitHub code search may miss binary HYSYS files or release-only assets.
- Some public repositories have no license; they were not downloaded.
- Secondary platform search is metadata-only and can miss attachments not exposed in search results.
- HYSYS versions remain unknown because no model was opened.

## Follow-Up Recommendations

1. Suppress empty profile repositories and generic web/app repositories that match HYSYS by name only.
2. Keep release-asset inspection restricted to repositories with clear license metadata and model-like asset names.
3. Add a separate automation-reference digest for MIT/GPL HYSYS COM examples that lack case files.
4. Continue direct Zenodo duplicate filtering before any download attempt.

## Local Artifacts

- CASE/2026-05-16-heartbeat-0908Z/artifacts/bitbucket-0908-repository-search-results.json - SHA256 aae57000235aa044f01b93927a56d54faa594054322a1027cd51558311207278 - 1380 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/dedupe-summary.json - SHA256 e944f5603a12df6bdbf081299a495a7f54a9d7ac4d2a7e41606bccb1644ef965 - 301 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/figshare-0908-targeted-search-results.json - SHA256 e0d6de37ae483aebddde737e67d8f0ad42680d857e55166e7159e1e0f25e6d5f - 61744 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-aspen-hysys-ext-hsc.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-aspen-hysys-ext-hscz.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-aspen-hysys-ext-xml.json - SHA256 f4d30ac771ea7c78cb02de99b223a34f20eb440b70245488647aaf885e28a24f - 11833 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-hysys-ext-compound.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-hysys-ext-hsc.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-hysys-ext-hscz.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-hysys-xml-cases-ext-xml.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-code-search-summary.json - SHA256 eac9aab89def4456b0140d5b33c1b72ec888df5a21ad2d91fc4e23a0ea2c8f00 - 1171 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-DanielVazVaz__PySIS.json - SHA256 7050b65932955e1c5b331c30980342e5cd163c3a0788479376db0ebf177098ca - 2786 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-oscarcontrerasnavas__hysys-to-excel-intro.json - SHA256 655cec73641b0b794cb0fae7888160ef1ce4ec83ccbc21ca8d84062a6d8236ce - 1909 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-pSantosb__Hysys-connection-Excel-Matlab-Python-Unity.json - SHA256 e801ed8fc5daf3206bfd1f1e3aeada30ad39fcdb5cee1b714da617e237d07ee8 - 3265 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-sajjad-ah__ASPEN-HYSYS.json - SHA256 0950c81c844914564630555926d64965956eddc0f60524bc24c812c722189b72 - 4022 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-scan-summary.json - SHA256 834c4063d35efeeaff9c73a9c1b74d69a23e422186a3547a90612381fd464b0f - 2732 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-Shreya88876__Aspen_file_shreya.json - SHA256 e8d1b69615b37d2a6ee5a76699adfc88d4861bd55f5b0516b029827d8d7ceb34 - 1088 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-snua__HYSYS-dynamic-simulation.json - SHA256 49c28f512c3723409cfaf317a74ca128008d198c1a8e2ceed4f1b8b0208f1694 - 1987 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-stonedingwt__HYSys.json - SHA256 88993638410e10fb4ec6be5209ae82d712795a0e9919d015287d569797dbc151 - 26317 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-SuradechKKPB__AutomatedHYSYS.json - SHA256 0181e0e83ea818f780ffb275ae50d19fae777ee9d0c689824e5777f4d8476370 - 1913 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-vminasid__Hysys-Unisis2Matlab.json - SHA256 dfb75b80eae7e6a1cafefa93c140c6a9836436b01060663a49688bcfbf3cf572 - 2210 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-deep-YuniqueCore__DynPlots.json - SHA256 6f655e97c1fb55e7b1e7f3e8866866da84aa92320b9162828ca863c3c7cbd47e - 3698 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-aspen-hysys.json - SHA256 106936005987176c366b1bdd5e4de8759ee20cc0524714ef39ee2298209df037 - 18851 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-broad.json - SHA256 ec91c14ee5ebcd3977aa098fae8ff730764a24f96460d16275384b91b697e478 - 17653 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-case-file.json - SHA256 7249b4ad6e08886ef7a0ee49d590b223951421569f3c18b5b34a97b44604dbc1 - 1221 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-excel-validation.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-hsc.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-hscz.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-matlab.json - SHA256 6d03e572399a34581470fb8c1ef7ecfba5cc0bb2e6d4616734631d85ea837b11 - 706 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-python-com.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-hysys-simulation.json - SHA256 d4994239c1aa3b2af3ce922a5f506d42dd0dd8697f46174c05231411252cdf23 - 2880 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-merged-results.json - SHA256 c8e91301700d59e4b836ffc83a1a583c49a78b22b1f0cefeb8dd3044b7164b54 - 133307 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/github-repo-search-summary.json - SHA256 fd2d5446c6abaf75a5b752eaf9b84728fc762b13071b6e495a9a1adcf66c64de - 1425 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/gitlab-0908-project-search-results.json - SHA256 7458b2f7f9dfecb0c0cbaa81a24bdc678560da0fa4cd8c9615ce3d9d16089033 - 1444 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/harvard-dataverse-0908-targeted-search-results.json - SHA256 b3d656834bdb56af64166acd0a71586b3d82512e6e95a30e74b5a773833907dc - 127841 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/mendeley-datacite-0908-targeted-search-results.json - SHA256 b832f2e823568fa9b0109abfc421b13db7f17424500742c0c4dae4a9836dd133 - 3180 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/security-inventory.json - SHA256 885d02d5d16940f5071e38ee9a89201a3ea2ac0adf9b27e65d1090b5d971636f - 19119 bytes
- CASE/2026-05-16-heartbeat-0908Z/artifacts/zenodo-0908-targeted-search-results.json - SHA256 52c25362bb592998988f3d12713dee5959fea7c66dac477d3b307b18bb28f352 - 253885 bytes

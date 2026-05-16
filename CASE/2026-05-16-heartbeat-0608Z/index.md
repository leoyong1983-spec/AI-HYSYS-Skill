# Aspen HYSYS Case Discovery Heartbeat - 2026-05-16 0608Z

## Run Time

- Trigger time UTC: 2026-05-16T06:08:12.133Z
- Repository: D:\CODEX\AI-HYSYS-Skill
- Branch gate: main confirmed; git status clean before work; git pull --ff-only origin main succeeded.
- Safety posture: no HYSYS model was opened, run, solved, or automated. No scripts, notebooks, macros, executables, or unknown binaries were executed.

## Search Mines

- GitHub code search for .hsc, .hscz, .xml, .compound plus GitHub repository search.
- GitLab and Bitbucket public project/repository search.
- Zenodo public records API, including direct record check for Zenodo 19469917.
- Figshare public articles API.
- Harvard Dataverse public search API.
- DataCite query restricted to Mendeley Data client ID.

## Keywords

- HYSYS --extension hsc
- Aspen HYSYS --extension hsc
- HYSYS --extension hscz
- Aspen HYSYS --extension hscz
- HYSYS --extension xml
- HYSYS XML Cases --extension xml
- HYSYS --extension compound
- "Aspen HYSYS" ".hsc"
- "Aspen HYSYS" ".hscz"
- "Aspen HYSYS" "case file"
- "Aspen HYSYS" "simulation files"
- "HYSYS" "Python" "COM"
- "HYSYS" "MATLAB" "hsc"
- "HYSYS" "Excel" "validation"
- Aspen HYSYS case file
- Aspen HYSYS simulation file
- Aspen HYSYS supplementary material hsc
- Aspen HYSYS CO2 capture hsc
- Aspen HYSYS LNG hsc
- Aspen HYSYS hydrogen hsc

## Download Case List

| Item | Source URL | Download URL | Local path | Quality |
|---|---|---|---|---|
| marcellobozzini/Python-Driving-License | https://github.com/marcellobozzini/Python-Driving-License | Not downloaded - no license | Metadata only in artifacts/github-marcellobozzini__Python-Driving-License-* | D |
| GaboTalero/HYSYS-Python-Case-Builder | https://github.com/GaboTalero/HYSYS-Python-Case-Builder | Not downloaded - no HYSYS model file | Metadata only in artifacts/github-GaboTalero__HYSYS-Python-Case-Builder-* | D |
| Zenodo 19469917 Hydrogen Co-Firing | https://zenodo.org/records/19469917 | Not retained - archive listing has no HYSYS model | artifacts/zenodo-19469917-record.json; artifacts/zenodo-19469917-archive-listing.txt | D |
| Known Zenodo duplicates | https://zenodo.org/records/10966344, /14882867, /18806107 | Not downloaded - duplicates | artifacts/zenodo-0608-targeted-search-results.json | D |

No new licensed, non-duplicate Aspen HYSYS benchmark case was retained in this run.

## Findings

- GitHub code search found no .hsc, .hscz, or .compound hits. The .xml hits were unrelated XML or file-signature metadata, not HYSYS XML cases.
- marcellobozzini/Python-Driving-License contains Separazione_reattori.hsc and a notebook, but has no repository license; payloads were not downloaded.
- GaboTalero/HYSYS-Python-Case-Builder is MIT-licensed and useful as HYSYS COM automation reference material, but contains no HYSYS model payload.
- Zenodo 19469917 is CC-BY-4.0 and title-relevant. Safe archive listing showed only PNG and XLSX files; no HYSYS model file was present, so the archive was not retained.
- Zenodo 10966344, 14882867, and 18806107 were rediscovered as duplicates already present in CASE.
- GitLab, Bitbucket, Mendeley/DataCite returned no actionable model hit. Figshare and Harvard Dataverse results were keyword noise.

## Selection Reasons

- New retained case count is 0 because no source met all three requirements: public/legal storage rights, non-duplicate status, and confirmed HYSYS model payload.
- Candidate metadata was retained because it improves future filtering and identifies one manual license-review target.

## Quality Ratings

- All entries are D: candidate, duplicate, rejected, or search metadata only.

## License And Public Access Notes

- Public GitHub and open data repository metadata only.
- No login, paywall, customer support, institution-only, or commercial training resource was accessed.
- The only new candidate with a confirmed .hsc file has no license, so it was not downloaded.

## Recommended Automation Uses

- Review marcellobozzini/Python-Driving-License manually for permission before any future payload acquisition.
- Treat GaboTalero/HYSYS-Python-Case-Builder as a COM automation reference candidate, not as a case benchmark.
- Exclude Zenodo 19469917 from benchmark downloads unless authors publish a real HYSYS case file.
- Keep known Zenodo records 10966344, 14882867, and 18806107 on the duplicate allowlist.

## Dedupe Basis

- Existing CASE/**/sources.json and CASE/**/index.md were scanned before discovery.
- Dedupe keys used: source_page, download_url, title, SHA256, and filename.
- Dedupe summary: 30 sources.json files, 30 index.md files, 157 structured source entries, 107 seen source pages, 88 seen download URLs, 207 seen titles, 528 seen SHA256 values, and 566 seen filenames.

## Residual Risks

- GitHub may not index binary HYSYS files in code search.
- Repository license metadata can change after this run.
- The Zenodo 19469917 RAR was listed but not retained or extracted; conclusions are based on archive listing only.
- HYSYS versions remain unknown for all candidates because no model was opened.

## Follow-Up Recommendations

1. Add marcellobozzini/Python-Driving-License to the manual-license-review watchlist.
2. Add GaboTalero/HYSYS-Python-Case-Builder to an automation-reference watchlist, separate from benchmark CASE assets.
3. Add zenodo:19469917 to a no-model exclusion list until a HYSYS case file is published.
4. Keep release-asset inspection disabled unless a repository has clear license metadata and a model-like release asset name.

## Local Artifacts

- CASE/2026-05-16-heartbeat-0608Z/artifacts/bitbucket-0608-repository-search-results.json - SHA256 76568b828a4493855f4e56a8f22b7a613484b0e730acc33e42e77ceddc793bee - 1022 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/dedupe-summary.json - SHA256 b92c4a6b3349fa6aacbb7e0ae25e3c5e4f47a4f5d5e70b1e8c7bb1f29ac68816 - 301 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/figshare-0608-targeted-search-results.json - SHA256 2e63f82e49a8153ef618f3fc2c35b20b6f1c8fef5d25624ff2bd6ad5b1c624ae - 51553 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-candidate-tree-summary.json - SHA256 5c7e29f75bcde5ffc8a99b9d3bd568e5bd21a754c04b400f15e28fcba2326133 - 3655 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-aspen-hysys-ext-hsc.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-aspen-hysys-ext-hscz.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-hysys-ext-compound.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-hysys-ext-hsc.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-hysys-ext-hscz.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-hysys-ext-xml.json - SHA256 24793146d22e0be1c55bcb206f2ded3f50871fa80478bfc1b77b9d682b925539 - 20851 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-hysys-xml-cases-ext-xml.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-code-search-summary.json - SHA256 788d9334ebe26cce88a5a1fe3821763ce3fa351f9bf9aa3effbda0302c4a55fd - 1159 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-GaboTalero__HYSYS-Python-Case-Builder-contents-root.json - SHA256 5b78beb73e8f3e6c36c31dc43ece356900ae3f33567ec6edbfd601194dbdfc50 - 8393 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-GaboTalero__HYSYS-Python-Case-Builder-repo.json - SHA256 b7a80221bc23c6141a0bc743aebe1fbb9c596168c9c6bb26390dbd04e8b1a270 - 486 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-GaboTalero__HYSYS-Python-Case-Builder-tree.json - SHA256 23dcec73dbd8e25d488d64d22b6c7fa63793497a8d6fec8cedcf56d2537b1428 - 2429 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-marcellobozzini__Python-Driving-License-contents-root.json - SHA256 ad0aacba99528cc39ee7a0fec23d9765682bb54808b4b42fd4673a27c30efcde - 2022 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-marcellobozzini__Python-Driving-License-repo.json - SHA256 76807a9e2059e57075dc307e4191dc6586c4d5fe97939c496220ef7515aa5eab - 418 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-marcellobozzini__Python-Driving-License-tree.json - SHA256 9447fa8d73041888a5f1da63c402a9ee2bfa0097952a572a04a73d7331e22af9 - 727 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-aspen-hysys-hsc.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-hysys-case-file.json - SHA256 f919b5e78d32fe66375d828af4cb28ac17f2ea3e1e997b375bf905c1d58ba51e - 463 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-hysys-excel-validation.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-hysys-hscz.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-hysys-matlab-link.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-hysys-python-com.json - SHA256 50056c08ce479cc2f54c4d6595a4264bdf32bf84f2995d59ff3bd513897ab414 - 7 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-hysys-simulation-files.json - SHA256 3a286dd32023776b2e26efd190b240c3a1d5ca9359fb8932a5c989c45664bb64 - 390 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/github-repo-search-summary.json - SHA256 ed3f9a31428fb39703a7b03b32e141bbdfadc3528af030a616a9fee816678687 - 1190 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/gitlab-0608-project-search-results.json - SHA256 f8efa3750152f2bd7180c8c746e0b91ae72b38e15ef6f7155f13e917b10ab828 - 1194 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/harvard-dataverse-0608-targeted-search-results.json - SHA256 3771f3fa2707301ec35a57ebe3176e6fb96aad67c0f9a690fe2d7d5fb0327fd2 - 103478 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/mendeley-datacite-0608-targeted-search-results.json - SHA256 ab16c38321b3b66619ed7f5cffff3df2e23f30fba853c298d053511a8ffd6960 - 2602 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/security-inventory.json - SHA256 68a450c1d160ee16ea3a162a85acbb1aeb78906e7d7af94ec731e089e83d9814 - 16301 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/zenodo-0608-targeted-search-results.json - SHA256 ccf673d516e9588d047ec1c69e2044e9eba7bf8395fa06245d3f3ac1368fb516 - 209187 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/zenodo-19469917-archive-listing.txt - SHA256 c4138bcf98dad6f840c9ea5aa63029ae44963a576e0a405c69603ac18df20957 - 293 bytes
- CASE/2026-05-16-heartbeat-0608Z/artifacts/zenodo-19469917-record.json - SHA256 b6b3a3abfa1bb371d1192813256067a055e25f389b3bf154ff4a11980dd3e98f - 7070 bytes

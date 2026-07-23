# Aspen HYSYS Case Discovery Heartbeat - 2026-05-16 0508Z

## Run Time

- Trigger time UTC: 2026-05-16T05:08:11.261Z
- Repository: D:\CODEX\AI-HYSYS-Skill
- Branch gate: main confirmed before work; git pull --ff-only origin main succeeded.
- Safety posture: metadata-only run; no HYSYS model, executable, macro, notebook, or script was opened, executed, or solved.

## Search Mines

- GitHub repository search and recursive tree metadata, prioritized over other mines.
- GitLab project search and Bitbucket repository search with narrow HYSYS terms.
- Zenodo public records API.
- Figshare public articles API.
- Harvard Dataverse public search API.

## Keywords

- HYSYS PFD hsc in:readme
- HYSYS flowsheet hsc in:readme
- HYSYS report hsc in:readme
- HYSYS Excel validation hsc in:readme
- HYSYS Python COM hsc in:readme
- HYSYS MATLAB hsc in:readme
- "Aspen HYSYS" "process simulation" hsc in:readme
- "Aspen HYSYS" "model file" in:readme
- HYSYS hscz in:readme
- HYSYS compound in:readme
- Aspen HYSYS PFD hsc
- Aspen HYSYS flowsheet hsc
- Aspen HYSYS report hsc
- Aspen HYSYS Excel validation hsc
- Aspen HYSYS V10 hsc
- Aspen HYSYS V11 hsc
- Aspen HYSYS model file
- Aspen HYSYS hscz
- HYSYS XML Cases xml

## Download Case List

| Item | Source URL | Download URL | Local path | Quality |
|---|---|---|---|---|
| GitHub-first repository sweep | https://github.com/search?q=Aspen+HYSYS+hsc+in%3Areadme&type=repositories | Not downloaded - no confirmed new model | artifacts/github-0508-* and github-cli-search-*.json | D |
| Zenodo duplicate HYSYS model sweep | https://zenodo.org/search?q=Aspen%20HYSYS%20hsc | Not downloaded - duplicates already archived | artifacts/zenodo-0508-targeted-search-results.json | D |
| GitLab and Bitbucket narrow sweep | https://gitlab.com/explore/projects / https://bitbucket.org/repo/all | Not downloaded - no results | artifacts/gitlab-0508-project-search-results.json; artifacts/bitbucket-0508-repository-search-results.json | D |
| Figshare and Harvard Dataverse sweep | https://figshare.com/search / https://dataverse.harvard.edu/dataverse/harvard | Not downloaded - no HYSYS model confirmed | artifacts/figshare-0508-targeted-search-results.json; artifacts/harvard-dataverse-0508-targeted-search-results.json | D |

No new HYSYS case payloads were downloaded in this run.

## Findings

- GitHub: 12 repository searches produced 23 unique repositories; 8 unseen repositories were inspected. None contained .hsc, .hscz, HYSYS XML, or .compound model payloads. jjgomera/pychemqt is a GPL-3.0 process-simulation tool, but it is not a HYSYS case repository.
- GitLab/Bitbucket: narrow public API searches returned no matching repositories.
- Zenodo: known HYSYS model records appeared again: 10966344, 14882867, and 18806107. They were treated as duplicates and not downloaded.
- Figshare/Harvard Dataverse: results were keyword noise or non-HYSYS XML datasets; no HYSYS model file was confirmed.

## Selection Reasons

- No candidate satisfied the run's lock criteria for a new, non-duplicate, public Aspen HYSYS model file with clear storage rights.
- Metadata artifacts were kept because they support duplicate suppression and query refinement.

## Quality Ratings

- All current-run entries are rated D: candidate/search metadata only, no new benchmark case added.

## License And Public Access Notes

- Only public metadata APIs and public GitHub tree metadata were used.
- Known Zenodo duplicates include CC-BY-4.0 and CC-BY-NC-ND-4.0 records; those assets already exist in prior CASE folders.
- No login-required, paid, customer-support, commercial-training, or institution-only resources were accessed.

## Recommended Automation Uses

- Use the GitHub false-positive list to refine repository filters.
- Keep Zenodo 10966344, 14882867, and 18806107 on the duplicate allowlist.
- Use Figshare/Dataverse metadata only for search tuning; do not treat returned XML files as HYSYS XML unless the surrounding metadata confirms Aspen HYSYS.

## Dedupe Basis

- Existing CASE/**/sources.json and CASE/**/index.md were scanned before discovery.
- Dedupe keys used: source_page, download_url, title, SHA256, and filename.
- Dedupe summary: 29 sources.json files, 29 index.md files, 153 structured source entries, 99 seen source pages, 85 seen download URLs, 199 seen titles, 506 seen SHA256 values, and 542 seen filenames.

## Residual Risks

- GitHub API search can miss binary files attached only to releases or stored behind LFS pointers that are not obvious from repository trees.
- GitLab and Bitbucket unauthenticated search coverage is shallow.
- Public repository licenses can change; no payloads were downloaded from no-license candidates.
- Search metadata can contain unrelated HSC/XML terms from non-process-simulation domains.

## Follow-Up Recommendations

1. Add a query suppression list for resume/portfolio and generic thermodynamics repositories that repeatedly match HYSYS terms without case files.
2. Keep GitHub as the primary mine but add release-asset inspection only after repository license and model signals are clear.
3. Continue treating Zenodo 10966344, 14882867, and 18806107 as known duplicates.
4. For Dataverse/Figshare, require explicit Aspen HYSYS wording plus model-like filenames before recording individual candidate entries.

## Local Artifacts

- CASE/2026-05-16-heartbeat-0508Z/artifacts/bitbucket-0508-repository-search-results.json - SHA256 87695ade294b514a506c04b3fcb4fa8fbf78bea8115815c32fc51eaa0fb960b0 - 1000 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/dedupe-summary.json - SHA256 12d41500bcea3576fe21729c23081cfec934391dd0bfe853c422b89fa1cd293d - 239 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/figshare-0508-targeted-search-results.json - SHA256 0eeddc44af52087e6e15d5ada4e825414fc2b970f1de52e61a8cd06df879bf32 - 52981 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-0508-search-merged-repos.json - SHA256 6b08071c96a967a74bb544c385ad5bb31de01d70c686a6b371dff2f60a095c09 - 7778 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-0508-tree-summary.json - SHA256 266812cb116f17661d007827372144153946e94d01fe63e61a1763ebf0a41070 - 6974 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-aspen-hysys-model-file.json - SHA256 8903ac86cdf2bd2a3752414f2da981932ed4527292ead0092930a8ba3393ac16 - 75 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-aspen-hysys-process-simulation.json - SHA256 e275820bfcd5d8406d2666e8b070f7ef452ea374123424d2514d2c25d09341f0 - 3639 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-excel-validation-hsc.json - SHA256 0807ea1c4b16288db70d0e020d60f80bf47a2457e1ecc7486db0755ed74eb809 - 1270 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-extension-compound.json - SHA256 412aca67266270f5a2cfdd1a9587a0ee2fa82b66b1aa6b8ced879ee2014caaad - 6764 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-extension-hscz.json - SHA256 dcd163395d9da097718040a9b09df9ef272c4a314e0347a86d8ff7e4cfcfcf46 - 55 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-flowsheet-hsc.json - SHA256 cab9de1ed0e02580d02668804b8de139ed615ee2cbc3df56ad0e15ba5274a045 - 3094 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-matlab-hsc.json - SHA256 3607e895012651201e6645aec6194d3a715e110d4da95a8fdcf59ac4779e18e3 - 3536 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-pfd-hsc.json - SHA256 3c4ecaf551cdc3231ca235dace2e753371101a3c9068f4cca3281be11a9e9387 - 676 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-python-com-hsc.json - SHA256 a354e4cfaf88d3b1a010805689822df6078d1790c5e7dc28363f1e135c216aaf - 5436 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-report-hsc.json - SHA256 0790dc476382f3368cb2652fe34aca9365a7af5a1462969e9d6990fd3691b1c3 - 1800 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-v10-hsc.json - SHA256 c2b3e9a7f45a5fac70bcb0ed89bf601238a3317bed0add5405fd2c059666c186 - 675 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-cli-search-hysys-v11-hsc.json - SHA256 1b07a8f63a3d75fb070573667294dcf43ba9241661095deb50a68af2780ab86d - 68 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-jjgomera__pychemqt-repo.json - SHA256 0151789bab571c0c36988fc1381758453c69b3140d0bdf1bfe4b0912de4b1481 - 6139 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/github-jjgomera__pychemqt-tree.json - SHA256 56c8a7bc77417cffd4e3cdef40fb4f349297dc3a056e610e6223468e9a0a4100 - 336858 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/gitlab-0508-project-search-results.json - SHA256 e37e7a5b1871d3063a668256d8a9b745d02306890d086f8f22e2cedca51902c0 - 1198 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/harvard-dataverse-0508-targeted-search-results.json - SHA256 fef71271429229fe1f817091ff2fb4c943881435447e67e4a2f4afc6b9cec5eb - 142285 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/security-inventory.json - SHA256 baa894e1cfc17eff198bc40066fef71e91be3a82e94556f47a0770c35a1224b2 - 10432 bytes
- CASE/2026-05-16-heartbeat-0508Z/artifacts/zenodo-0508-targeted-search-results.json - SHA256 5f31ba3ec6696c85d554f060de65adb6871ff664a504d1690f0b3e7dcbed86c6 - 209352 bytes

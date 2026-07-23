# CASE Heartbeat 2026-05-11 1815Z

## Run Time
- Trigger UTC window: 2026-05-11T18:15:45Z -> 2026-05-11T18:25:41Z
- Local workspace: D:\CODEX\AI-HYSYS-Skill
- Output folder: CASE/2026-05-11-heartbeat-1815Z

## Repository Gate
- Confirmed Git repo on main.
- Executed git status and git pull --ff-only origin main before discovery.
- Pull result: up to date.

## Search Mines (priority-first)
1. Scientific data repositories
- Zenodo API (q=Aspen HYSYS, q=HYSYS)
- Mendeley Data public API (/public-api/datasets/{id})
- Figshare API (/v2/articles/search with hysys / Aspen HYSYS)
2. Open-source code hosting
- GitHub repository snapshots via codeload.github.com for HYSYS candidates
3. Existing CASE dedupe baseline
- Loaded all historical CASE/*/sources.json and deduped by source_page, download_url, title, filename, SHA256.

## Keywords Used
- "Aspen HYSYS" "case file"
- "Aspen HYSYS" ".hsc"
- "HYSYS XML Cases" ".xml"
- "process simulation" "flowsheet" "experimental data"
- LNG, 
atural gas sweetening, methanol, hydrogen, CO2 capture

## Downloaded New Cases (A/B/C)
- None this run.
- Reason: all model-bearing public candidates were either exact duplicates (same .hsc SHA256 as existing CASE assets) or lacked explicit redistribution-safe licensing.

## Candidate/Probe Summary (recorded in sources.json)
1. shahria-sunny/Natural-Gas-Sweetening
- Source: https://github.com/shahria-sunny/Natural-Gas-Sweetening
- Model found: Gas Sweetening.hsc
- Dedupe: SHA256 cda7509...d4610 equals existing 2026-05-11-heartbeat-0741Z asset.
- Decision: skip download (duplicate).

2. shahria-sunny/CDU-Simulation-Optimization
- Source: https://github.com/shahria-sunny/CDU-Simulation-Optimization
- Model found: project.hsc
- Dedupe: SHA256 795c3587...fbdd2 equals existing 2026-05-11-heartbeat-0741Z asset.
- Decision: skip download (duplicate).

3. CristopherCano/Projects-ASPEN-HYSYS
- Source: https://github.com/CristopherCano/Projects-ASPEN-HYSYS
- Models found: 15 .hsc files (+ PDF/CSV/README)
- License/public access note: no LICENSE file detected in snapshot.
- Decision: candidate only, not ingested until redistribution permission is explicit.

4. Paryazdan/Aspen-HYSYS-Projects
- Source: https://github.com/Paryazdan/Aspen-HYSYS-Projects
- Model found: YazdanihaPHw3aSim.hsc
- License/public access note: no LICENSE file detected.
- Decision: candidate only.

5. kush1706/Methanol_Synthesis_Aspen_hysys
- Source: https://github.com/kush1706/Methanol_Synthesis_Aspen_hysys
- Model found: GROUP_17.hsc.hsc
- License/public access note: no LICENSE file detected.
- Decision: candidate only.

6. Mendeley cny3h66vx8
- Source: https://data.mendeley.com/datasets/cny3h66vx8
- License/public access: CC BY 4.0
- Files exposed: DOC only, no .hsc/.xml.
- Decision: candidate only (not a runnable HYSYS package).

7. Mendeley g5k7tndk77
- Source: https://data.mendeley.com/datasets/g5k7tndk77
- License/public access: CC BY 4.0
- Files exposed: XLSX only, metadata mentions HYSYS 10.1 method, no .hsc/.xml.
- Decision: candidate only.

## Local Artifacts
- rtifacts/github_probe_candidates.json
- rtifacts/mendeley_cny3h66vx8_metadata.json
- rtifacts/mendeley_g5k7tndk77_metadata.json

## Recommended Automation Uses
- Use duplicate SHA hits as regression tests for dedupe pipeline.
- Use license-unclear candidates as manual legal triage queue.
- Use Mendeley spreadsheet-only candidates for data-ingestion tests (not solver-case execution).

## Residual Risks
- Public GitHub repositories without explicit LICENSE remain redistribution-uncertain.
- GitHub API anonymous rate limits constrained metadata retrieval; codeload snapshot probing was used as fallback.
- No model execution performed; all model_run_status remain 
ot_run.

## Next Suggestions
1. Add a strict policy hook: reject ingestion if LICENSE file absent.
2. Prioritize repository families with explicit open licenses + .hsc + README/report combos.
3. Add optional LFS/size guard before future commits to avoid >100MB push rejection regressions.

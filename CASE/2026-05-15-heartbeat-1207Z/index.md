# CASE Heartbeat 2026-05-15 1207Z

## 1. Run Time

- Trigger UTC time: 2026-05-15T12:07:51.352Z
- Local workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-15-heartbeat-1207Z
- Artifacts directory: CASE/2026-05-15-heartbeat-1207Z/artifacts
- Model run status: not_run for all entries; no HYSYS model, script, notebook, workbook, macro or executable was run.

## 2. Searched Mining Areas

- GitHub repository search, focused on high-signal HYSYS topic terms and license terms.
- GitHub tree inspection for unseen repositories returned by those searches.
- Zenodo, Figshare and Harvard Dataverse public metadata searches.
- Existing CASE dedupe pass over 27 prior sources.json files and 143 source entries.

## 3. Keywords Used

- GitHub: `HYSYS GOSP`, `HYSYS gas oil separation`, `HYSYS natural gas hsc`, `HYSYS LNG hsc`, `HYSYS CO2 capture hsc`, `HYSYS methanol hsc`, `HYSYS syngas hsc`, `HYSYS ammonia hsc`, `HYSYS hydrogen hsc`, `Aspen HYSYS simulation file`, `Aspen HYSYS case file`, `HYSYS hsc license:mit`.
- Zenodo/Figshare/Dataverse: `Aspen HYSYS .hsc`, `Aspen HYSYS .hscz`, `Aspen HYSYS case file`, `Aspen HYSYS simulation file`, `Aspen HYSYS model validation`, `Aspen HYSYS experimental data`, `Aspen HYSYS CO2 capture supplementary`, `Aspen HYSYS LNG supplementary`.

## 4. Downloaded Case List

No new HYSYS model payload was downloaded in this run.

Reason: no new source satisfied all requirements: public/legal, non-duplicate, clear license or archiving rights, and containing a qualifying HYSYS model file.

## 5. Candidate Findings

### D - LNG niching metaheuristics HYSYS optimization code

- Source page: https://github.com/M-Hamdy-M/lng-niching-metaheuristics
- Download URL considered: https://github.com/M-Hamdy-M/lng-niching-metaheuristics
- Local evidence: `artifacts/github-1207-tree-summary.json`
- Selection reason: HYSYS/LNG optimization lead with Python notebooks/code.
- Skip reason: no `.hsc`, `.hscz`, HYSYS XML `.xml`, or `.compound` file in the repository tree.
- Recommended automation use: reference only for optimization patterns; not a benchmark case.

### D - HYSYS GOSP design README candidate

- Source page: https://github.com/Ambercozy/HYSYS-GOSP-Design
- Download URL considered: https://github.com/Ambercozy/HYSYS-GOSP-Design
- Local evidence: `artifacts/github-1207-tree-summary.json`
- Selection reason: GOSP/HYSYS query hit.
- Skip reason: README-only repository, no model payload.
- Recommended automation use: manual lead only.

### D - CrBlend-ML HYSYS connector lead

- Source page: https://github.com/Jimohmuktar/CrBlend-ML
- Download URL considered: https://github.com/Jimohmuktar/CrBlend-ML
- Local evidence: `artifacts/github-1207-tree-summary.json`
- Selection reason: contains Python HYSYS connector-oriented code.
- Skip reason: no HYSYS model file.
- Recommended automation use: possible connector-reference lead, not a case benchmark.

## 6. Data Repository Results

- Zenodo returned known duplicate HYSYS-related records and non-qualifying payloads such as PDF/XLSX/.lnr/.apw. No new `.hsc/.hscz/HYSYS XML/.compound` payload was downloaded.
- Figshare returned broad irrelevant results for HYSYS terms; no qualifying model was identified.
- Harvard Dataverse returned mostly unrelated `HSC` abbreviation hits or generic supplementary material; no qualifying model was identified.

## 7. Quality Ratings

- No A/B/C new downloads were added.
- D entries record no-model leads and metadata-only repository sweeps.

## 8. Safety Notes

- No model payload, PDF, spreadsheet, notebook or script was downloaded in this run.
- Final committed artifacts are JSON metadata plus `index.md` and `sources.json` only.
- Security inventory reports no executable or macro-like files.

## 9. Residual Risks

- GitHub repository search may miss binary model files not referenced in README.
- Figshare and Dataverse searches produced noisy false positives and need stronger filters.
- Some no-model leads may later gain model files or licenses and should be rechecked only if their repository tree changes.

## 10. Follow-up Recommendations

1. Add suppression rules for README-only/no-model leads: `Ambercozy/HYSYS-GOSP-Design`, `M-Hamdy-M/lng-niching-metaheuristics`, and `Jimohmuktar/CrBlend-ML`.
2. Keep Zenodo 14882867 on the duplicate allowlist.
3. Continue GitHub repository-tree scanning for HYSYS binaries, but require model-file presence before saving individual repo metadata.
4. Add stricter Figshare/Dataverse filters to reduce irrelevant abbreviation hits.

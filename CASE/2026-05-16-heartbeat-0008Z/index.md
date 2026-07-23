# CASE Heartbeat 2026-05-16 0008Z

## 1. Run Time

- Trigger UTC time: 2026-05-16T00:08:05.749Z
- Local workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-16-heartbeat-0008Z
- Artifacts directory: CASE/2026-05-16-heartbeat-0008Z/artifacts
- Model run status: not_run for all entries; no HYSYS model, script, notebook, workbook, macro or executable was run.

## 2. Searched Mining Areas

- GitHub repository search, focused on dynamic simulation, distillation, amine sweetening, dehydration, acid gas, HYSYS V12/V14, `.hscz`, `.compound`, supplementary and validation terms.
- GitHub tree inspection for unseen repositories returned by those searches.
- Zenodo, Figshare and Harvard Dataverse public metadata searches.
- Existing CASE dedupe pass over 28 prior sources.json files and 148 source entries.

## 3. Keywords Used

- GitHub: `HYSYS dynamic simulation hsc`, `HYSYS distillation hsc`, `HYSYS amine hsc`, `HYSYS dehydration hsc`, `HYSYS acid gas hsc`, `Aspen HYSYS V12 hsc`, `Aspen HYSYS V14 hsc`, `HYSYS hscz`, `HYSYS compound`, `HYSYS supplementary hsc`, `HYSYS validation hsc`, `HYSYS hsc license:mit`.
- Data repositories: `Aspen HYSYS dynamic simulation hsc`, `Aspen HYSYS distillation hsc`, `Aspen HYSYS amine sweetening hsc`, `Aspen HYSYS dehydration hsc`, `Aspen HYSYS V12 hsc`, `Aspen HYSYS hscz`, `Aspen HYSYS supplementary hsc`.

## 4. Downloaded Case List

No new HYSYS model payload was downloaded in this run.

Reason: no new source satisfied all requirements: public/legal, non-duplicate, clear license or archiving rights, and containing a qualifying HYSYS model file.

## 5. Candidate Findings

### D - ML for DME Optimization HYSYS-adjacent lead

- Source page: https://github.com/AdityaSharma911/ML-for-DME-Optimization-
- Local evidence: `artifacts/github-0008-tree-summary.json`
- License/public access note: MIT metadata was visible, but no HYSYS model file exists in the tree.
- Recommended automation use: none as a benchmark case unless a public `.hsc/.hscz/HYSYS XML/.compound` file is added later.

### D - CheProcess thermodynamic package lead

- Source page: https://github.com/AhmadAlsaadi/CheProcess
- Local evidence: `artifacts/github-0008-tree-summary.json`
- License/public access note: GPL-3.0 metadata was visible, but no HYSYS model file exists in the tree.
- Recommended automation use: reference only; not a HYSYS model benchmark.

### D - DWSIM interop services lead

- Source page: https://github.com/OntoLedgy/ol_dwsim_interop_services
- Local evidence: `artifacts/github-0008-tree-summary.json`
- License/public access note: AGPL-3.0 metadata was visible, but no HYSYS model file exists in the tree.
- Recommended automation use: interop reference only; not a HYSYS benchmark case.

## 6. Data Repository Results

- Zenodo returned mostly PDF/XLSX records, `.lnr/.apw` records, or known duplicate HYSYS-related records; no new qualifying HYSYS model payload was downloaded.
- Figshare returned broad irrelevant results for HYSYS terms; no qualifying model was identified.
- Harvard Dataverse returned mostly unrelated `HSC` abbreviation hits or generic simulation datasets; no qualifying model was identified.

## 7. Quality Ratings

- No A/B/C new downloads were added.
- D entries record no-model leads and metadata-only repository sweeps.

## 8. Safety Notes

- No model payload, PDF, spreadsheet, notebook or script was downloaded in this run.
- Final committed artifacts are JSON metadata plus `index.md` and `sources.json` only.
- Security inventory reports no executable or macro-like files.

## 9. Residual Risks

- GitHub search can miss binary `.hsc/.hscz` files not referenced in README.
- Figshare and Dataverse searches continue to produce noisy false positives for HYSYS/HSC-like terms.
- No-model leads may later add model files and should only be revisited when the repository tree changes.

## 10. Follow-up Recommendations

1. Suppress no-model compound-query false positives in future sweeps.
2. Keep repository-tree inspection as the model-file gate before saving individual repo metadata.
3. Keep prior Zenodo HYSYS records on the duplicate allowlist.
4. Add stronger Figshare/Dataverse filters for file names/extensions before recording candidates.

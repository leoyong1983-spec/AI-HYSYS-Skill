# AGENTS.md

## Mission

Keep this repository installable, reviewable, and trustworthy as an AI-ready HYSYS skill. Favor small, high-confidence improvements over speculative expansion.

## Repository Map

- `SKILL.md` is the primary skill contract.
- `references/` contains the domain guardrails that explain control-lane choice, package deliverables, and project lessons.
- `CASE/` contains the public source pack, digest notes, and release-positioning material for the open-source repo.
- `scripts/hysys_automation.py` is a reusable direct COM starter wrapper.
- `scripts/hysys_readiness_check.py` verifies real Windows/HYSYS runtime readiness when Aspen HYSYS is available.
- `scripts/hysys_h2_density_table.py` is a minimal native HYSYS property-table smoke calculation for pure hydrogen.
- `scripts/hysys_pfd_layout.py` reorganizes a native PFD on a workcopy and verifies calculation fingerprints after reopen.
- `scripts/sync_installed_skill.ps1` safely synchronizes the validated `origin/main` runtime payload to the local Codex skill installation with backup, local-edit detection, and hash verification.
- `references/pfd-layout-workflow.md` records the verified V15 PFD COM sequence and visual handoff rules.
- `agents/openai.yaml` contains the Codex-facing UI metadata.
- `scripts/validate_repo.ps1` is the preferred local validation entry point on Windows.
- `scripts/validate_repo.py` is the lightweight repository smoke test.
- `.github/` contains collaboration, dependency, and CI hygiene for the open-source repo.

## Source Hierarchy

Use external knowledge in this order:

1. Official AspenTech HYSYS and Aspen Simulation Workbook product/support/training pages
2. Proven project-local HYSYS runners, logs, and validated workcopies
3. Public bridge examples such as spreadsheet-driven Python control
4. Recent AI-for-HYSYS research when it materially informs the workflow
5. Secondary community material only as fallback

## Maintenance Priorities

1. Fix install failures, broken links, README-to-repo drift, missing validation, and open-source hygiene gaps first.
2. Prefer low-risk improvements that can be reviewed in a small branch or PR.
3. Keep the repository lightweight; do not add large dependencies or speculative frameworks.
4. Preserve the current project positioning as an auditable, script-first HYSYS skill for review-stage basic process packages.
5. Treat Chinese reader-facing content carefully and verify encoding before editing.

## Guardrails

- Do not change the license without maintainer approval.
- Do not commit secrets, credentials, proprietary plant data, private case files, or personal machine paths.
- Do not claim Aspen HYSYS runtime validation unless a real local HYSYS environment was available and exercised.
- Do not relabel external EOS calculations or fitted data as HYSYS-native results; native results must come from a HYSYS object/property readback.
- Do not silently upgrade the scope from basic process package support to detailed design.
- Do not replace official HYSYS behavior with speculative wrapper behavior.

## Validation

After repository-facing changes, run:

```powershell
.\scripts\validate_repo.ps1
```

If you add or change GitHub workflows, keep them dependency-light and explain any schedule or timezone assumptions in the workflow or PR description.

## Safe Change Areas

These are normally safe to improve without extra approval:

- documentation consistency
- installation instructions
- CASE indexing and digest notes
- issue and pull request templates
- SECURITY / CONTRIBUTING guidance
- lightweight GitHub Actions and Dependabot configuration
- repository smoke tests that do not require Aspen HYSYS binaries

Use an issue or maintainer note instead of direct edits for major roadmap changes, architectural repositioning, or large dependency additions.

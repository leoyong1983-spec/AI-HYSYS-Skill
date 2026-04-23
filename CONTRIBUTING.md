# Contributing to AI-HYSYS-Skill

## Scope

This repository packages a reusable Codex skill and workflow for auditable Aspen HYSYS automation. Contributions should strengthen installability, documentation accuracy, reviewability, source provenance, and lightweight repository maintenance.

## Good First Contribution Areas

- fix broken links or outdated instructions
- improve README, references, or CASE index clarity
- add lightweight repository validation
- tighten issue, PR, and release hygiene
- improve examples or prompts without changing project scope

## Before You Start

1. Keep changes small and reviewable.
2. Open or reference an issue first for large design changes, policy changes, or new dependency proposals.
3. Do not change the license, project positioning, or baseline workflow philosophy without maintainer approval.

## Development Expectations

1. Work from a branch instead of committing directly to `main`.
2. Keep HYSYS-facing claims auditable and source-backed.
3. Do not add secrets, private simulation data, exported plant data, or personal machine paths.
4. If a change could affect user-facing behavior, update the relevant documentation in the same branch.

## Validation

Run the repository smoke test before submitting a PR:

```powershell
.\scripts\validate_repo.ps1
```

If you could not run a check because the environment lacks Python, Aspen HYSYS, COM automation, Excel/workbook access, or another required tool, say so clearly in the PR.

## Pull Request Expectations

Each pull request should explain:

1. the problem being solved
2. the change made
3. how it was validated
4. remaining risks or follow-up work

Use the pull request template and keep follow-up ideas separate from the core fix when possible.

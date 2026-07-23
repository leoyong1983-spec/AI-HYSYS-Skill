# Heartbeat scan 2026-05-22

Automation ID: `ai-hysys-daily-scan`

Worktree used: `D:\SKILL\AI-HYSYS-Skill-heartbeat-main`

## Search focus

Searched for latest credible sources around Aspen HYSYS automation, COM/Python/spreadsheet/workbook control, public package examples, LLM agents for process simulation, AspenTech AVA, digital twins, and hybrid AI workflows.

## New valuable source

### aspen_pysys PyPI / Codeberg candidate

- PyPI JSON: [../community/aspen-pysys-pypi-json-2026-05-22.json](../community/aspen-pysys-pypi-json-2026-05-22.json)
- Codeberg snapshot: [../community/aspen-pysys-codeberg-page-2026-05-22.html](../community/aspen-pysys-codeberg-page-2026-05-22.html)
- PyPI project: https://pypi.org/project/aspen-pysys/
- Codeberg repository: https://codeberg.org/CacklingTanuki/aspen-pysys
- Version observed: `0.1.0a0`
- Upload time: 2026-05-20
- License expression: `GPL-3.0-or-later`
- Requires Python: `>=3.12.12`
- Requires dist: `pywin32>=311`
- Wheel SHA256: `f1df2b0c6852c58ffc9a976835bed72061b90be20ca6bf335387b5529c374d5a`
- Source distribution SHA256: `8cb0e699ee34c273a549bbaea6f39b14167692445965467d82d57b5ee318956a`
- Quality: B-
- Category: community candidate wrapper

## Value judgment

This source is worth adding because a previously indexed `aspen-pysys` candidate now has real PyPI metadata, a Codeberg repository, and a released alpha wheel/source distribution. It is directly relevant to HYSYS + Python automation discovery and corrects the older 2026-05-17 note that no releases were available.

It should remain candidate-only for this repository. The package is alpha, GPL-licensed, unverified in this local HYSYS runtime, and requires a narrow Python/pywin32 stack. Its own setup guidance still assumes an existing HYSYS simulation case can be opened or attached; it does not prove reliable from-scratch model generation.

## Lower-value findings

- Piwheels requests intermittently failed during this scan, so PyPI JSON and Codeberg snapshots were used as the stronger evidence.
- A PyPI browser page request returned a client-challenge page and was not committed.
- Generic AI/process-industry material was ignored because it did not improve HYSYS control, readiness, or boundary decisions.

## Project updates made

- Added PyPI JSON metadata and Codeberg repository snapshot under `CASE/community`.
- Updated `CASE/source-index.md`.
- Updated `CASE/notes/hysys-source-digest.md`.
- Updated `README.md`.
- Updated `SKILL.md` and `references/authority-and-path-selection.md` to keep third-party wrappers candidate-only until runtime, license, and project-fit checks pass.

## Safety notes

- No proprietary case files were added.
- No `.hsc`, `.hscz`, installer, executable, wheel, source distribution, or raw plant data file was added.
- Only metadata and repository page snapshots were saved; the GPL package artifact itself was not vendored into this MIT repository.

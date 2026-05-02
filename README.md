# AI-HYSYS-Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
![HYSYS](https://img.shields.io/badge/Aspen_HYSYS-COM_Automation-blue)
![Bridge](https://img.shields.io/badge/Spreadsheet-Workbook_Bridge-yellow)
![Case Library](https://img.shields.io/badge/CASE-Public_Source_Pack-orange)

An AI-driven Aspen HYSYS automation and basic process package toolkit.

This repository packages a reusable skill, source pack, and workflow for engineers who want to let an AI agent take over Aspen HYSYS in a controlled, auditable, script-first way.

It is designed for real execution, not just documentation. The workflow covers:

- Aspen HYSYS environment readiness checks
- `HYSYS.Application` COM takeover
- spreadsheet / workbook bridge control for stable tagged IO
- existing-case loading and bounded modification
- bounded tuning and sensitivity runs
- baseline freezing
- machine-readable exports
- review-stage basic process package generation
- release gate and blocker control

## What This Is

This repository is built around a simple idea:

1. Use official Aspen HYSYS capabilities as the authority layer
2. Use Python and PowerShell as orchestration layers
3. Keep every major action reproducible, reviewable, and exportable

The skill is optimized for projects such as:

- gas processing
- LNG and cryogenic studies
- refining unit studies
- dehydration / AGR / sulfur systems
- other process packages that need a repeatable HYSYS-to-package workflow

## Core Design Principles

- Script first, GUI last
- Prefer proven project runners over ad hoc clicks
- Prefer direct `HYSYS.Application` control as the primary execution lane
- Use spreadsheets or Aspen Simulation Workbook when object paths are fragile but named cells are stable
- Never overwrite a frozen baseline
- Always leave machine-auditable artifacts on disk
- Separate launch issues, case loading issues, object binding issues, and solver issues
- Treat release blockers and human decisions as first-class controls
- Prefer takeover of a human-built, already-runnable HYSYS case over AI greenfield case construction

## Recommended Control Stack

Preferred execution order:

1. existing proven project runner
2. direct `HYSYS.Application` COM automation
3. HYSYS spreadsheet / Aspen Simulation Workbook bridge
4. HYSYS data tables or special-object lanes when already configured in the case
5. Excel / VBA, Matlab, C#, or intermediate-file bridges only if they already exist and are working
6. GUI only for layout sign-off or unavoidable visual checks

This recommendation is now captured as an actionable decision matrix in [references/control-lane-decision-matrix.md](references/control-lane-decision-matrix.md). The recommendation is based on five source classes collected in [CASE/source-index.md](CASE/source-index.md):

- official AspenTech HYSYS and Aspen Simulation Workbook product pages
- public AspenTech support articles for Jump Start and Customization Guide entry points
- community HYSYS spreadsheet-bridge examples
- peer-reviewed HYSYS interconnection and Python-HYSYS automation papers
- recent AI-for-HYSYS research on multi-agent flowsheet generation, digital twins, LNG optimization, production planning, and ML surrogate models

## Repository Structure

```text
AI-HYSYS-Skill/
|-- README.md
|-- SKILL.md
|-- AGENTS.md
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- LICENSE
|-- GITHUB_REPO_SETTINGS.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- authority-and-path-selection.md
|   |-- basic-package-deliverables.md
|   |-- control-lane-decision-matrix.md
|   |-- digital-twin-boundary.md
|   `-- project-lessons.md
|-- scripts/
|   |-- hysys_automation.py
|   |-- validate_repo.ps1
|   `-- validate_repo.py
|-- CASE/
|   |-- source-index.md
|   |-- community/
|   |-- official/
|   |-- research/
|   `-- notes/
`-- .github/
    |-- dependabot.yml
    |-- pull_request_template.md
    |-- ISSUE_TEMPLATE/
    `-- workflows/
```

## Requirements

Minimum practical requirements:

- Windows
- Aspen HYSYS installed locally
- a working `HYSYS.Application` COM registration

Optional but useful:

- Python for orchestration and batch workflows
- Excel or Aspen Simulation Workbook for spreadsheet-bridge control
- project-local runner scripts or templates

## Quick Start

### 1. Clone the repository

```powershell
git clone https://github.com/leoyong1983-spec/AI-HYSYS-Skill.git
cd AI-HYSYS-Skill
```

### 2. Install it as a Codex skill

Copy the repository contents into a Codex skill folder named `ai-hysys-basic-package`.

```powershell
$source = Get-Location
$target = "$env:USERPROFILE\\.codex\\skills\\ai-hysys-basic-package"
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item `
  "$source\\README.md", `
  "$source\\SKILL.md", `
  "$source\\AGENTS.md", `
  "$source\\agents", `
  "$source\\references", `
  "$source\\scripts", `
  "$source\\CASE" `
  -Destination $target -Recurse -Force
```

### 3. Use it in a real HYSYS task

Example prompts:

```text
Use ai-hysys-basic-package to verify the Aspen HYSYS environment, prove the working control lane, and report whether direct COM or spreadsheet bridge is the safer path.
```

```text
Use ai-hysys-basic-package to open the latest valid HYSYS case, run a bounded update, and export key streams, unit operations, utility summary, status, and open issues.
```

```text
Use ai-hysys-basic-package to freeze the accepted HYSYS case as a review-stage baseline and prepare machine-readable package outputs.
```

### Option A: Use it as a Codex skill

Copy this repository into your Codex skills directory under the folder name `ai-hysys-basic-package`.

Typical local path:

```powershell
$skillPath = "$env:USERPROFILE\\.codex\\skills\\ai-hysys-basic-package"
```

Then invoke it in a task such as:

- `Use ai-hysys-basic-package to take over Aspen HYSYS, run a COM smoke test, and export key streams and equipment.`
- `Use ai-hysys-basic-package to decide whether direct COM or spreadsheet bridge is the safer automation lane for this case.`
- `Use ai-hysys-basic-package to freeze the current workcopy as a review-stage baseline and generate package exports.`

### Option B: Use it as a workflow reference in your own repository

If you do not use Codex skills directly, you can still reuse:

- `SKILL.md` as the operating playbook
- `AGENTS.md` as the repository-specific maintenance contract for AI coding agents
- `references/authority-and-path-selection.md` to choose the correct control lane
- `references/control-lane-decision-matrix.md` to turn COM, spreadsheet/workbook, data tables, indirect bridges, and GUI fallback into a concrete decision
- `references/digital-twin-boundary.md` to use official HYSYS digital twin / hybrid AI evidence without overclaiming direct control
- `references/project-lessons.md` to avoid known failure modes
- `references/basic-package-deliverables.md` to structure exports and review-stage package outputs
- `CASE/` as a public source pack and launch-positioning library

## CASE Folder

`CASE/` is a curated public source pack prepared on 2026-04-21 (Asia/Shanghai). It is grouped into:

- `official/` for AspenTech product and support pages
- `community/` for public bridge examples and sample HYSYS case files
- `research/` for recent AI-for-HYSYS academic material
- `notes/` for Chinese digest notes and a release playbook

Start with [CASE/source-index.md](CASE/source-index.md) and [CASE/notes/hysys-source-digest.md](CASE/notes/hysys-source-digest.md).

## Maintenance and Validation

This repository includes lightweight open-source maintenance scaffolding:

- `AGENTS.md` for repository-specific AI agent instructions
- `CONTRIBUTING.md` for contribution scope and review expectations
- `SECURITY.md` for vulnerability reporting guidance
- `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md` for consistent collaboration
- `.github/workflows/repo-hygiene.yml` for push, pull request, manual, and daily repository checks
- `scripts/validate_repo.ps1` as the Windows-friendly local validation entry point
- `scripts/validate_repo.py` for the underlying repository smoke checks without requiring Aspen HYSYS

Run the local validation entry point after repository-facing changes:

```powershell
.\scripts\validate_repo.ps1
```

The PowerShell wrapper prefers a real Python installation behind `py` or `python` and fails with a clear message if neither is available.

## Typical Workflow

1. Verify the environment
2. Choose the control lane with [references/control-lane-decision-matrix.md](references/control-lane-decision-matrix.md)
3. Prove the control lane with a smoke test
4. Reuse an existing valid case if possible
5. Only consider a minimal experimental case for smoke tests after all candidate cases fail, and do not treat that path as a production default
6. Run calculations and classify failures correctly
7. Perform bounded tuning only when explicitly allowed
8. Freeze the accepted case as a baseline
9. Export machine-readable results
10. Compile review-stage package deliverables
11. Run release-gate checks before issue

## What Good Output Looks Like

A good run should leave artifacts such as:

- `case_summary.json`
- `key_streams.csv`
- `key_operations.csv`
- `utility_summary.csv`
- `assumptions.md`
- `open_issues.md`
- `run_status.md`
- baseline or workcopy traceability
- review-stage package outputs when requested

## What This Toolkit Does Not Do By Default

It does not assume:

- detailed design is complete
- a frozen baseline may be overwritten
- free tuning remains allowed after the project enters review-stage package work
- human decision items may be closed automatically by AI
- GUI clicking is the primary automation strategy
- AI can reliably build a production-ready HYSYS case from zero without a validated baseline

## References

Official AspenTech pages:

- [Aspen HYSYS product page](https://www.aspentech.com/en/products/engineering/aspen-hysys)
- [Aspen Simulation Workbook product page](https://www.aspentech.com/en/products/engineering/aspen-simulation-workbook)
- [AspenTech course catalog PDF](https://www.aspentech.com/-/media/aspentech/home/customer-help/aspentech-course-catalog.pdf?hash=35328F62068FD84D73AB9A55D8197071&sc_lang=en)
- [Aspen HYSYS V8.0 Jump Start article](https://esupport.aspentech.com/S_Article?id=000060539)
- [Aspen HYSYS V7.3 Customization Guide article](https://esupport.aspentech.com/s_Article?key=131879)
- [Aspen HYSYS 2025 brochure PDF](https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy25/q4/at-4162_bro_aspen-hysys_final_0525.pdf)
- [AspenTech performance engineering digital twin case study](https://www.aspentech.com/en/resources/case-studies/energy-company-saves-%246m-usd-with-a-performance-engineering-digital-twin)
- [AspenTech process simulation digital twin article](https://www.aspentech.com/en/resources/articles/utilize-a-process-simulation-digital-twin-to-optimize-condensate-yield)
- [AspenTech V15 What's New](https://solutions.aspentech.com/en/whats-new)
- [AspenTech EHM105 AI-Powered Digital Twins course](https://esupport.aspentech.com/UniversityCourse?id=a3pUn0000028hg9IAA)
- [Aspen HYSYS Dynamics product page](https://www.aspentech.com/en/products/engineering/aspen-hysys-dynamics)
- [Deploy Simulation Models Online Easily Gain Unrivaled Process Insights](https://www.aspentech.com/en/resources/on-demand-webinars/deploy-simulation-models-online-easily-gain-unrivaled-process-insights)

Community bridge example:

- [edgarsmdn/Aspen_HYSYS_Python](https://github.com/edgarsmdn/Aspen_HYSYS_Python)

Recent AI paper:

- [Sketch2Simulation (arXiv:2603.24629)](https://arxiv.org/abs/2603.24629)
- [From Text to Simulation (arXiv:2601.06776)](https://arxiv.org/abs/2601.06776)
- [Large Language Model Agent for User-friendly Chemical Process Simulations (arXiv:2601.11650)](https://arxiv.org/abs/2601.11650)
- [PINN Digital Twin for Aspen HYSYS generated dynamic data (arXiv:2603.24644)](https://arxiv.org/abs/2603.24644)
- [Data-driven simulation of crude distillation using Aspen HYSYS and comparative machine learning models](https://doi.org/10.1002/cjce.70297)
- [AI-driven surrogate modeling for LNG process optimization](https://doi.org/10.1016/j.jclepro.2026.148110)
- [HEFA/SAF production planning surrogate model paper](https://www.sciencedirect.com/science/article/pii/S009813542600102X)

HYSYS automation and interconnection papers:

- [Hydrogen liquefaction study using Aspen HYSYS V12 with Python COM automation](https://www.sciencedirect.com/science/article/abs/pii/S0360319925061464)
- [Integrating coding platforms with process simulators for custom applications](https://www.sciencedirect.com/science/article/pii/S0098135425002510)
- [A comparative study on Aspen HYSYS interconnection methodologies](https://papers.sim2.be/assets/uploads/files/1c6ba-communicationarticle.pdf)

## Publishing Note

This repository ships with the MIT license and a prepared [GITHUB_REPO_SETTINGS.md](GITHUB_REPO_SETTINGS.md) file.

If you publish this repository on GitHub, copy the values from that file into the repository "About" section and keep `CASE/` in the public tree so the positioning remains source-backed.

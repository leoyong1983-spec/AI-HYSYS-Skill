# PySIS Candidate Metadata - 2026-06-20

## Source

- Repository: https://github.com/DanielVazVaz/PySIS
- README snapshot: `CASE/community/pysis-danielvazvaz-readme-2026-06-20.md`
- GitHub metadata snapshot: `CASE/community/pysis-danielvazvaz-github-metadata-2026-06-20.json`
- Setup snapshot: `CASE/community/pysis-danielvazvaz-setup-2026-06-20.py`

## Observed Metadata

- Description: Abstract layer over Aspen HYSYS using Python.
- Default branch: `master`.
- Last observed update: 2026-05-26.
- GitHub API license field: `null`.
- `setup.py` license classifier/name: MIT.
- README claims checked use with Aspen HYSYS V11, V12, and V14.
- README describes the package as an abstraction layer over the COM HYSYS interface using Python.
- Dependency declared by `setup.py`: `pywin32>=225`.
- Development status classifier: Pre-Alpha.

## Value Grade

Grade: **B-/C+ direct community wrapper candidate**

PySIS is directly relevant because it targets Aspen HYSYS and wraps the COM interface in Python. It is useful as a design reference for object abstraction, COM wrapper ergonomics, and version-compatibility notes.

It is not promoted to a default dependency because it is a small community repository, GitHub license detection is absent, the package advertises pre-alpha status, and this heartbeat did not validate it against a local licensed HYSYS runtime.

## Adoption Boundary

Use this source only as candidate wrapper evidence. Do not replace AI-HYSYS-Skill's default direct COM and spreadsheet/workbook bridge lanes with PySIS unless a real project runner proves runtime value, license compatibility, and recovery behavior.

Do not claim that PySIS proves safe production writeback, reliable from-scratch HYSYS model generation, or autonomous HYSYS control.

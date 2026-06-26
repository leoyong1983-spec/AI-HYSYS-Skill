# HYSYS Python Case Builder

Python scripts for creating, opening, and modifying Aspen HYSYS case files through the COM interface.

## Repository Description

This repository contains small Python automation scripts that connect to Aspen HYSYS, create `.hsc` simulation files, configure fluid packages and streams, and build simple flowsheet elements such as heaters, splitters, and energy streams.

## Included Scripts

- `Hysys_python_creator.py`: creates or opens a HYSYS case and adds a basic fluid package with oxygen.
- `Hysys_python_flowsheet.py`: creates or updates a simple flowsheet with streams, a heater, and an energy stream.
- `EXtest.py`: builds a larger example with heat exchangers and a tee splitter.
- `HYSYS_python_simulation.py`: runs a higher-level example using the spreadsheet connection helper.
- `HYSYS_python_spreadsheets_creator.py`: helper module used to connect Python to an existing HYSYS case.
- `HyCOM_DIC_creator.py`: explores the HYSYS COM object model and writes attributes to a text file.

## Path Configuration

Private local paths were removed from the publishable version of this project.

The shared path configuration is in `project_paths.py`.

By default, HYSYS case files are read from and saved into the same folder as the clean copy:

```python
HYSYS_WORKDIR = Path(__file__).resolve().parent
```

If you want to store the `.hsc` files in another location, update that variable to your own folder, for example:

```python
HYSYS_WORKDIR = Path(r"C:\path\to\your\hysys\workspace")
```

## Requirements

- Windows
- Aspen HYSYS installed
- Python with `pywin32`

Install the Python dependency with:

```powershell
pip install pywin32
```

## Basic Usage

1. Make sure Aspen HYSYS is installed and accessible through COM.
2. Review `project_paths.py` and adjust `HYSYS_WORKDIR` if needed.
3. Run one of the scripts, for example:

```powershell
python Hysys_python_creator.py
```

## Notes

- These scripts assume a Windows environment because Aspen HYSYS COM automation is Windows-based.
- Some scripts expect specific components, operations, or reaction packages to exist in the target case.
- Generated `.hsc`, `.bk0`, and exported text files are not required as source code and can be excluded from publication if desired.

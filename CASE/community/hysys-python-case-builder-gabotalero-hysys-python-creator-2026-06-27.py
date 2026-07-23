import win32com.client
from pathlib import Path

from project_paths import HYSYS_WORKDIR, get_case_path

new_file_name = "Test4.hsc"
new_file_path = get_case_path(new_file_name)


# Ensure folder exists
Path(HYSYS_WORKDIR).mkdir(parents=True, exist_ok=True)

# Start or connect to Aspen HYSYS
try:
    HyApp = win32com.client.GetActiveObject("HYSYS.Application")  # Attach to an existing instance
    print("Connected to an existing HYSYS session.")
except Exception:
    HyApp = win32com.client.Dispatch("HYSYS.Application")  # Start a new instance
    print("Started a new HYSYS session.")

HyApp.Visible = True  # Make it visible

# === CHECK IF FILE EXISTS ===
if Path(new_file_path).exists():
    print(f"Opening existing HYSYS file: {new_file_path}")
    HyCase = HyApp.SimulationCases.Open(new_file_path)
else:
    print(f"Creating new HYSYS file: {new_file_path}")
    HyCase = HyApp.SimulationCases.Add()
    HyCase.SaveAs(new_file_path)

HyCase.Visible = True

# === ACCESS BASIS MANAGER ===
basis_manager = HyCase.BasisManager

# === ACCESS FLUID PACKAGES ===
fluid_packages = basis_manager.FluidPackages

fluid_package = fluid_packages.Item(0) if fluid_packages.Count > 0 else fluid_packages.Add()
fluid_package.Name = "MyFluidPackage"

# Assign Property Package
fluid_package.PropertyPackageName = "PengRob"

# === Add Oxygen Component ===
components_list = fluid_package.Components
oxygen = components_list.Add("Oxygen")
print(f"Added component: {oxygen.Name}")


# === SAVE AND CLOSE HYSYS CASE ===
print("Saving HYSYS file...")
HyCase.Save()
print("File saved successfully.")

# Close HYSYS
print("Closing HYSYS...")
HyCase.Close()
HyApp.Quit()
print("HYSYS closed.")

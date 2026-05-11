import math

print("=================================================")
print(" PRESSURE DROP IN A STRAIGHT PIPE ")
print(" Darcy–Weisbach Method ")
print("=================================================")

# =========================
# STAGE 1: USER INPUTS
# =========================
Q = float(input("Enter volumetric flow rate Q (m^3/s): "))
D = float(input("Enter pipe diameter D (m): "))
L = float(input("Enter pipe length L (m): "))

rho = float(input("Enter fluid density rho (kg/m^3): "))
mu  = float(input("Enter fluid viscosity mu (Pa.s): "))

eps = float(input("Enter pipe roughness epsilon (m): "))

nK = int(input("Enter number of fittings / minor losses: "))

Ksum = 0.0
for i in range(1, nK + 1):
    Ki = float(input(f"Enter K-value for fitting {i}: "))
    Ksum += Ki

# =========================
# STAGE 2: VELOCITY & REYNOLDS NUMBER
# =========================
A = math.pi * D**2 / 4        # Cross-sectional area (m^2)
v = Q / A                    # Velocity (m/s)

Re = rho * v * D / mu        # Reynolds number

# =========================
# STAGE 3: FRICTION FACTOR
# =========================
if Re < 2300:
    flowRegime = "Laminar Flow"
    f = 64 / Re

else:
    flowRegime = "Turbulent Flow"

    print("\nSelect friction factor method:")
    print("1 → Swamee–Jain (Explicit)")
    print("2 → Colebrook (Iterative)")
    method = int(input("Enter choice (1 or 2): "))

    if method == 1:
        # Swamee–Jain equation
        f = 0.25 / (
            math.log10(eps / (3.7 * D) + 5.74 / (Re ** 0.9))
        ) ** 2
    else:
        f = None  # will be computed by Colebrook


# =========================
# COLEBROOK FUNCTION
# =========================
def colebrook(Re, eps, D):
    """Solves Colebrook equation using iteration"""
    f = 0.02      # Initial guess
    tol = 1e-6

    for _ in range(100):
        f_new = 1 / (
            -2 * math.log10(eps / (3.7 * D) + 2.51 / (Re * math.sqrt(f)))
        ) ** 2

        if abs(f_new - f) < tol:
            break

        f = f_new

    return f


# If turbulent and Colebrook selected
if Re >= 2300 and f is None:
    f = colebrook(Re, eps, D)

# =========================
# STAGE 4: FRICTIONAL PRESSURE DROP
# =========================
dp_friction = f * (L / D) * (rho * v**2 / 2)

# =========================
# STAGE 5: MINOR LOSSES
# =========================
dp_minor = Ksum * (rho * v**2 / 2)

# =========================
# TOTAL PRESSURE DROP
# =========================
dp_total = dp_friction + dp_minor

# =========================
# DISPLAY RESULTS
# =========================
print("\n================ RESULTS ================")
print(f"Flow regime            : {flowRegime}")
print(f"Velocity (m/s)         : {v:.4f}")
print(f"Reynolds number        : {Re:.3e}")
print(f"Friction factor (f)    : {f:.5f}")
print(f"Δp (friction) (Pa)     : {dp_friction:.2f}")
print(f"Δp (minor) (Pa)        : {dp_minor:.2f}")
print(f"Δp (total) (Pa)        : {dp_total:.2f}")
print("=========================================")

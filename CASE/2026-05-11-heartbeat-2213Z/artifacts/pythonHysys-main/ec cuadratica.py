import numpy as np

def resolver_ecuacion_cubica(a, b, c, d):
    # Coeficientes de la ecuación cúbica
    coeficientes = [a, b, c, d]
    # Usar numpy para encontrar las raíces
    raices = np.roots(coeficientes)
    return raices

# Ejemplo de uso
a, b, c, d = 1, 0.05, 0.05, -1.86e-5
raices = resolver_ecuacion_cubica(a, b, c, d)
print("Raíces de la ecuación cúbica:", raices)
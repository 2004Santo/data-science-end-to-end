# Ejercicio 2: usa pandas (dependencia externa) y lee/escribe datos.
# Lo resuelvo en clase junto con su Dockerfile y el volumen.

import pandas as pd

ENTRADA = "datos/ventas.csv"
SALIDA = "datos/resumen_ventas.csv"

if __name__ == "__main__":
    ventas = pd.read_csv(ENTRADA)
    resumen = ventas.groupby("producto")["monto"].sum().reset_index()
    resumen = resumen.sort_values("monto", ascending=False)
    resumen.to_csv(SALIDA, index=False)
    print("Resumen de ventas por producto:")
    print(resumen.to_string(index=False))

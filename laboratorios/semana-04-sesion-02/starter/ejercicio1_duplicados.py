import pandas as pd

datos = pd.read_csv("inscripciones.csv")
print(f"Filas totales: {len(datos)}")

duplicados = datos.duplicated()
print(f"Filas duplicadas (repiten todas las columnas): {duplicados.sum()}")

datos_limpios = datos.drop_duplicates()
print(f"Filas después de quitar duplicados: {len(datos_limpios)}")

datos_limpios.to_csv("inscripciones_limpio.csv", index=False)

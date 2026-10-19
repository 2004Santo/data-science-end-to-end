import pandas as pd

datos = pd.read_csv("sensores.csv")
print("Tipos de dato por columna:")
print(datos.dtypes)

print()
print("Valores faltantes por columna:")
print(datos.isna().sum())

datos["temperatura_numerica"] = pd.to_numeric(datos["temperatura"], errors="coerce")
print()
print(f"Filas sin temperatura numerica valida tras la conversion: {datos['temperatura_numerica'].isna().sum()}")


def normalizar_fecha(valor):
    if "/" in valor:
        return pd.to_datetime(valor, format="%d/%m/%Y")
    return pd.to_datetime(valor, format="%Y-%m-%d")


datos["fecha_normalizada"] = datos["fecha"].apply(normalizar_fecha)
print()
print("Fechas normalizadas (formato detectado y convertido de forma explicita):")
print(datos[["fecha", "fecha_normalizada"]])

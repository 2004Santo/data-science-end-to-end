import pandas as pd

# La misma ruta que usaste en la exploracion de la Semana 8: OBT del PSet 2 (ECU 911).
# Los codigos DPA se leen como texto para no perder el cero inicial (0101 = Cuenca).
datos = pd.read_csv(
    r"C:\Users\DELL\Downloads\obt_emergencias_canton_dia.csv",
    dtype={"cod_canton": str, "cod_provincia": str},
    parse_dates=["fecha"],
)

# La columna que el modelo va a predecir: el conteo de emergencias en t+3
# (de ahi sale la etiqueta y_3 de alta demanda).
OBJETIVO = "obj_n_emergencias_t3"

# Feature 1 (Hallazgo 2 de la Semana 8): emergencias de hace 4 dias en el
# mismo canton. t-4 cae el mismo dia de la semana que t+3.
datos = datos.sort_values(["cod_canton", "fecha"])
datos["lag_4d"] = datos.groupby("cod_canton")["n_emergencias"].shift(4)

# Feature 2: dia de la semana de t+3 (1 = lunes ... 7 = domingo). La fecha
# a predecir ya se conoce en t, asi que esta columna existe al predecir.
datos["dia_semana_t3"] = (datos["dia_semana"] + 2) % 7 + 1

# Evidencia: correlacion de lag_4d con el objetivo, comparada con la de
# las emergencias de hoy, dentro de un mismo canton.
for canton in ["QUITO", "GUAYAQUIL", "CUENCA"]:
    serie = datos[datos["canton"] == canton]
    print(canton, serie[["n_emergencias", "lag_4d", OBJETIVO]]
          .corr()[OBJETIVO].drop(OBJETIVO).round(3).to_dict())

# Evidencia: objetivo promedio segun el dia de la semana de t+3.
print(datos.groupby("dia_semana_t3")[OBJETIVO].mean().round(1))

print(datos[["canton", "fecha", "n_emergencias", "lag_4d", "dia_semana_t3", OBJETIVO]].head())

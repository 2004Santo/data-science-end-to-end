import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Muestra de la OBT del PSet 2 (ECU 911): 10 cantones y solo las columnas que se usan.
# Va en data/processed/ (no se sube a Git).
datos = pd.read_csv(
    "../../../data/processed/obt_emergencias_muestra.csv",
    dtype={"cod_canton": str, "cod_provincia": str},
    parse_dates=["fecha"],
)

# Las 2 features de la sesion pasada.
datos = datos.sort_values(["cod_canton", "fecha"])
datos["lag_4d"] = datos.groupby("cod_canton")["n_emergencias"].shift(4)
datos["dia_semana_t3"] = (datos["dia_semana"] + 2) % 7 + 1

# Los ultimos 3 dias de cada canton no tienen objetivo: no sirven para entrenar.
datos = datos.dropna(subset=["obj_n_emergencias_t3"])

OBJETIVO = "obj_n_emergencias_t3"
NUMERICAS = ["n_emergencias", "lag_1d", "lag_4d", "lag_7d", "media_prev_7d", "media_prev_28d"]
CATEGORICAS = ["dia_semana_t3", "cod_provincia"]
YA_LISTAS = ["es_feriado_t3"]

X = datos[NUMERICAS + CATEGORICAS + YA_LISTAS]
y = datos[OBJETIVO]

# El modelo predice el futuro a partir de filas con fecha: se divide por
# fecha, con el mismo corte de la Semana 8.
CORTE = pd.Timestamp("2025-07-01")
en_entrenamiento = datos["fecha"] < CORTE
X_ent, X_prueba = X[en_entrenamiento], X[~en_entrenamiento]
y_ent, y_prueba = y[en_entrenamiento], y[~en_entrenamiento]

preparacion = ColumnTransformer([
    ("numericas", Pipeline([
        ("imputar", SimpleImputer(strategy="median")),
        ("escalar", StandardScaler()),
    ]), NUMERICAS),
    ("categoricas", Pipeline([
        ("imputar", SimpleImputer(strategy="most_frequent")),
        ("codificar", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ]), CATEGORICAS),
    ("ya_listas", "passthrough", YA_LISTAS),
])

X_ent_listo = preparacion.fit_transform(X_ent)
X_prueba_listo = preparacion.transform(X_prueba)
print("Entrenamiento:", X_ent_listo.shape, "Prueba:", X_prueba_listo.shape)
print(list(preparacion.get_feature_names_out()))

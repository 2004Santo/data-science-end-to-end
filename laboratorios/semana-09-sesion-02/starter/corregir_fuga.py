import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

viajes = pd.read_csv('viajes_features.csv')

COLUMNAS = ['distancia_km', 'pasajeros', 'hora_sin', 'hora_cos',
            'es_fin_de_semana', 'es_hora_pico', 'es_tarifa_fija']
X = viajes[COLUMNAS].copy()
y = viajes['tarifa']

# Version con fuga: imputa y escala con TODO el dataset y despues divide.
# El conjunto de prueba entra al entrenamiento en estas dos lineas.
X_fuga = X.copy()
X_fuga[['distancia_km', 'pasajeros']] = SimpleImputer(strategy='median').fit_transform(X_fuga[['distancia_km', 'pasajeros']])
X_fuga[['distancia_km', 'pasajeros']] = StandardScaler().fit_transform(X_fuga[['distancia_km', 'pasajeros']])

X_ent, X_prueba, y_ent, y_prueba = train_test_split(X_fuga, y, test_size=0.2, random_state=42)
modelo = LinearRegression().fit(X_ent, y_ent)
mae_fuga = mean_absolute_error(y_prueba, modelo.predict(X_prueba))

# Version corregida: primero se divide, y el imputador y el escalador
# aprenden solo con entrenamiento dentro de un Pipeline.
X_ent, X_prueba, y_ent, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = Pipeline([
    ('imputar', SimpleImputer(strategy='median')),
    ('escalar', StandardScaler()),
    ('regresion', LinearRegression()),
])
modelo.fit(X_ent, y_ent)
mae_corregido = mean_absolute_error(y_prueba, modelo.predict(X_prueba))

print('MAE en prueba con fuga:     ', round(mae_fuga, 4))
print('MAE en prueba sin fuga:     ', round(mae_corregido, 4))
print('Mediana de distancia (todo):', X['distancia_km'].median())
print('Mediana de distancia (ent): ', X_ent['distancia_km'].median())

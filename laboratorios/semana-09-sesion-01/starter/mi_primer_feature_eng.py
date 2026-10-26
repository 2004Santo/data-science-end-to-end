import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

viajes = pd.read_csv('viajes_taxi.csv')

# Solo se quitan los errores confirmados en la Semana 8 (tarifa 999.99 y duracion negativa)
viajes_clean = viajes.query('tarifa < 999 and duracion_min >= 0').copy()

print(viajes_clean.head())
viajes_clean.info()

fecha_inicio = pd.to_datetime(viajes_clean['fecha_hora_inicio'])

viajes_clean['fecha_hora_inicio'] = fecha_inicio
viajes_clean['hora'] = fecha_inicio.dt.hour
viajes_clean['dia_semana'] = fecha_inicio.dt.dayofweek

# Sabado (5) y domingo (6)
viajes_clean['es_fin_de_semana'] = (viajes_clean['dia_semana'] >= 5).astype(int)

# Hora pico: lunes a viernes, de 7 a 9 y de 16 a 19
en_hora_pico = viajes_clean['hora'].between(7, 9) | viajes_clean['hora'].between(16, 19)
viajes_clean['es_hora_pico'] = (en_hora_pico & (viajes_clean['es_fin_de_semana'] == 0)).astype(int)

print(viajes_clean[['fecha_hora_inicio', 'hora', 'dia_semana', 'es_fin_de_semana', 'es_hora_pico']].head())

# La hora como ciclo: la 23 queda junto a la 0
viajes_clean['hora_sin'] = np.sin(2 * np.pi * viajes_clean['hora'] / 24)
viajes_clean['hora_cos'] = np.cos(2 * np.pi * viajes_clean['hora'] / 24)

print(viajes_clean[['fecha_hora_inicio', 'hora', 'hora_sin', 'hora_cos']])

# ¿La hora pico aporta algo a la tarifa? Se compara la tarifa por km,
# sin la tarifa fija de 70 ni los viajes con distancia 0
normales = viajes_clean.query('tarifa != 70 and distancia_km > 0').copy()
normales['tarifa_por_km'] = normales['tarifa'] / normales['distancia_km']
print('\nTarifa por km segun hora pico:')
print(normales.groupby('es_hora_pico')['tarifa_por_km'].mean().round(2))
print('\nDuracion por km segun hora pico:')
print((normales['duracion_min'] / normales['distancia_km']).groupby(normales['es_hora_pico']).mean().round(2))

viajes_codificado = pd.get_dummies(viajes_clean, columns=['zona_origen', 'zona_destino'], prefix=['origen', 'destino'])

print(viajes_codificado)

encoder = OrdinalEncoder()

viajes_codificado['metodo_pago_ordinal'] = encoder.fit_transform(viajes_codificado[['metodo_pago']]).ravel()

print(viajes_codificado.head())

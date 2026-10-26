"""Ejercicio 2: relaciones entre variables de viajes_taxi.csv.

Corre el script con:

    python3 ejercicio2_relaciones.py

Al final se imprime una comprobacion por cada TODO. No la modifiques:
cuando las cinco digan OK, pasa a los hallazgos del README.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("figuras", exist_ok=True)
viajes = pd.read_csv("viajes_taxi.csv")

# TODO 1: quita solo los errores que el Ejercicio 1 ya confirmo (tarifa
# 999.99 y duracion negativa). No quites los demas atipicos. Imprime
# cuantas filas quedan.
limpios = viajes.query("tarifa != 999.99 and duracion_min >= 0")
print("Filas despues de quitar errores:", len(limpios))

# TODO 2: grafico de dispersion de distancia_km (eje x) contra tarifa
# (eje y), guardado en figuras/distancia_vs_tarifa.png. Mira el grafico
# antes de seguir: busca puntos que no sigan la tendencia general y
# cuentalos con un filtro.
plt.figure()
plt.scatter(limpios["distancia_km"], limpios["tarifa"], s=5)
plt.title("Distancia vs tarifa")
plt.xlabel("distancia_km")
plt.ylabel("tarifa")
plt.savefig("figuras/distancia_vs_tarifa.png")
plt.close()

# Linea horizontal en 70 USD: tarifa fija del aeropuerto.
tarifa_fija = limpios[limpios["tarifa"] == 70]
print("Viajes con tarifa exacta de 70:", len(tarifa_fija))
print(tarifa_fija.groupby(["zona_origen", "zona_destino"]).size())

# Columna vertical en distancia 0: viajes que cobran sin registrar kilometros.
distancia_cero = limpios[limpios["distancia_km"] == 0]
print("Viajes con distancia 0:", len(distancia_cero))
print(distancia_cero[["duracion_min", "tarifa"]].describe().round(2))

# TODO 3: resumen_propina, con la propina promedio, la cantidad de viajes
# y la cantidad de viajes con propina 0, por metodo de pago.
resumen_propina = limpios.groupby("metodo_pago").agg(
    propina_promedio=("propina", "mean"),
    viajes=("propina", "size"),
    viajes_propina_0=("propina", lambda p: (p == 0).sum()),
)
print(resumen_propina.round(2))
print("Viajes sin metodo de pago:", limpios["metodo_pago"].isna().sum())

# TODO 4: correlaciones, la correlacion de distancia_km, duracion_min,
# pasajeros y propina con la tarifa.
correlaciones = limpios[["distancia_km", "duracion_min", "pasajeros", "propina", "tarifa"]].corr()["tarifa"]
print(correlaciones.drop("tarifa").round(2))

# TODO 5: cuantos viajes tienen pasajeros vacio y cuantos tienen 0.
pasajeros_vacios = limpios["pasajeros"].isna().sum()
pasajeros_cero = (limpios["pasajeros"] == 0).sum()
print("Pasajeros vacio:", pasajeros_vacios, "| Pasajeros en 0:", pasajeros_cero)


def comprobar(numero, condicion):
    if condicion:
        print(f"TODO {numero}: OK")
    else:
        print(f"TODO {numero}: revisa")


if isinstance(correlaciones, pd.DataFrame):
    correlaciones = correlaciones["tarifa"]

print()
print("Comprobacion")
comprobar(1, len(limpios) == 2975)
comprobar(2, os.path.exists("figuras/distancia_vs_tarifa.png"))
comprobar(3, resumen_propina is not None and len(resumen_propina) == 2)
comprobar(4, correlaciones is not None and round(float(correlaciones["distancia_km"]), 2) == 0.96)
comprobar(5, pasajeros_vacios == 119 and pasajeros_cero == 19)

# Semana 9, Sesión 1: Ingeniería de características: principios aplicados

> Objetivo de la sesión: explicar por qué una misma variable cruda puede necesitar codificaciones distintas según el modelo que la consuma, y diseñar al menos dos features derivadas para el dataset de tu proyecto.

**Lectura previa de esta sesión:** ["Feature Engineering that Makes Business Sense"](https://towardsdatascience.com/feature-engineering-that-makes-business-sense-419b9403236e/), Towards Data Science.

**Referencia de esta sesión:** *Designing Machine Learning Systems*, Chip Huyen (O'Reilly, 2022), Capítulo 5: Feature Engineering.

## Requisitos antes de esta sesión

pandas y matplotlib, de la sesión pasada. numpy se instala junto con pandas; verifica con:

```
python3 -c "import numpy; print(numpy.__version__)"
```

Ten a mano tus 3 hallazgos de la exploración de la Semana 8, Sesión 2: las features de hoy salen de ahí.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué diferencia a una feature que tiene sentido de negocio de una que solo mejora una métrica?**

_(tu respuesta)_

**Elige uno de los ejemplos del artículo: ¿qué conocimiento del negocio traduce a una columna, y cómo?**

_(tu respuesta)_

## Pregunta de apertura

La exploración encontró dos patrones que no existen como columnas: la tarifa fija entre JFK y Manhattan, y viajes que cuestan más por kilómetro a ciertas horas. El modelo solo ve columnas. ¿Cómo le das esa información?

Creándole columnas nuevas a partir de las que ya existen. Para la tarifa fija, una columna `es_tarifa_fija` que vale 1 cuando el viaje va entre JFK y una zona de Manhattan. Para la hora, sacar la hora de `fecha_hora_inicio` y marcar con `es_hora_pico` los viajes de lunes a viernes en horas de tráfico. Así el modelo ve como número lo que nosotros vimos en los gráficos.

## Ejercicio 1: features de fecha y hora

Archivo: [`starter/ejercicio1_features_tiempo.py`](./starter/ejercicio1_features_tiempo.py), sobre [`starter/viajes_taxi.csv`](./starter/viajes_taxi.csv), el mismo dataset de la sesión pasada. El script ya quita los errores confirmados, convierte `fecha_hora_inicio` y compara la tarifa por kilómetro según la hora pico; faltan 4 `TODO`: hora, día de la semana, fin de semana, hora pico y la hora como ciclo. Córrelo una vez antes de tocar nada:

```
cd laboratorios/semana-09-sesion-01/starter
python3 ejercicio1_features_tiempo.py
```

**Respuesta 1 (TODO 4), antes de ver la solución:** si dejas la hora como un número del 0 al 23, ¿qué tan lejos queda la hora 23 de la hora 0 para un modelo que mide distancias entre números? ¿Y en el reloj?

Como número, la 23 y la 0 están a 23 unidades, lo más lejos posible. En el reloj están a 1 hora. Por eso se convierte la hora en un ciclo con seno y coseno (`hora_sin`, `hora_cos`): con eso la 23 queda junto a la 0.

**Respuesta 2 (TODO 3):** sin el TODO 3, el Paso 4 muestra un solo grupo. Con la hora pico construida, ¿esperas que la tarifa por kilómetro sea más alta o más baja en hora pico? ¿Por qué, si la tarifa depende de la distancia y de la duración?

Más alta. La tarifa cobra por distancia y también por tiempo, y en hora pico hay más tráfico: cada kilómetro tarda más y por eso cuesta más. La salida lo confirma: la mediana sube de 3.22 a 3.52 USD por km.

**Respuesta 3:** la duración del viaje no existe al pedir el taxi, pero la hora sí. ¿Qué parte de lo que la duración le diría al modelo puede traer `es_hora_pico`?

El tráfico. La duración es alta cuando hay tráfico, y en hora pico hay más tráfico. En los datos, en hora pico el viaje tarda 4.12 min por km frente a 3.36 fuera de ella, así que `es_hora_pico` le da al modelo una parte de esa información sin usar algo que todavía no existe al pedir el taxi.

**Lo que confirmó la salida, TODO por TODO:**

- TODO 1 y 2: `hora` y `dia_semana` salen de `fecha_hora_inicio` (0 es lunes), y `es_fin_de_semana` vale 1 en sábado y domingo. Quedan 2975 viajes sin los errores confirmados.
- TODO 3: `es_hora_pico` vale 1 en 888 viajes (lunes a viernes, de 7 a 9 y de 16 a 19). En el Paso 4, sin tarifa fija ni distancia 0, la mediana de la tarifa por km es 3.22 USD fuera de hora pico y 3.52 en hora pico.
- TODO 4: con `hora_sin` y `hora_cos`, en el Paso 5 la 23 y la 0 quedan a 0.26, la misma distancia que la 11 y la 12. Como número, la primera pareja está a 23 y la segunda a 1.

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 2: zona, codificación y disponibilidad

Solo o en pareja. Archivo: [`starter/ejercicio2_features_zona.py`](./starter/ejercicio2_features_zona.py), sobre el mismo `viajes_taxi.csv`. Completa los 4 `TODO`. Al final, el script imprime una comprobación por TODO: complétalos hasta que todas digan `OK`.

```
python3 ejercicio2_features_zona.py
```

**Respuesta 1:** ¿cuántos viajes tienen `es_tarifa_fija` en 1, y qué tarifa mínima y máxima tienen? ¿Qué te dice eso sobre lo que un modelo lineal puede aprender con esta columna?

300 viajes, todos con tarifa mínima y máxima de 70 USD. La tarifa no depende de la distancia en esos viajes. Con esta columna un modelo lineal puede aprender un ajuste para ese grupo, aunque no la regla completa "si es tarifa fija, cobra 70 sin importar la distancia", porque la distancia sigue sumando. Un árbol de decisión sí podría separar ese grupo por completo.

**Respuesta 2:** ¿cuántas columnas crea one-hot para la zona de origen, y cuántas la codificación ordinal? Si el modelo es una regresión lineal, ¿cuál de las dos usarías, y por qué la otra le da información falsa?

One-hot crea 8 columnas, una por zona. La ordinal crea 1 sola columna con números del 0 al 7. Para una regresión lineal usaría one-hot. La ordinal le dice al modelo que las zonas tienen un orden y distancias entre sí (por ejemplo, que Upper West Side = 7 está más lejos de Brooklyn = 0 que Harlem = 1), y eso es falso: el orden solo sale del alfabeto.

**Respuesta 3:** ¿qué columnas del dataset no existen al pedir el taxi? ¿Qué pasaría con el modelo si las usaras para entrenar?

`duracion_min` y `propina` no existen al pedir el taxi, y `tarifa` es lo que se predice. Si se entrena con la duración o la propina, hay fuga de información: el modelo se ve excelente en la evaluación (la duración tiene correlación 0.96 con la tarifa), pero en producción esa columna no está y el modelo falla.

## Ejercicio 3: dos features para tu proyecto

Usa el mismo archivo de la exploración de la Semana 8 y la plantilla [`plantilla-features/features_proyecto.py`](./plantilla-features/features_proyecto.py).

### Paso 1: el momento de la predicción (5 minutos)

Escribe qué predice tu modelo y en qué momento: qué información existe en ese instante y cuál todavía no.

El modelo predice, al cerrar el día t, si un cantón va a tener alta demanda de emergencias del ECU 911 en el día t+3 (`y_3`, a partir de `obj_n_emergencias_t3`). En ese momento existen las emergencias de t y de los días anteriores (`n_emergencias`, `lag_1d`, `lag_7d`, `media_prev_7d`, `media_prev_28d`), el cantón y la provincia, y el calendario: qué día de la semana es t+3 y si es feriado (`es_feriado_t3`). Todavía no existen los conteos de t+1, t+2 ni t+3, ni `obj_n_emergencias_t7`.

### Paso 2: construye las 2 features (15 minutos)

Completa la plantilla con 2 columnas nuevas, derivadas de las existentes. Al menos una tiene que salir de uno de tus hallazgos de la exploración.

En [`plantilla-features/features_proyecto.py`](./plantilla-features/features_proyecto.py):

```python
datos = datos.sort_values(["cod_canton", "fecha"])
datos["lag_4d"] = datos.groupby("cod_canton")["n_emergencias"].shift(4)

datos["dia_semana_t3"] = (datos["dia_semana"] + 2) % 7 + 1
```

### Paso 3: justifica cada feature (5 minutos)

Para cada una: de qué hallazgo o conocimiento del dominio sale, qué evidencia muestra que aporta (una correlación, una diferencia de promedios), y por qué existe en el momento de predecir. Si alguna es categórica, di qué codificación usarías según el modelo que planeas entrenar.

**Feature 1:**

`lag_4d`, las emergencias del mismo cantón 4 días antes. Sale del Hallazgo 2 de la Semana 8: hay un ciclo semanal fuerte, y t−4 cae el mismo día de la semana que t+3. Evidencia: su correlación con `obj_n_emergencias_t3` es 0.73 en Quito, 0.85 en Guayaquil y 0.66 en Cuenca, mientras que `n_emergencias` de t tiene −0.33 en Quito. Existe al predecir porque es un dato del pasado. Es numérica: se imputa (los primeros 4 días de cada cantón quedan vacíos) y se escala.

**Feature 2:**

`dia_semana_t3`, el día de la semana del día que se predice (1 = lunes, 7 = domingo). Sale del mismo ciclo semanal. El script imprime el objetivo promedio por `dia_semana_t3`: en los 10 cantones de la muestra es 555,8 cuando t+3 es domingo y 391,5 cuando es martes, y sube de forma continua del martes al domingo. Existe al predecir porque la fecha de t+3 se conoce desde t. Es categórica: para una regresión logística usaría one-hot (7 columnas), porque con números del 1 al 7 el modelo creería que el domingo está "lejos" del lunes y que la demanda sube en línea recta durante la semana; para un modelo de árboles también serviría la codificación ordinal.

## Antes de la próxima sesión

**Lectura:** ["The Dreaded Antagonist: Data Leakage in Machine Learning"](https://towardsdatascience.com/the-dreaded-antagonist-data-leakage-in-machine-learning-5f08679852cc/), Towards Data Science.

Para escalar la distancia antes de entrenar, le restas la media y la divides por la desviación estándar. ¿Con qué viajes calculas esa media: con todos, o solo con los de entrenamiento? ¿Cambia algo?

Solo con los de entrenamiento. Si se usa la media de todos los viajes, el conjunto de prueba ya influyó en cómo se preparan los datos de entrenamiento: es una fuga de información, aunque sea pequeña. En la práctica el número casi no cambia con 3000 viajes, pero la evaluación deja de ser honesta, porque en producción los viajes nuevos no estarán en esa media.

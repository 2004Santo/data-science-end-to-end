# Semana 9, Sesión 2: Pipeline reproducible de features

> Objetivo de la sesión: construir un pipeline de transformación reproducible con scikit-learn (imputación, codificación, escalado) para el dataset de tu proyecto, que evite la fuga de información entre entrenamiento y validación.

**Lectura previa de esta sesión:** ["The Dreaded Antagonist: Data Leakage in Machine Learning"](https://towardsdatascience.com/the-dreaded-antagonist-data-leakage-in-machine-learning-5f08679852cc/), Towards Data Science.

**Referencia de esta sesión:** [Pipelines and composite estimators (documentación oficial de scikit-learn)](https://scikit-learn.org/stable/modules/compose.html).

## Requisitos antes de esta sesión

scikit-learn ya viene en el Codespace. En tu laptop, instálalo con `pip install -r requirements.txt` desde la raíz del repositorio. Verifica con:

```
python3 -c "import sklearn; print(sklearn.__version__)"
```

Este laboratorio usa `sparse_output=False` en `OneHotEncoder`, disponible desde scikit-learn 1.2. El `requirements.txt` del repositorio ya fija una versión posterior.

Ten a mano el script de features de tu proyecto de la sesión pasada.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué es la fuga de información, y por qué un modelo con fuga puede verse excelente en la evaluación y fallar en producción?**

_(tu respuesta)_

**El artículo describe varias formas en que se produce una fuga. ¿Cuál de ellas viste la sesión pasada con la duración del viaje?**

_(tu respuesta)_

## Pregunta de apertura

Para escalar la distancia, le restas la media y la divides por la desviación estándar. ¿Con qué viajes calculas esa media: con todos, o solo con los de entrenamiento? ¿Cambia algo?

Solo con los de entrenamiento. Si la media sale de todos los viajes, los de prueba ya influyeron en la preparación y la evaluación deja de simular lo que pasa en producción. Con 2975 viajes el número casi no cambia (la mediana de la distancia es 6.93 con todos y 6.94 solo con entrenamiento), pero el procedimiento sigue teniendo fuga.

## Ejercicio 1: encontrar y corregir la fuga

Archivo: [`starter/ejercicio1_fuga.py`](./starter/ejercicio1_fuga.py), sobre [`starter/viajes_features.csv`](./starter/viajes_features.csv): los viajes de taxi con las features de la sesión pasada, sin los errores confirmados, y con la distancia 0 y los 0 pasajeros marcados como faltantes. La primera parte del script es el código de un compañero: imputa y escala la distancia y los pasajeros con todo el dataset, después divide en entrenamiento y prueba, y entrena una regresión lineal. La segunda parte es la versión correcta, con 3 `TODO`. Córrelo una vez antes de tocar nada:

```
cd laboratorios/semana-09-sesion-02/starter
python3 ejercicio1_fuga.py
```

**Respuesta 1, antes de ver la solución:** en la versión del compañero, ¿en qué línea entra el conjunto de prueba al entrenamiento? ¿Qué número de la salida lo delata?

En el `fit_transform` del imputador y del escalador sobre todo el dataset, antes de `train_test_split`. Ahí la mediana, la media y la desviación estándar se calculan también con los viajes de prueba.

**Respuesta 2 (TODO 1 y 3):** sin resolver, la versión correcta dice que tiene 2975 filas de prueba. ¿Qué está midiendo ese error, si prueba y entrenamiento son las mismas filas?

Espero que cambie muy poco, porque con miles de viajes la mediana y la media casi no se mueven. Y así pasó: 2.5276 con fuga y 2.5274 sin fuga. Que casi no cambie no significa que no había fuga: la fuga está en el procedimiento. Con pocos datos, con una columna que cambia en el tiempo o con una fuga más grave (como la duración), la diferencia sí sería grande.

**Respuesta 3:** ¿cuánto esperas que cambie el error absoluto medio en prueba al corregir la fuga? Si casi no cambia, ¿significa que no había fuga?

[`starter/corregir_fuga.py`](./starter/corregir_fuga.py) corre las dos versiones con las mismas columnas (`distancia_km`, `pasajeros` y las features de la sesión pasada). La versión con fuga imputa y escala con todo el dataset y después divide. La corregida divide primero y mete el imputador, el escalador y la regresión lineal en un `Pipeline`, que aprende solo con entrenamiento. MAE en prueba: 2.5276 con fuga y 2.5274 corregida. La mediana de la distancia es 6.93 con todo el dataset y 6.94 solo con entrenamiento. Se corre con `python3 corregir_fuga.py` desde `starter/`, o con Docker (`docker build -t semana09s2 .` y `docker run --rm semana09s2`).

**Lo que confirmó la salida, TODO por TODO:**

_(anota las filas que vio cada escalador y los dos errores)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 2: el pipeline completo

Solo o en pareja. Archivo: [`starter/ejercicio2_pipeline.py`](./starter/ejercicio2_pipeline.py), sobre el mismo `viajes_features.csv`. Completa los 5 `TODO`: división, `ColumnTransformer` con tres grupos de columnas, `fit` solo con entrenamiento, verificación de las medianas, y un viaje desde una zona que el entrenamiento nunca vio. Al final, el script imprime una comprobación por TODO: complétalos hasta que todas digan `OK`.

```
python3 ejercicio2_pipeline.py
```

**Respuesta 1:** ¿cuántas columnas quedan después de preparar los datos? Explica de dónde sale ese número a partir de los tres grupos de columnas.

25 columnas: 2 numéricas (`distancia_km`, `pasajeros`), 18 de one-hot (8 zonas de origen + 8 zonas de destino + 2 métodos de pago) y 5 que pasan sin cambios (`hora_sin`, `hora_cos`, `es_fin_de_semana`, `es_hora_pico`, `es_tarifa_fija`). 2 + 18 + 5 = 25. Entrenamiento queda con (2380, 25) y prueba con (595, 25).

**Respuesta 2:** ¿las medianas que aprendió el imputador coinciden con las de entrenamiento o con las de todo el dataset? ¿Qué demuestra eso?

Con las de entrenamiento: el imputador aprendió 6.94 km y 1 pasajero, igual que las medianas de entrenamiento, mientras que con todo el dataset la distancia da 6.93. Demuestra que `fit` solo vio entrenamiento y que el conjunto de prueba no se filtró en la preparación.

**Respuesta 3:** ¿qué le pasa al viaje desde el Bronx? ¿Qué habría pasado con `pd.get_dummies` aplicado por separado a ese viaje?

Como el Bronx no estaba en entrenamiento, `handle_unknown="ignore"` deja las 8 columnas de `zona_origen` en 0 (0 columnas en 1) y el viaje sigue teniendo las mismas 25 columnas. Con `pd.get_dummies` aplicado solo a ese viaje saldría una columna `zona_origen_Bronx` que el modelo no conoce y faltarían las otras: las columnas no coincidirían con las de entrenamiento y el modelo daría error o leería mal los datos.

## Ejercicio 3: el pipeline de tu proyecto

Usa tu archivo con las 2 features de la sesión pasada y la plantilla [`plantilla-pipeline/pipeline_proyecto.py`](./plantilla-pipeline/pipeline_proyecto.py).

### Paso 1: clasifica tus columnas (5 minutos)

Escribe qué columnas son numéricas, cuáles categóricas y cuáles ya están listas, y cuál es el objetivo. Deja fuera toda columna que no exista al momento de predecir.

- **Objetivo:** `obj_n_emergencias_t3` (de ahí sale la etiqueta `y_3` de alta demanda). Se quitan las filas sin objetivo (los últimos 3 días de cada cantón).
- **Numéricas:** `n_emergencias`, `lag_1d`, `lag_4d`, `lag_7d`, `media_prev_7d`, `media_prev_28d`. Se imputan con la mediana (los rezagos están vacíos al inicio de cada serie) y se escalan.
- **Categóricas:** `dia_semana_t3` y `cod_provincia`, con one-hot.
- **Ya listas:** `es_feriado_t3` (ya es 0 o 1).
- **Fuera:** `obj_n_emergencias_t7` (es un dato del futuro), `fecha` y `anio` (solo sirven para dividir), y `canton`, `nombre_dia` y `nombre_feriado` porque repiten información que ya está en otras columnas.

### Paso 2: decide cómo dividir (5 minutos)

¿Tu modelo predice el futuro a partir de filas con fecha? Si sí, divide por fecha; si no, al azar. Justifica.

Sí: predice t+3 a partir de lo que pasó hasta t. Divido por fecha con el mismo corte de la Semana 8: entrenamiento antes del 1 de julio de 2025 y prueba desde esa fecha. Si se divide al azar, el modelo entrena con días posteriores a los de prueba y con días vecinos casi iguales, y eso es fuga. Además el volumen baja con los años (Hallazgo 3), así que la prueba tiene que estar en el periodo más reciente, como en producción.

### Paso 3: construye y corre el pipeline (15 minutos)

Completa la plantilla y córrela. Anota la forma de los conjuntos de entrenamiento y prueba ya preparados, y la lista de columnas que produce.

[`plantilla-pipeline/pipeline_proyecto.py`](./plantilla-pipeline/pipeline_proyecto.py). Con la OBT de 224 cantones del 1 de julio de 2021 al 31 de agosto de 2026, el entrenamiento tiene 327.264 filas (224 × 1.461 días) y la prueba 94.976 (224 × 424 días). Las columnas son 6 numéricas + 7 de `dia_semana_t3` + una por provincia + `es_feriado_t3`:

```
['numericas__n_emergencias', 'numericas__lag_1d', 'numericas__lag_4d', 'numericas__lag_7d',
 'numericas__media_prev_7d', 'numericas__media_prev_28d',
 'categoricas__dia_semana_t3_1', ..., 'categoricas__dia_semana_t3_7',
 'categoricas__cod_provincia_01', ..., 'ya_listas__es_feriado_t3']
```

## Antes de la próxima sesión

**Lectura:** ["Ensembles in Machine Learning"](https://towardsdatascience.com/ensembles-in-machine-learning-9128215629d1/), Towards Data Science.

Ya tienes los datos listos para entrenar. Si entrenas dos modelos sobre el mismo conjunto y uno da un error mucho menor en entrenamiento que en prueba, ¿qué le está pasando?

Está sobreajustando (overfitting): memorizó los datos de entrenamiento, incluido el ruido, en lugar de aprender el patrón general, y por eso falla con datos que no vio.

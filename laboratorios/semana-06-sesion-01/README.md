# Semana 6, Sesión 1: Procesamiento por lotes de datos históricos

> Objetivo de la sesión: procesar los datos históricos de tu proyecto, que no caben en memoria, mediante un job de procesamiento distribuido por lotes.

**Lectura previa de esta sesión:** ["Batch and Streaming in the World of Data Science and Data Engineering"](https://medium.com/capital-one-tech/batch-and-streaming-in-the-world-of-data-science-and-data-engineering-2cc029cdf554), Capital One Tech.

**Referencia de esta sesión:** [Data Engineering Zoomcamp, módulo de batch processing (DataTalksClub)](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/06-batch). Este laboratorio usa Spark en modo local (`local[*]`), sobre los núcleos de tu propia máquina (tu Codespace o tu laptop), sin ningún clúster real: el mismo criterio que ya usó este curso con Docker/Terraform locales (Semana 3), Kestra local (Semana 4) y DuckDB local (Semana 5).

## Requisitos antes de esta sesión

1. **Java 17 y PySpark 3.5.3.** En el Codespace ya vienen instalados. En tu laptop, instala OpenJDK 17 (en Mac, con Homebrew: `brew install openjdk@17`) y después corre `pip install -r requirements.txt` desde la raíz del repositorio, que fija PySpark en la versión 3.5.3 (compatible con Java 8/11/17; la rama 4.x de PySpark exige Java 17 o superior). Verifica con:
   ```
   java -version
   python3 -c "import pyspark; print(pyspark.__version__)"
   ```
2. Ten a mano el archivo histórico real que tu pipeline orquestado de la Semana 4 genera para tu proyecto, y al menos una transformación de pandas que ya escribiste sobre ese archivo en una sesión anterior (Semana 4, Sesión 2, o Semana 5).

**Si ves un error de red al arrancar Spark (`UnknownHostException`) que no te deja ver la salida del programa:** corre el script con la variable de ambiente `SPARK_LOCAL_IP=127.0.0.1` antes del comando, por ejemplo `SPARK_LOCAL_IP=127.0.0.1 python3 mi_job.py`. No es un error de tu código. En el Codespace esta variable ya viene configurada, así que ahí no deberías verlo.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué distingue a un job de procesamiento por lotes (batch) de un job de procesamiento en tiempo real (streaming)?**

_(tu respuesta)_

**El artículo describe el procesamiento distribuido como una forma de repartir el trabajo entre varias máquinas o núcleos. ¿Qué problema resuelve repartir el trabajo, que un solo proceso de pandas no resuelve?**

_(tu respuesta)_

## Pregunta de apertura

Tu pipeline de la Semana 4 lleva semanas acumulando el histórico de tu proyecto. Un día ese archivo pesa más que la memoria RAM de tu laptop. ¿Qué le pasa exactamente a un script de pandas que intenta leerlo con `pd.read_csv()`, y por qué?

_(tu respuesta)_

## Ejercicio 1: leer y filtrar un CSV con Spark

Enunciado: [`starter/ventas.csv`](./starter/ventas.csv) tiene ventas de una tienda (categoría, cantidad, precio unitario), la misma tarea de siempre, ahora con Spark en vez de pandas.

**Respuesta 1, antes de ver la solución:** si `spark.read.csv(...)` no ejecuta nada todavía porque es parte de un plan perezoso, ¿qué instrucción de las que ya conoces de pandas tendría que cambiar de comportamiento aquí?

_(tu respuesta)_

**Respuesta 2:** si agregaras un `.filter()` más entre `spark.read.csv(...)` y `.show()`, sin llamar a ninguna acción entre medio, ¿cuántas veces se ejecuta realmente el archivo completo?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el script completo, mientras se revisa en clase)_

## Ejercicio 2: agregación con Spark

Enunciado: la misma pregunta de negocio de la Semana 5 (monto total por categoría), esta vez con la API de DataFrames de Spark en vez de SQL sobre DuckDB.

**Respuesta 1, antes de ver la solución:** ¿qué método de la API de DataFrames de Spark esperas que sea el equivalente directo del `GROUP BY` de SQL que ya usaste con DuckDB?

_(tu respuesta)_

**Respuesta 2:** cuando `resumen.write.csv(...)` corre, ¿esperas que el resultado quede en un solo archivo `.csv`, como haría `df.to_csv()` de pandas, o en algo distinto?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el script completo, mientras se revisa en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: reescribe una transformación de tu proyecto como job de Spark

Elige una transformación de pandas que ya escribiste sobre el archivo histórico de tu propio proyecto (una columna calculada, una agregación por categoría), y reescríbela con la API de DataFrames de Spark. Parte de la plantilla [`plantilla-spark/construir_job_spark.py`](./plantilla-spark/construir_job_spark.py), que trae los `TODO` marcados en vez del script en blanco.

### Paso 1: lee tu archivo con Spark (5 minutos)

Reemplaza la ruta del archivo histórico real de tu proyecto.

_(tu ruta de archivo, y cuántas filas leyó Spark)_

### Paso 2: reescribe tu transformación (10 minutos)

Con `withColumn()` para la columna calculada y `groupBy().agg()` para la agregación, reproduce exactamente el mismo cálculo que ya hacías con pandas.

_(tu transformación, y qué pregunta de tu proyecto responde)_

### Paso 3: corre el job y compara contra pandas (5 minutos)

Confirma que el resultado de Spark coincide con el resultado que ya conocías de pandas.

_(qué mostró tu job, y si coincidió con lo que esperabas)_

## Antes de la próxima sesión

Ya reescribiste una transformación de tu proyecto para que corra en particiones, sobre un histórico ya acumulado.

Pregunta: hoy procesaste un histórico ya acumulado, de una sola vez. ¿Qué pasa si tu proyecto necesita reaccionar a cada dato nuevo apenas llega, sin esperar a que se acumule un lote?

_(tu respuesta)_

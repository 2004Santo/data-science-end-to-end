# Semana 5, Sesión 1: Data warehouse y data lake

> Objetivo de la sesión: elegir entre un data warehouse y un data lake para los datos de tu proyecto, justificando la decisión según el tipo de dato y el patrón de consulta.

**Lectura previa de esta sesión:** ["Data Lakes vs Data Warehouses Explained"](https://www.databricks.com/blog/data-lakes-vs-data-warehouses-what-your-organization-needs-know), Databricks.

**Referencia de esta sesión:** [BigQuery, documentación oficial](https://cloud.google.com/bigquery/docs/introduction). Este laboratorio usa DuckDB como warehouse local: cumple el mismo rol conceptual que BigQuery (base de datos analítica que recibe datos estructurados y sirve consultas SQL agregadas) sin necesitar ninguna cuenta de nube ni facturación, el mismo criterio que ya usó este curso con Docker/Terraform locales (Semana 3) y con Kestra local (Semana 4).

## Requisitos antes de esta sesión

1. **Python con `pandas` ya instalado**, el mismo de sesiones pasadas.
2. Instala DuckDB:
   ```
   pip install duckdb
   ```
   Verifica con:
   ```
   python -c "import duckdb; print(duckdb.__version__)"
   ```
3. Ten a mano el archivo (o los archivos) que tu pipeline orquestado de la Semana 4, Sesión 1 genera para tu proyecto. Si todavía no lo has corrido desde entonces, corre tu flow de Kestra al menos una vez antes de esta sesión.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué tipo de dato y qué patrón de consulta hacen que un equipo prefiera un data warehouse en vez de un data lake?**

_(tu respuesta)_

**¿Y qué tipo de dato y qué patrón de consulta hacen que un equipo prefiera un data lake?**

_(tu respuesta)_

## Pregunta de apertura

Un equipo de finanzas necesita generar el mismo reporte de ventas todos los lunes, con columnas fijas (fecha, producto, monto), para cargarlo directo a un dashboard. Un equipo de machine learning recolecta clics, logs de la aplicación e imágenes de producto, en formatos distintos, sin saber todavía qué de todo eso va a usar en un modelo futuro. ¿Cuál de los dos necesita un data warehouse, y cuál un data lake?

_(tu respuesta)_

## Ejercicio 1: cargar un CSV a un warehouse local y correr la primera consulta

Enunciado: [`starter/pedidos.csv`](./starter/pedidos.csv) tiene pedidos de una tienda (categoría, cantidad, precio unitario). Hasta ahora es un archivo plano, sin ninguna estructura de consulta.

**Respuesta 1, antes de ver la solución:** ¿qué necesitas para poder correr una consulta SQL de agregación (por ejemplo, monto total por categoría) sobre este archivo, sin escribir tú mismo el código que suma cada fila?

_(tu respuesta)_

**Respuesta 2:** si cargas `pedidos.csv` a una tabla de un warehouse y el archivo original cambia después, ¿la tabla se actualiza sola, o hay que volver a cargarla?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el script completo, mientras se revisa en clase)_

## Ejercicio 2: unir dos tablas del warehouse

Enunciado: [`starter/clientes.csv`](./starter/clientes.csv) tiene la ciudad y el segmento de cada cliente que aparece en `pedidos.csv`. Por separado, ninguno de los dos archivos responde "¿cuánto se vendió por ciudad?".

**Respuesta 1, antes de ver la solución:** con las dos tablas ya cargadas en el mismo warehouse, ¿qué instrucción de SQL las combina en una sola consulta?

_(tu respuesta)_

**Respuesta 2:** si en vez de un warehouse tuvieras los dos archivos crudos sueltos en un data lake, sin cargarlos a ninguna tabla, ¿qué tendrías que hacer distinto para responder la misma pregunta?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el script completo, con el JOIN y las dos agregaciones, mientras se revisa en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: el warehouse de tu propio proyecto

Carga el archivo real que tu pipeline orquestado (Semana 4, Sesión 1) genera para tu proyecto a un warehouse de DuckDB propio, y escribe tus primeras consultas. Parte de la plantilla [`plantilla-warehouse/construir_warehouse.py`](./plantilla-warehouse/construir_warehouse.py), que trae los `TODO` marcados en vez del script en blanco.

### Paso 1: conecta y carga tu archivo (5 minutos)

Reemplaza el nombre del archivo `.duckdb`, la ruta de tu CSV (o el formato que tu proyecto genere) y el nombre de la tabla.

_(tu nombre de archivo `.duckdb` y de tabla elegidos)_

### Paso 2: primera consulta, cuántas filas cargaste (5 minutos)

Confirma que el número de filas coincide con lo que esperabas de tu archivo de origen.

_(cuántas filas cargaste, y si coincide con lo esperado)_

### Paso 3: una agregación que responda una pregunta real de tu proyecto (10 minutos)

Elige una columna categórica de tu dataset y agrégala con `GROUP BY`, pensando en una pregunta que de verdad te interese para tu proyecto, no una agregación arbitraria.

_(tu consulta, qué pregunta responde, y qué encontraste)_

## Antes de la próxima sesión

Ya tienes tus datos en un warehouse y corriste tus primeras consultas.

Pregunta: si mañana necesitas ese mismo tipo de consulta pero con una columna calculada nueva, y la próxima semana alguien más del equipo necesita otra variación de la misma lógica, ¿qué pasa si cada quien la escribe como un SQL nuevo desde cero?

_(tu respuesta)_

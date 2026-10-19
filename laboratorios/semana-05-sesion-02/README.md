# Semana 5, Sesión 2: Modelado analítico (analytics engineering)

> Objetivo de la sesión: construir un modelo de datos en capas (staging, intermedia, marts) con pruebas y documentación para los datos de tu proyecto.

**Lectura previa de esta sesión:** ["What is analytics engineering?"](https://www.getdbt.com/blog/what-is-analytics-engineering), dbt Labs.

**Referencia de esta sesión:** [dbt, documentación oficial](https://docs.getdbt.com/docs/introduction). Este laboratorio usa `dbt-duckdb`, el adaptador que conecta dbt al mismo warehouse de DuckDB que construiste la sesión pasada: dbt corre igual de local que DuckDB, sin ningún servicio ni cuenta adicional.

## Requisitos antes de esta sesión

1. **El warehouse de DuckDB de la Sesión 1**, con los datos de tu proyecto ya cargados (el archivo `.duckdb` del Ejercicio 3 de la sesión pasada).
2. Instala dbt con el adaptador de DuckDB:
   ```
   pip install dbt-core dbt-duckdb
   ```
   Verifica con:
   ```
   dbt --version
   ```
   Deberías ver `duckdb` listado en la sección de plugins.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué hace un analytics engineer que no hace ni un ingeniero de datos puro ni un analista puro?**

_(tu respuesta)_

**El artículo describe el flujo de trabajo de dbt (escribir SQL, dbt lo convierte en tablas o vistas). ¿Qué gana ese SQL por vivir dentro de un proyecto de dbt en vez de pegarse directo en una consola de SQL?**

_(tu respuesta)_

## Pregunta de apertura

Imagina un solo archivo SQL de 200 líneas: limpia los datos crudos, calcula columnas de negocio, une varias tablas y agrega el resultado final, todo en una sola consulta con subconsultas anidadas. Funciona. ¿Por qué no dejarlo así?

_(tu respuesta)_

## Ejercicio 1: la capa de staging

Enunciado: ya tienes `raw_pedidos` y `raw_clientes` en tu warehouse (recreadas hoy con [`starter/cargar_raw.py`](./starter/cargar_raw.py) a partir de [`starter/pedidos.csv`](./starter/pedidos.csv) y [`starter/clientes.csv`](./starter/clientes.csv), el mismo par de tablas de la sesión pasada). Un modelo de dbt es un archivo `.sql` con un `SELECT`: dbt lo convierte en una vista o una tabla según la configuración del proyecto.

**Respuesta 1, antes de ver la solución:** si el modelo de staging solo selecciona columnas de la tabla cruda, sin ningún cálculo, ¿qué sentido tiene crear un modelo aparte en vez de consultar `raw_pedidos` directamente cada vez?

_(tu respuesta)_

**Respuesta 2:** dbt permite declarar pruebas (`tests`) sobre una columna de un modelo, como `unique` o `not_null`, en un archivo `schema.yml`. ¿Sobre qué columna de `stg_pedidos` tendría sentido poner una prueba `unique`?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí los modelos `stg_pedidos.sql`, `stg_clientes.sql` y su `schema.yml` con las pruebas, mientras se revisan en clase)_

## Ejercicio 2: la capa intermedia y la capa de marts

Enunciado: con `stg_pedidos` y `stg_clientes` ya construidos, falta responder la pregunta de negocio real: cuánto se vendió por ciudad.

**Respuesta 1, antes de ver la solución:** un modelo intermedio referencia a otro modelo de dbt con `{{ ref('nombre_del_modelo') }}` en vez de escribir el nombre de la tabla directamente. ¿Qué usarías, `{{ ref('stg_pedidos') }}` o el nombre de la tabla cruda `raw_pedidos`, para construir el modelo intermedio que une pedidos con clientes?

_(tu respuesta)_

**Respuesta 2:** si mañana cambias cómo se calcula `monto_total` en el modelo intermedio, ¿tienes que tocar también el modelo de marts que lo consume?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí `int_pedidos_con_cliente.sql`, `marts_ventas_por_ciudad.sql` y el comando para correrlos, mientras se revisan en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: modela en capas los datos de tu propio proyecto

Usa exactamente el mismo patrón de los Ejercicios 1 y 2 (staging, intermedia, marts), aplicado a la tabla que cargaste a tu warehouse en la Sesión 1. Parte de la plantilla [`plantilla-dbt/`](./plantilla-dbt/), que trae los `TODO` marcados en cada archivo en vez del proyecto en blanco.

### Paso 1: staging (7 minutos)

Renombra `models/staging/stg_TODO.sql` a `stg_<tu_tabla>.sql`, selecciona las columnas de tu tabla cruda, y agrega al menos una prueba (`unique` o `not_null`) en `schema.yml` sobre la columna que identifica cada fila.

_(tu modelo de staging y la prueba que elegiste)_

### Paso 2: intermedia y marts (13 minutos)

Renombra y completa `models/intermedia/int_TODO.sql` con una transformación o combinación de tablas de staging (usando `{{ ref(...) }}`), y `models/marts/marts_TODO.sql` con la agregación final que responda una pregunta real de tu proyecto.

_(tus modelos y qué pregunta responde tu marts)_

Corre y prueba tu proyecto:

```
dbt run --profiles-dir .
dbt test --profiles-dir .
```

_(qué mostró `dbt run`, y si alguna prueba falló)_

## Antes de la próxima sesión

Ya tienes tus datos organizados en capas, con pruebas que fallan si algo se rompe.

Pregunta: todo lo que hiciste hasta ahora (warehouse, capas, pruebas) asume que tus datos caben enteros en la memoria de tu computadora. ¿Qué pasa el día en que el historial completo de tu proyecto ya no cabe?

_(tu respuesta)_

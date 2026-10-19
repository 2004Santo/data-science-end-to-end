# Semana 4, Sesión 2: Calidad de datos, diagnóstico y limpieza de los datos

> Objetivo de la sesión: diagnosticar problemas de calidad en el dataset de tu proyecto (duplicados, valores faltantes, inconsistencias de esquema) y justificar qué estrategia de limpieza aplica a cada uno.

**Lectura previa de esta sesión:** ["An Introduction to Data Quality"](https://medium.com/towards-data-science/an-introduction-to-data-quality-951cc6fe0274), Towards Data Science / Medium.

**Referencia de esta sesión:** *Designing Machine Learning Systems*, Cap. 3, Data Engineering Fundamentals (Chip Huyen).

## Requisitos antes de esta sesión

Confirma que tienes pandas instalado (`pip install pandas` si hace falta) y acceso al dataset real de tu proyecto, aunque sea en una versión parcial o de muestra.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿por qué un modelo puede entrenar sin ningún error y producir métricas razonables, aunque los datos de entrada tengan problemas serios de calidad?**

_(tu respuesta)_

**El artículo distingue varias dimensiones de calidad de datos. ¿Cuál te parece más difícil de detectar solo con un vistazo rápido al dataset, sin código?**

_(tu respuesta)_

## Pregunta de apertura

Tu modelo entrena sin ningún error, y las métricas se ven razonables. ¿Eso significa que los datos de entrada estaban bien?

_(tu respuesta)_

## Ejercicio 1: duplicados

Enunciado: el archivo [`starter/inscripciones.csv`](./starter/inscripciones.csv) tiene algunas filas que aparecen más de una vez, exactamente iguales en todas sus columnas.

**Respuesta 1, antes de ver la solución:** ¿qué método de pandas usarías para saber cuántas filas están exactamente repetidas, antes de eliminar ninguna?

_(tu respuesta)_

**Respuesta 2:** ¿por qué crees que existen esas filas duplicadas en este dataset: son eventos reales que coinciden, o algo salió mal en el proceso que las generó?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el código y la salida, mientras se revisan en clase)_

## Ejercicio 2: valores faltantes, tipos y fechas mezcladas

Enunciado: el archivo [`starter/sensores.csv`](./starter/sensores.csv) tiene celdas vacías, un valor `N/D` en la columna que debería ser numérica, y fechas escritas en dos formatos distintos mezclados en la misma columna.

**Respuesta 1, antes de ver la solución:** si una columna que debería ser numérica aparece como texto en `dtypes`, ¿qué esperarías encontrar dentro de esa columna?

_(tu respuesta)_

**Respuesta 2:** si en vez de detectar el formato de fecha explícitamente usaras una conversión automática de formato mixto, ¿qué podría pasar con una fecha ambigua como `01/02/2026`?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el código y la salida, mientras se revisan en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: diagnóstico del dataset de tu proyecto

Corre sobre tu propio dataset las mismas verificaciones de los Ejercicios 1 y 2 (`duplicated()`, `isna()`, `dtypes`, conversión con `errors="coerce"`, revisión manual de formatos mezclados), y documenta lo que encuentres en la plantilla [`plantilla-diagnostico/diagnostico.md`](./plantilla-diagnostico/diagnostico.md).

El resultado de hoy es el diagnóstico documentado y justificado, no todavía la limpieza completa implementada: antes de corregir hay que entender qué se está corrigiendo y por qué, como muestra el ConcepTest de esta sesión.

### Paso 1: corre las verificaciones (10 minutos)

Adapta el código de los Ejercicios 1 y 2 a las columnas reales de tu dataset.

_(qué verificaciones corriste)_

### Paso 2: revisa manualmente lo que el código no captura solo (5 minutos)

Duplicados, faltantes y tipos se detectan con código; los formatos mezclados (fechas, categorías escritas de más de una forma, unidades distintas) muchas veces requieren mirar valores únicos de una columna (`datos["columna"].unique()`) para notarlos.

_(qué encontraste al revisar manualmente)_

### Paso 3: completa la plantilla de diagnóstico (5 minutos)

Para cada problema encontrado, documenta la estrategia que aplicarías y por qué, no solo que el problema existe.

_(tu plantilla completa, o un resumen si la completaste aparte)_

## Antes de la próxima sesión

Ya diagnosticaste los problemas de calidad de tu dataset.

Pregunta: ¿cómo decides, con evidencia y no solo con intuición, qué variables de ese dataset ayudan a predecir lo que tu proyecto necesita predecir, y cuáles solo parecen ayudar?

_(tu respuesta)_

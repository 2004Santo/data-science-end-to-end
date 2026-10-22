# Semana 4, Sesión 1: Orquestación del pipeline de ingesta

> Objetivo de la sesión: convertir el script de ingesta de tu proyecto, que hasta ahora ejecutas a mano, en un pipeline programado con reintentos y backfill.

**Lectura previa de esta sesión:** ["Data Pipeline Orchestration"](https://towardsdatascience.com/data-pipeline-orchestration-9887e1b5eb7a/), Towards Data Science.

**Referencia de esta sesión:** [Data Engineering Zoomcamp, Módulo 2 (DataTalksClub)](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/README.md). Este curso usa Kestra, el mismo orquestador que enseña la edición vigente de ese módulo.

## Requisitos antes de esta sesión

1. **Docker**, el mismo de las sesiones pasadas. Si trabajas en el Codespace, ábrelo para esta sesión con una máquina de 4 núcleos ("Change machine type"): Kestra y su Postgres necesitan más memoria que los laboratorios anteriores.
2. Levanta Kestra localmente antes de la sesión, con el `docker-compose.yml` de [`starter/docker-compose.yml`](./starter/docker-compose.yml):
   ```
   docker compose up -d
   ```
   Abre `localhost:8080` en el navegador (en el Codespace, desde la pestaña **Ports** de VS Code, puerto 8080): deberías ver la pantalla de inicio de sesión de Kestra. Entra con el usuario `admin@kestra.io` y la contraseña `Admin1234`, definidos en el mismo `docker-compose.yml`. Si es la primera vez que arranca, puede tardar 20-30 segundos en quedar lista.

Este `docker-compose.yml` es una versión simplificada del oficial de Kestra: quita el `healthcheck` de Postgres (fuera del vocabulario de Docker Compose de este curso) porque el reintento de conexión, igual que en la Sesión 2 de la semana pasada, se resuelve del lado de cada flow, no de Docker.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué diferencia hay entre encadenar scripts con un cron job y usar una herramienta de orquestación?**

_(tu respuesta)_

**¿Por qué un cron job, que solo dispara un comando a una hora fija, no resuelve por sí solo el problema de un pipeline que falla a mitad de camino?**

_(tu respuesta)_

## Pregunta de apertura

Tu script de ingesta corre perfecto cuando tú lo ejecutas a las 10 de la mañana, mirando la pantalla. Si tiene que correr todos los días a las 3 de la madrugada, sin que nadie esté despierto para revisarlo, ¿qué cosas pueden salir mal que hoy nunca has visto fallar?

_(tu respuesta)_

## Ejercicio 1: un flow sin trigger

Enunciado: el script [`starter/ingesta_simple.py`](./starter/ingesta_simple.py), sin ninguna dependencia externa, registra en un archivo que la ingesta se ejecutó hoy. Hasta ahora lo corres a mano con `python ingesta_simple.py`.

**Respuesta 1, antes de ver la solución:** con lo que sabes de la anatomía de un flow, ¿qué tres campos mínimos necesita el archivo YAML para poder correr este script dentro de Kestra?

_(tu respuesta)_

**Respuesta 2:** si corremos este flow tres veces seguidas desde el botón "Execute", ¿tenemos un flow o tres? ¿tenemos una ejecución o tres?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el flow completo, mientras se revisa en clase)_

## Ejercicio 2: reintentos y horario

Enunciado: el script [`starter/ingesta_inestable.py`](./starter/ingesta_inestable.py) simula una fuente de datos real: la mitad de las veces la conexión falla y el script termina con error, la otra mitad completa la ingesta sin problema.

**Respuesta 1, antes de ver la solución:** si este script falla la mitad de las veces por una razón que no depende de ti, ¿qué le agregarías al flow del Ejercicio 1 para que no dependa de que un humano lo vuelva a correr a mano cuando falla?

_(tu respuesta)_

**Respuesta 2:** si la ejecución de una noche agota sus reintentos y falla, ¿la ejecución programada de la noche siguiente también falla, o corre normal?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el flow completo, con el bloque retry y el trigger Schedule, mientras se revisa en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: el flow de tu propio proyecto

Usa exactamente el mismo patrón de los Ejercicios 1 y 2, aplicado al script de ingesta real de tu proyecto (el que empaquetaste en Docker la Sesión 1 de la semana pasada). Parte de la plantilla [`plantilla-flow/flow_proyecto.yml`](./plantilla-flow/flow_proyecto.yml), que trae los `TODO` marcados en vez del flow en blanco.

### Paso 1: el task que corre tu script (5 minutos)

Completa `id`, `namespace`, y el comando real que corre tu script de ingesta dentro de `commands`.

_(tu id y namespace elegidos)_

### Paso 2: decide el retry (7 minutos)

Piensa en tu fuente de datos real: ¿es una API externa que a veces no responde? ¿un archivo que a veces todavía no está listo? Decide `maxAttempt` e `interval` según qué tan probable y qué tan larga es esa falla, y descomenta el bloque `retry`.

_(tu decisión de retry, y por qué)_

### Paso 3: agrega el trigger Schedule (8 minutos)

Descomenta el bloque `triggers` y elige una expresión cron con la frecuencia que tenga sentido para tu proyecto. No todos los proyectos necesitan correr todos los días.

_(tu expresión cron, y por qué esa frecuencia)_

Sube el flow a la interfaz de Kestra (botón "Create" en la sección Flows, pega el YAML) y ejecútalo manualmente al menos una vez para confirmar que corre sin errores de sintaxis.

_(qué verificaste, y si encontraste algún error)_

## Antes de la próxima sesión

Ya tienes tu pipeline de ingesta corriendo solo, todos los días o con la frecuencia que decidiste.

Pregunta: ¿cómo sabes si los datos que trajo son datos buenos, o datos con problemas que ningún error de ejecución te va a avisar?

_(tu respuesta)_

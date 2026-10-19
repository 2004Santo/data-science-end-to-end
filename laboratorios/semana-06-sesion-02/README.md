# Semana 6, Sesión 2: Procesamiento en tiempo real: ¿lo necesita el proyecto?

> Objetivo de la sesión: decidir si tu proyecto necesita procesamiento en tiempo real, y producir/consumir un flujo simple de eventos con una herramienta de streaming.

**Lectura previa de esta sesión:** ["Introduction to Streaming for Data Scientists"](https://huyenchip.com/2022/08/03/stream-processing-for-data-scientists.html), Chip Huyen.

**Referencia de esta sesión:** ["Batch or Stream? The Eternal Data Processing Dilemma" (Towards Data Science)](https://towardsdatascience.com/batch-or-stream-the-ethernal-data-processing-dilemma/). Este laboratorio usa Redpanda en vez de Apache Kafka con Zookeeper: un solo binario que habla el mismo protocolo de red que Kafka, así que cualquier cliente de Kafka (incluida la librería de Python de este laboratorio) se conecta sin cambios. Es el mismo criterio que ya usó este curso con DuckDB en vez de BigQuery (Semana 5): la herramienta real de la industria es la referencia, y el laboratorio usa la alternativa más simple de levantar en una sola laptop sin perder compatibilidad de protocolo. La misma edición de Data Engineering Zoomcamp que ya sirve de referencia a este curso usa Redpanda en su propio módulo de streaming.

## Requisitos antes de esta sesión

1. **Docker y Docker Compose**, los mismos de la Semana 3.
2. Instala el cliente de Python para Kafka:
   ```
   pip install kafka-python
   ```
3. Levanta Redpanda desde este laboratorio:
   ```
   docker compose up -d
   ```
   El archivo [`starter/docker-compose.yml`](./starter/docker-compose.yml) levanta un solo broker de Redpanda, escuchando en el puerto `9092`, el mismo puerto estándar de Kafka. Verifica que el contenedor arrancó con `docker compose ps`.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué gana un sistema al procesar eventos uno por uno o en microlotes, frente a esperar y procesarlos todos juntos?**

_(tu respuesta)_

**El artículo advierte que streaming no es gratis: agrega complejidad operativa real. ¿Qué tipo de complejidad menciona, comparado con un job de batch?**

_(tu respuesta)_

## Caso de apertura

Un compañero de clase construye un sistema de recomendación de productos y quiere que se actualice apenas un cliente hace clic en algo. Otro construye un modelo que predice el precio de una casa a partir de datos que se publican una vez al mes. ¿Cuál de los dos proyectos se beneficia de procesar los datos en tiempo real, y cuál no gana nada haciéndolo?

_(tu respuesta)_

## Ejercicio 1: producir eventos

Enunciado: Redpanda ya corre en tu máquina. Falta publicar el primer evento a un tópico.

**Respuesta 1, antes de ver la solución:** con evento, tópico, productor, consumidor y broker ya definidos en clase, ¿qué necesitas crear primero para poder publicar un evento: un consumidor o un productor?

_(tu respuesta)_

**Respuesta 2:** si corres el script del productor dos veces seguidas, ¿el tópico `pedidos` termina con 10 o con 20 eventos?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el script completo del productor, mientras se revisa en clase)_

## Ejercicio 2: consumir eventos

Enunciado: con eventos ya publicados en el tópico `pedidos`, falta el lado que los consume.

**Respuesta 1, antes de ver la solución:** el consumidor necesita revertir exactamente lo que hizo `value_serializer` en el productor. ¿Qué dos pasos tiene que deshacer, en qué orden?

_(tu respuesta)_

**Respuesta 2:** si corres este consumidor por segunda vez, después de que ya consumió los 10 eventos la primera vez, ¿los vuelve a mostrar?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el script completo del consumidor, mientras se revisa en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: tu propio proyecto, ¿streaming o batch?

Aplica las dos preguntas que decidieron el caso de apertura a tu propio proyecto, y produce/consume al menos un evento representativo de tu proyecto con Redpanda. Parte de la plantilla [`plantilla-kafka/`](./plantilla-kafka/), que trae los `TODO` marcados en `productor.py` y `consumidor.py` en vez del código en blanco.

### Paso 1: responde las dos preguntas de decisión para tu proyecto (5 minutos)

¿La decisión que tu proyecto habilita pierde valor si se toma con datos de hace una hora, un día o una semana? ¿Los datos de tu proyecto llegan de forma continua e impredecible, o en bloques ya definidos?

_(tus respuestas, y tu conclusión: streaming o batch)_

### Paso 2: escribe tu productor (7 minutos)

Reemplaza el tópico y los eventos de ejemplo por al menos un evento representativo de tu propio proyecto.

_(tu tópico, y los eventos que publicaste)_

### Paso 3: escribe tu consumidor y confirma que recibe lo publicado (8 minutos)

_(qué mostró tu consumidor al correrlo)_

## Antes de la próxima sesión

Ya decidiste si tu proyecto necesita streaming, y produjiste/consumiste tu primer flujo de eventos.

Pregunta: llevas cuatro semanas construyendo piezas sueltas del pipeline de tu proyecto (contenedor, infraestructura, orquestación, calidad, warehouse, modelado, batch, streaming). ¿Qué falta para que todas esas piezas corran juntas, de principio a fin, sin que tengas que ejecutarlas una por una a mano?

_(tu respuesta)_

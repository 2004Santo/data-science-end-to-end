# Semana 3, Sesión 1: Contenedores para pipelines de proyectos

> Objetivo de la sesión: empaquetar el entorno de trabajo de tu proyecto propio en una imagen de Docker reproducible, y explicar qué problema de "funciona en mi máquina" resuelve un contenedor.

**Lectura previa de esta sesión:** ["How Docker Can Help You Become a More Effective Data Scientist"](https://medium.com/data-science/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5), Towards Data Science / Medium.

**Referencia de esta sesión:** [Data Engineering Zoomcamp, Módulo 1 (DataTalksClub)](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform).

## Requisitos antes de esta sesión

Abre el Codespace de tu fork (ver [Tu ambiente de desarrollo](../../README.md#tu-ambiente-de-desarrollo) en el README del repositorio): Docker ya viene instalado. Confirma que funciona corriendo `docker run hello-world` en la terminal. Si prefieres trabajar en tu laptop, instala [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows, Mac o Linux) y corre la misma verificación. Si tu proyecto necesita GPU o un ambiente que no corre bien en ninguna de las dos opciones, avísame antes de esta sesión.

El Codespace también es un contenedor, pero no reemplaza el Dockerfile que construyes hoy. El Codespace trae las herramientas del curso, iguales para todos. La imagen de tu proyecto trae solo lo que tu proyecto necesita para correr en cualquier máquina, incluida una que nunca abrió este repositorio.

## Antes de empezar

A partir de la lectura previa:

**Según el artículo, ¿qué diferencia hay entre una imagen de Docker y un contenedor?**

_(tu respuesta)_

**¿Qué captura Docker, además de las librerías de Python, que un `requirements.txt` por sí solo no captura?**

_(tu respuesta)_

## Pregunta de apertura

¿Por qué un notebook que corre perfecto en mi laptop podría fallar por completo en la tuya, aunque ambos tengan el mismo código?

_(tu respuesta)_

## Ejercicio 1: un script sin dependencias

Enunciado: el script [`starter/analisis.py`](./starter/analisis.py), que solo usa la biblioteca estándar de Python, funciona en tu laptop. Yo tengo una versión distinta de Python instalada y no logro correrlo sin ajustar mi propio ambiente.

**Respuesta 1, antes de ver la solución:** con lo que sabes de la anatomía de un Dockerfile, ¿qué instrucción usarías para decirle a Docker qué versión de Python usar como base?

_(tu respuesta)_

**Respuesta 2:** si cambiamos una línea dentro de `analisis.py` y volvemos a construir la imagen, ¿Docker vuelve a descargar la imagen base de Python desde cero, o reutiliza algo?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el Dockerfile completo y los comandos de build/run, mientras se revisan en clase)_

## Ejercicio 2: un script con dependencias y datos

Enunciado: el script [`starter/procesar.py`](./starter/procesar.py) usa pandas para leer [`starter/datos/ventas.csv`](./starter/datos/ventas.csv) y generar un resumen. El resultado debe quedar disponible como un archivo que puedas abrir fuera del contenedor.

**Respuesta 1, antes de ver la solución:** comparado con el Ejercicio 1, ¿qué dos cosas nuevas necesita este Dockerfile, ahora que el script tiene una dependencia externa y produce un archivo de salida?

_(tu respuesta)_

**Respuesta 2:** ¿por qué copiaríamos `requirements.txt` e instalaríamos las dependencias antes de copiar `procesar.py`, en vez de copiar todo el proyecto de una sola vez?

_(tu respuesta)_

**La formulación completa, tal como la resuelvo yo:**

_(anota aquí el Dockerfile completo, el comando con volumen, y por qué el orden de las instrucciones importa, mientras se revisan en clase)_

## Durante el ConcepTest

**Tu voto, antes de discutir en pareja** (A, B, C o D):

_(tu voto)_

**Tu razonamiento:**

_(tu respuesta)_

**Después de discutir en pareja, ¿cambiaste de voto? ¿Por qué?**

_(tu respuesta)_

## Ejercicio 3: el Dockerfile de tu propio proyecto

Usa exactamente el mismo patrón de los Ejercicios 1 y 2, aplicado al ambiente real de tu proyecto. Parte de la plantilla [`plantilla-dockerfile/Dockerfile`](./plantilla-dockerfile/Dockerfile), que trae los `TODO` marcados en vez del Dockerfile en blanco.

### Paso 1: identifica tus dependencias reales (5 minutos)

Lista las librerías externas que tu proyecto necesita (lo que normalmente instalarías con `pip install`). Si todavía no tienes un `requirements.txt`, créalo ahora con esa lista.

_(tu lista de dependencias)_

### Paso 2: completa el Dockerfile (10 minutos)

Edita `plantilla-dockerfile/Dockerfile`: resuelve cada `TODO`, decidiendo el orden de las instrucciones pensando en la cache (dependencias antes que código), y agrega un volumen en tus notas si tu proyecto lee o escribe datos.

### Paso 3: construye y verifica (5 minutos)

```
docker build -t <nombre-de-tu-proyecto> .
docker run <con -v si tu proyecto usa datos> <nombre-de-tu-proyecto>
```

Confirma que el resultado dentro del contenedor coincide con correr tu código directamente en tu máquina.

_(qué verificaste, y si encontraste alguna diferencia)_

## Antes de la próxima sesión

Ya tienes tu proyecto empaquetado en una imagen reproducible.

Pregunta: ¿qué pasa si necesitas provisionar el almacenamiento de datos donde ese contenedor va a leer y escribir, sin hacerlo a mano cada vez?

_(tu respuesta)_

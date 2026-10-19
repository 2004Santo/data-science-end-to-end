# Diagnóstico de calidad de datos: [nombre de tu proyecto]

Dataset analizado: [nombre o ruta del archivo]. Fecha del diagnóstico: [TODO].

## Duplicados

**¿Cuántas filas duplicadas encontraste?** (`datos.duplicated().sum()`)

_(TODO)_

**¿Por qué crees que existen?** (¿error de ingesta, de combinación de fuentes, evento legítimo repetido?)

_(TODO)_

**Estrategia y justificación:**

_(TODO)_

## Valores faltantes

**¿Qué columnas tienen valores faltantes, y cuántos por columna?** (`datos.isna().sum()`, y revisa también valores como "N/D", "-" o vacíos que `isna()` no detecta directamente)

_(TODO)_

**¿Faltan al azar, o siguen un patrón relacionado con otra variable?**

_(TODO)_

**Estrategia y justificación por columna:**

_(TODO)_

## Inconsistencias de esquema

**¿Alguna columna tiene el tipo de dato incorrecto según `datos.dtypes`?**

_(TODO)_

**¿Alguna columna mezcla formatos (fechas, categorías escritas de más de una forma, unidades distintas)?**

_(TODO)_

**Estrategia y justificación:**

_(TODO)_

## Resumen

**De los problemas encontrados, ¿cuál priorizarías corregir primero, y por qué?**

_(TODO)_

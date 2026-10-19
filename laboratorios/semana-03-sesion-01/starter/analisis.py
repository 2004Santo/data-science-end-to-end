# Ejercicio 1: no tiene dependencias externas, solo biblioteca estandar de Python.
# Lo resuelvo en clase junto con su Dockerfile.

def resumen(numeros):
    return {
        "cantidad": len(numeros),
        "suma": sum(numeros),
        "promedio": sum(numeros) / len(numeros) if numeros else 0,
    }


if __name__ == "__main__":
    datos = [12, 45, 7, 89, 23, 56, 34]
    resultado = resumen(datos)
    print("Resumen del analisis:")
    for clave, valor in resultado.items():
        print(f"  {clave}: {valor}")

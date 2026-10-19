import datetime

fecha = datetime.date.today()
with open("registro_ingesta.txt", "a") as archivo:
    archivo.write(f"Ingesta ejecutada para la fecha {fecha}\n")
print(f"Ingesta completada para {fecha}")

import csv
from datetime import datetime

# Leer datos
input_file = "data.csv"
output_file = "resultado.csv"
log_file = "log.txt"

datos_filtrados = []

with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row) 
        if int(row["edad"]) >= 18:
            datos_filtrados.append(row)

# Guardar resultados
with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["nombre", "edad", "ciudad"])
    writer.writeheader()
    writer.writerows(datos_filtrados)

# Crear log
with open(log_file, mode='a') as log:
    now = datetime.now()
    log.write(f"Se filtraron {len(datos_filtrados)} registros | Fecha: {now} | Archivo: {input_file}\n")

print("Proceso completado")
import csv

nombre = ["Juan", "Pedro", "Carlos","Andres"]
edad = [20, 18, 15, 19]
Ciudad= ["Miami", "Armenia","cartagena", "Barranquilla"]

with open('C:\\Users\\B09S202est\\Documents\\programacion-2025\\prog-2025-2-10am-unidad5-Juan-David-v\\ARCHIVOS\\Ejercicio_listas.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])
    escritor.writerow(nombre)
    escritor.writerow(edad)
    escritor.writerow(Ciudad)

    print(nombre)
    print(edad)
    print(Ciudad)

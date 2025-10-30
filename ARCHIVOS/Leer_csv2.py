import csv #se hace el cambio de la , por un . trabajando con la columna 3 del archivo

with open('C:\\Users\\B09S202est\\Documents\\programacion-2025\\prog-2025-2-10am-unidad5-Juan-David-v\\ARCHIVOS\\Variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    encabezado= next(lector) # next copia toda la fila, salta la fila y pasa la siguiente
    #print(encabezado)
    presion = []
    print(encabezado[0])
    for fila in lector: #con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace(",",".") # replace cambia lo que habia antes por algo nuevo 
        dato = float(fila[3])
        presion.append(dato)
print(presion)

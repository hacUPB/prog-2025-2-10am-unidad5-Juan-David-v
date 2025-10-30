# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
ubicacion= "C:\\Users\\B09S202est\\Desktop\\Archivos"
modo = "w"

# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8") as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = input("Ingrese los datos que desea escribir en el archivo: ")
    archivo.write(datos)

# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
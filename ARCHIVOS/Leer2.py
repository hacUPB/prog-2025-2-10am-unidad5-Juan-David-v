from io import SEEK_END


archivo = open("./ARCHIVOS/texto2.txt","r")
#for i in range(3):
#    datos = archivo.readline()
#print(datos[11:])

# IMPRIMIR POR MEDIO DE BUCLE FOR 

#archivo.readline()
#archivo.readline()
#archivo.read(11)
archivo.seek(10)
datos = archivo.readline()
archivo.close()
print(datos)
 
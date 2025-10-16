# abrir el archivo y definir el modo 
archivo = open("./ARCHIVOS/texto.txt", "r")
#2. leer datos del archivo
#datos = archivo.read(10)
#datos = archivo.readline() # lee y abre el archivo al principio y cada operacion que hace va acomulando dependeindo de cuantas operaciones haga 
#for i in range (5):
 #   datos= archivo.readline() # lee desde la linea 0 a la 5  me imprimiria la linea 5
#for datos in archivo:  imprime la primera letra de cada linea 
 #   print(datos[0])

datos = archivo.readlines()
print (datos)


# 3. cerrar el archivo
archivo.close()
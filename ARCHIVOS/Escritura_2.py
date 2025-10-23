ubicacion= "C:\\Users\\B09S202est\\Desktop\\Archivos"
#se usa para comandos de texto 
nombre_archivo ="escritura2.txt"
modo= "a" # solo escribe 
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
frase= input("Por favor ingresar una frase: ")
#solicitar una variable entera y una float al usuario y escribirla en el archivo
edad= str(input("ingrese la edad : "))
estatura= float(input("Ingrese su estatura: "))
fp.write(frase+"\n") 
fp.write(str(edad)+"\n")
fp.write(str(estatura)+"\n") 


fp.close()

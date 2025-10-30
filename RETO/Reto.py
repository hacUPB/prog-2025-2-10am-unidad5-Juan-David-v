import os, sys, csv

TIENE_MATPLOTLIB = True
try:
    import matplotlib.pyplot as graf
except Exception:
    TIENE_MATPLOTLIB = False

# ---------- FUNCIONES GENERALES ----------
def limpiar_pantalla():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except:
        pass

def pausar():
    try:
        input("\nPresiona Enter para continuar...")
    except:
        pass

def mostrar_archivos():
    print("\n1) Carpeta actual\n2) Especificar ruta")
    opcion = input("Opción: ").strip()
    ruta = "." if opcion != "2" else input("Ruta: ").strip()
    try:
        print("\nContenido de:", os.path.abspath(ruta))
        for archivo in os.listdir(ruta):
            print(" -", archivo)
    except Exception as error:
        print("Error:", error)

# ---------- ARCHIVOS .TXT ----------
def leer_texto(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except Exception as error:
        print("No se pudo leer:", error)
        return None

def escribir_texto(ruta, contenido):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
            return True
    except Exception as error:
        print("No se pudo escribir:", error)
        return False

def contar_texto(ruta):
    texto = leer_texto(ruta)
    if texto is None:
        return
    palabras = texto.split()
    total_palabras = len(palabras)
    caracteres_con_espacios = len(texto)
    caracteres_sin_espacios = sum(1 for c in texto if not c.isspace())
    print("\nPalabras:", total_palabras)
    print("Caracteres (con espacios):", caracteres_con_espacios)
    print("Caracteres (sin espacios):", caracteres_sin_espacios)

def reemplazar_texto(ruta):
    texto = leer_texto(ruta)
    if texto is None:
        return
    palabra_original = input("Palabra a buscar: ").strip()
    palabra_nueva = input("Reemplazar por: ").strip()
    if palabra_original == "":
        print("No puede ser vacía.")
        return
    if escribir_texto(ruta, texto.replace(palabra_original, palabra_nueva)):
        print("Archivo actualizado.")

def contar_vocales(ruta):
    texto = leer_texto(ruta)
    if texto is None:
        return
    vocales = ["a", "e", "i", "o", "u"]
    conteos = [0] * 5
    for caracter in texto.lower():
        if caracter in vocales:
            conteos[vocales.index(caracter)] += 1
    print("\nOcurrencias de vocales:")
    for i in range(5):
        print(f" {vocales[i]} : {conteos[i]}")
    if TIENE_MATPLOTLIB:
        graf.bar(vocales, conteos)
        graf.title("Frecuencia de vocales")
        graf.xlabel("Vocal")
        graf.ylabel("Cantidad")
        graf.show()
    else:
        print("( no se muestra gráfico)")

def menu_txt():
    print("\nArchivos disponibles en carpeta 'RETO':")
    try:
        for archivo in os.listdir("RETO"):
            if archivo.lower().endswith(".txt"):
                print(" -", archivo)
    except FileNotFoundError:
        print(" Carpeta 'RETO' no encontrada. Créala en el mismo nivel del programa.")
        pausar()
        return

    nombre = input("\nNombre del archivo .txt (solo el nombre): ").strip()
    ruta = os.path.join("RETO", nombre)

    if not os.path.exists(ruta):
        print("El archivo no existe en la carpeta 'RETO'. Verifica el nombre.")
        pausar()
        return

    while True:
        print("\nTXT: 1) Contar  2) Reemplazar  3) Gráfico de vocales  4) Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            contar_texto(ruta)
            pausar()
        elif opcion == "2":
            reemplazar_texto(ruta)
            pausar()
        elif opcion == "3":
            contar_vocales(ruta)
            pausar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

# ---------- ARCHIVOS .CSV ----------
def abrir_csv(ruta):
    try:
        archivo = open(ruta, "r", newline="", encoding="utf-8")
        return archivo, csv.reader(archivo)
    except Exception as error:
        print("No se pudo abrir:", error)
        return None, None

def mostrar_cabecera_csv(ruta):
    archivo, lector = abrir_csv(ruta)
    if lector is None:
        return
    contador = 0
    try:
        for fila in lector:
            print(fila)
            contador += 1
            if contador >= 15:
                break
    finally:
        archivo.close()

def leer_csv_completo(ruta):
    archivo, lector = abrir_csv(ruta)
    if lector is None:
        return None
    datos = []
    try:
        for fila in lector:
            datos.append(fila)
    finally:
        archivo.close()
    return datos

def indice_columna(encabezados, entrada):
    if entrada.isdigit():
        i = int(entrada)
        return i if 0 <= i < len(encabezados) else -1
    for i, nombre in enumerate(encabezados):
        if nombre == entrada:
            return i
    return -1

def columna_a_float(filas, indice):
    valores = []
    for fila in filas:
        if indice < len(fila):
            valor = fila[indice].strip()
            if valor != "":
                try:
                    valores.append(float(valor.replace(",", ".")))
                except:
                    pass
    return valores

def estadisticas_basicas(valores):
    n = len(valores)
    if n == 0:
        return (0, None, None, None, None, None)
    promedio = sum(valores) / n
    ordenados = sorted(valores)
    minimo, maximo = ordenados[0], ordenados[-1]
    if n % 2 == 1:
        mediana = ordenados[n // 2]
    else:
        mediana = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
    desviacion = (sum((x - promedio) ** 2 for x in valores) / n) ** 0.5
    return (n, promedio, mediana, desviacion, minimo, maximo)

def estadisticas_csv(ruta):
    datos = leer_csv_completo(ruta)
    if not datos:
        print("CSV vacío o no válido.")
        return
    encabezados = datos[0]
    print("\nEncabezados disponibles:")
    for i, nombre in enumerate(encabezados):
        print(f"  [{i}] {nombre}")
    seleccion = input("Nombre o índice de columna: ").strip()
    indice = indice_columna(encabezados, seleccion)
    if indice == -1:
        print("Columna no encontrada.")
        return
    valores = columna_a_float(datos[1:], indice)
    n, prom, med, desv, mn, mx = estadisticas_basicas(valores)
    print("\nCantidad:", n)
    print("Promedio:", prom)
    print("Mediana:", med)
    print("Desviación estándar:", desv)
    print("Mínimo:", mn)
    print("Máximo:", mx)

def graficar_csv(ruta):
    if not TIENE_MATPLOTLIB:
        print("Matplotlib no disponible.")
        return
    datos = leer_csv_completo(ruta)
    if not datos:
        print("CSV vacío o no válido.")
        return
    encabezados = datos[0]
    print("\nEncabezados disponibles:")
    for i, nombre in enumerate(encabezados):
        print(f"  [{i}] {nombre}")
    seleccion = input("Columna numérica (nombre o índice): ").strip()
    indice = indice_columna(encabezados, seleccion)
    if indice == -1:
        print("Columna no encontrada.")
        return
    x, y = [], []
    for idx, fila in enumerate(datos[1:]):
        if indice < len(fila):
            valor = fila[indice].strip()
            if valor != "":
                try:
                    y.append(float(valor.replace(",", ".")))
                    x.append(idx)
                except:
                    pass
    if len(y) == 0:
        print("No hay datos numéricos válidos.")
        return
    graf.figure()
    graf.scatter(x, y)
    graf.title(f"Dispersión - {encabezados[indice]}")
    graf.xlabel("Índice")
    graf.ylabel(encabezados[indice])
    graf.show()

    # Histograma
    minimo, maximo = min(y), max(y)
    bins = 5
    ancho = (maximo - minimo) / bins if bins > 0 else 1
    etiquetas, frecuencias = [], [0] * bins
    for b in range(bins):
        lim_inf = minimo + b * ancho
        lim_sup = minimo + (b + 1) * ancho if b < bins - 1 else maximo
        etiquetas.append(f"{lim_inf:.2f}-{lim_sup:.2f}")
    for valor in y:
        for b in range(bins):
            li, ls = map(float, etiquetas[b].split("-"))
            if li <= valor < ls or (b == bins - 1 and valor <= ls):
                frecuencias[b] += 1
                break
    graf.figure()
    graf.bar(etiquetas, frecuencias)
    graf.title(f"Frecuencia por rangos - {encabezados[indice]}")
    graf.xlabel("Rango")
    graf.ylabel("Frecuencia")
    graf.xticks(rotation=45)
    graf.tight_layout()
    graf.show()

def menu_csv():
    print("\nArchivos disponibles en carpeta 'RETO':")
    try:
        for archivo in os.listdir("RETO"):
            if archivo.lower().endswith(".csv"):
                print(" -", archivo)
    except FileNotFoundError:
        print("Carpeta 'RETO' no encontrada. Créala en el mismo nivel del programa.")
        pausar()
        return

    nombre = input("\nNombre del archivo .csv (solo el nombre): ").strip()
    ruta = os.path.join("RETO", nombre)

    if not os.path.exists(ruta):
        print("1 El archivo no existe en la carpeta 'RETO'. Verifica el nombre.")
        pausar()
        return

    while True:
        print("\nCSV: 1) Ver primeras 15 filas  2) Estadísticas  3) Gráficas  4) Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            mostrar_cabecera_csv(ruta)
            pausar()
        elif opcion == "2":
            estadisticas_csv(ruta)
            pausar()
        elif opcion == "3":
            graficar_csv(ruta)
            pausar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

# ---------- MENÚ PRINCIPAL ----------
def main():
    limpiar_pantalla()
    print("CLI Unidad 5 - Archivos y Visualización\n")
    if not TIENE_MATPLOTLIB:
        print("Aviso: matplotlib no está instalado; las opciones gráficas no funcionarán.")
    while True:
        print("\n1) Listar archivos\n2) Archivos .TXT\n3) Archivos .CSV\n4) Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            mostrar_archivos()
            pausar()
        elif opcion == "2":
            menu_txt()
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            print("Adiós")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrumpido.")
        sys.exit(0)

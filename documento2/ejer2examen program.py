VOCALES = "aeiou"
CONSONANTES = "qwrtypsdfghjklñzxcvbnm"

def transformar_palabra(palabra):
    transformada = []
    longitud_par = len(palabra) % 2 == 0
    
    for caracter in palabra:
        if longitud_par:
            if caracter.lower() in VOCALES:
                continue  # Eliminar vocales
            else:
                transformada.append(caracter)
        else:
            if caracter.lower() in CONSONANTES:
                transformada.append('#')  # Reemplazar consonantes por '#'
            else:
                transformada.append(caracter)
    
    return ''.join(transformada)

def leer_fichero(ruta_lectura):
    with open(ruta_lectura, "r") as fichero:
        contenido = fichero.readlines()
    return contenido

def escribir_fichero(ruta_escritura, contenido):
    with open(ruta_escritura, "w") as fichero:
        fichero.write(contenido)

ruta_lectura = "C://Users//Ricardo Posada//Desktop//documento2//documento2.txt"
contenido = leer_fichero(ruta_lectura)

contenido_transformado = ""
for linea in contenido:
    palabras_en_linea = linea.split()
    for palabra in palabras_en_linea:
        pal_transformada = transformar_palabra(palabra)
        contenido_transformado += pal_transformada
        contenido_transformado += " "
    contenido_transformado += "\n"

ruta_escritura = "solucion2.txt"
salida = escribir_fichero(ruta_escritura, contenido_transformado)
print(salida)
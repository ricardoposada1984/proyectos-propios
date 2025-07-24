
def cifrar(texto):
    vocales = {'a': '3', 'e': '4', 'i': '5', 'o': '6', 'u': '7'}
    resultado = []
    for palabra in texto.split():
        if len(palabra) % 2 == 0:  # longitud par
            nueva_palabra = ''.join([vocales.get(letra.lower(), letra) for letra in palabra])
        else:  # longitud impar
            nueva_palabra = ''.join(['#' if letra.lower() not in vocales else letra for letra in palabra])
        resultado.append(nueva_palabra)
    return ' '.join(resultado)

# Leer el fichero
#with open("C://Users//Ricardo Posada//Desktop//documento2//documento2.txt", 'r') as f:
    #texto = f.read().replace("-", "")

with open("C://Users//Ricardo Posada//Desktop//documento2//documento2.txt", 'r') as f:
    contenido = f.read()
    print(contenido)
         



#Cifrar el texto
texto_cifrado = cifrar(contenido)

#Guardar el resultado
with open('solucion2.txt', 'w') as f:
    f.write(texto_cifrado)
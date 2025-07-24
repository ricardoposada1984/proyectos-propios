
# Ejercicio de cifrado :)


def cifrar(texto):
    vocales = {'a': '3', 'e': '4', 'i': '5', 'o': '6', 'u': '7'}
    texto_cifrado = ""
    palabras = texto.split()
    for palabra in palabras:
        palabra_cifrada = ""
        if len(palabra) % 2 == 0:  # longitud par
            for letra in palabra:
                if letra.lower() in vocales:
                    palabra_cifrada += vocales[letra.lower()]
                else:
                    palabra_cifrada += letra
        else:  # longitud impar
            for letra in palabra:
                if letra.lower() not in vocales:
                    palabra_cifrada += "#"
                else:
                    palabra_cifrada += letra
        texto_cifrado += palabra_cifrada + " "
    return texto_cifrado.rstrip()

with open('C://Users//Ricardo Posada//Desktop//documento2//documento2.txt', 'r') as f:
    texto = f.read()

texto_cifrado = cifrar(texto)

with open('solucion2.txt', 'w') as f:
    f.write(texto_cifrado)
print(texto)
print(texto_cifrado)
# 1. necesitamos las imagenes del ahorcado
# y una lista de palabras vamos a conseguirlas online :) 
# listo ahora, vamos a programar !!!

import random
from palabras_del_ahorcado import palabras
from diagramas_ahoracado import vidas_diccionario_visual
import string



intro = '<>'
print(intro*20)
print("<><><><> Bienvenido a ahorcado <><><><>")
print(intro*20)



def palabra_valida():
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()


def ahorcado():
    palabra = palabra_valida()
    
    vidas = 7
    vidas = int(vidas)
    letras_por_adivinar = set(palabra)
    abecedario1 = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    abecedario2 = set(string.ascii_uppercase)
    letras_adivinadas = set()
    
    while vidas > 0 and len(letras_por_adivinar) > 0:
        print(f"Te quedan {vidas} vidas",
         f"Haz usado las letras : {' '.join(letras_adivinadas)} " )

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]

        print(f"Palabra: {' '.join(palabra_lista)}")
        print(vidas_diccionario_visual[vidas])

        letra_usuario = input("Escribe un letra: ").upper()

        if letra_usuario in abecedario1 - letras_adivinadas:
            letras_adivinadas.add(letra_usuario) 

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)

            else:
                vidas -= 1 
                print(f"\n La letra, {letra_usuario} no está en la palabra")      

        elif letra_usuario in letras_adivinadas:
            print(f"\n Ya  escogiste la letra {letra_usuario}, por favor escoge una nueva :)") 
        else:
            print("\n Ese caracter no es valido, por favor escoge un caracter valido")

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"!Ahorcado!,haz perdido! :( la palabra era {palabra}") 
    else:
        print(f"Felicidades :), haz adivinado la palabra era {palabra}!")           

ahorcado()        

# Ok vamos a crear un programa que le pida
# al usuario que adivine un número del
# 1 al 20.

# Se puede mejorar permitiendole al usuario que escoja 
# que tan grande es el intervalo para adivinar el numero 
# de 1 a x.

# tambien se puede mejorar dandole pistas al usuario conforme falla
# como que el numero es primo, o multiplo de otro.

import random


print(" ") 

print('========================================')
print('======= Bienvenid@ al juego ============')
print('======= vamos a adivinar un ============')
print('======= número del 1 al 20 :) :) =======')
print('========================================')

print(" ")

numero = random.randint(1, 20)
usuario = input("Elije un numero: ")
usuario = int(usuario)

while numero != usuario:
    if numero > usuario:
        usuario = input('Elige un numero mas grande: ')
        usuario = int(usuario)
    elif numero < usuario:
        usuario = input('Elige un número mas pequeño: ')
        usuario = int(usuario)
 
print(f"felicidades haz adivinado, el número era {numero}")        

    


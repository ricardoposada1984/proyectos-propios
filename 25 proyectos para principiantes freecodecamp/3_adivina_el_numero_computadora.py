
# En este caso queremos que la computadora adivine un numero
# que generaremos previamente, el numero puede ser de 1 a 100
# pero tambien podemos adaptar el juego para que sea de 1 a x.
# programaremos la computadora para que restrinja el intervalo de
# busqueda según las pistas que tu les das :)

import random

print(" ") 

print('========================================')
print('======= Bienvenid@ al juego ============')
print('======= la computadora adivinará =======')
print('======= número del 1 al 100 :) :) =======')
print('========================================')

print(" ")

limite_inferior = int(1)
limite_superior = int(101)

list1 = list(range(limite_inferior, limite_superior))
usuario = input("""ingresa un numero
para que lo adivine la computadora: """)
usuario = int(usuario)
computadora = random.choice(list1)
print(f"La computadora dice {computadora}")
pista = None

while computadora != usuario:
    pista = input("""Dile a la computadora
    si tu número es mas grande, tecleando g
    o mas pequeño, tecleando p:  """)
    if pista == "g":
        limite_inferior = computadora + 1 
        list1 = list(range(limite_inferior , limite_superior))
        computadora = random.choice(list1) 
        print(f"La computadora dice {computadora}")  
    elif pista == "p":
        limite_superior = computadora
        list1 = list(range(limite_inferior, limite_superior))
        computadora = random.choice(list1)
        print(f"La computadora dice {computadora}")
        

print(f"""La computadora ha adivinado tu número,
el número es {computadora}""")        




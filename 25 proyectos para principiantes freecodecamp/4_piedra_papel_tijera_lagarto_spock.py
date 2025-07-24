

# Vamos a crear este juego inspirado en piedra 
# papel y tijera, mejorado por un pionero de
# internet llamado cash a piedra-papel-tijera-lagarto Spock
# y explicado magistralmente por Sheldon Cooper:

# Las reglas se pueden ver en:
# https://www.youtube.com/watch?v=C7gneuyNLwE&ab_channel=wredants
 
# 1. Tijeras cortan Papel
# 2. Papel envuelve Piedra
# 3. Piedra aplasta Lagarto
# 4. Lagarto envenena a Spock
# 5. Spock aplasta Tijeras 
# 6. Tijeras decapita al Lagarto
# 7. Lagarto se come Papel
# 8. Papel refuta a Spock
# 9. Spock desintegra la Piedra
# y como siempre....
# 10. Piedra aplasta Tijeras :)

# Posibles mejoras:

# 1. Reescribiendolo usando clases
# y observar si el código es mas eficiente 
# intuitivo o mejora en algo para otro 
# programador que lo lea.

# 2. hacerlo player vs player y cp vs cp ??

# 3. Es posible darle a la computadora 
# nombres famosos, como los personajes de
# la serie, con otro random.choice

# 4. Para mas de 2 jugadores :)

# Poner imagen de bienvenida :)

import random as random


print("""Escoge pi: para piedra
       pa: para papel
       ti: para tijera
       la: lagarto
       sp: para Spock
       Vamos a jugar :) """)

print("""Gana quien primero, le tome
2 puntos de ventaja al oponente""")       

list = ["pi","pa","ti","la","sp"]
jug1 = input("Escribe tu nombre jugador 1: ")
cp_score = 0
jug1_score = 0
round = 0
while abs(cp_score - jug1_score) < 2:
    
    print("************************")
    print(f"Ronda  {round}")
    print(f"{jug1}   => {jug1_score}")
    print(f"cp       => {cp_score}")
    print("************************")
    print(" ")
    round += 1
    p1 = input(f"Tu turno {jug1}: ").lower()
    cp = random.choice(list)
    
    if  p1 == cp and p1 in list:
        print("Empate!")
    elif p1 == "ti":
        if cp == "pa":
            print(f"La tijera corta el papel, {jug1} gana") 
            jug1_score += 1
        if cp == "pi":
            print("La piedra aplasta la tijera, la computadora gana")
            cp_score += 1   
        if cp == "la":
            print(f"La tijera decapita el lagarto, {jug1} gana")
            jug1_score += 1
        if cp == "sp":
            print("Spock aplasta las tijeras,la computadora gana")
            cp_score += 1 
    elif p1 == "pa":
        if cp == "ti":
            print("La tijera corta el papel,la computadora gana")
            cp_score += 1 
        if cp == "pi":
            print(f"El papel envuelve la piedra, {jug1} gana")   
            jug1_score += 1           
        if cp == "la":
            print("El lagarto se come el papel, la computadora gana")
            cp_score += 1
        if cp == "sp":
            print(f"El papel desacredita a Spock, {jug1} gana")
            jug1_score += 1
    elif p1 == "pi":
        if cp == "pa":
            print("El papel envuelve la piedra,la computadora gana") 
            cp_score += 1 
        if cp == "ti":
            print(f"la piedra aplasta la tijera, {jug1} gana")   
            jug1_score += 1
        if cp == "la":
            print(f"la piedra aplasta el lagarto, {jug1} gana")
            jug1_score += 1
        if cp == "sp":
            print("Spock desintegra la piedra, computadora gana")
            cp_score += 1
    elif p1 == "la":
        if cp == "pa":
            print(f"El lagarto se come el papel, {jug1} gana") 
            jug1_score += 1
        if cp == "ti":
            print("La tijera decapita el lagarto, computadora gana")   
            cp_score += 1
        if cp == "pi":
            print("la piedra aplasta el lagarto, computadora gana")
            cp_score += 1
        if cp == "sp":
            print(f"EL lagarto envenena a Spock, {jug1} gana")
            jug1_score += 1

    elif p1 == "sp":
        if cp == "pa":
            print(f"El papel desacredita a Spock, computadora gana") 
            cp_score += 1
        if cp == "ti":
            print(f"Spock aplasta las tijeras, {jug1} gana")  
            jug1_score += 1
        if cp == "pi":
            print(f"Spock desintegra la piedra, {jug1} gana")
            jug1_score += 1
        if cp == "la":
            print("El lagarto envenena a Spock, computadora gana")
            cp_score += 1
    else:
        print("teclea una opción correcta")    

if jug1_score > cp_score:
    print(f"""Fin del juego ha ganado {jug1}:
    jug1 => {jug1_score}
    cp => {cp_score}""")
else:
   print(f"""Fin del juego la computadora 
    ha ganado:
    jug1 => {jug1_score}
    cp => {cp_score}""") 


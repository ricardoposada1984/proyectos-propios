# El objetivo es determinar si un numero dado
# es primo.

import time
import math

n = input("Escribe el numero para decidir si es primo: ")
n = int(n)

# Busqueda ingenua

def busqueda_ingenua(n):
    
    div1 = []
    for i in range(1, n+1):
        if n%i == 0:
            div1.append(i)

    if len(div1) == 2:
        print(f"El numero {n} es primo, sus divisores son {div1}")
    else:
        print(f"""El numero {n} tiene los divisores {div1},
        por tanto no es primo""")

t1 = time.time()
busqueda_ingenua(n)
t2 = time.time()
print(f"t inicial busqueda ingenua = {t1}")
print(f"t final busqueda ingenua = {t2}") 
print(f"tiempo de la busqueda ingenua es: {t2-t1}")        


# Busqueda binaria
 
def busqueda_binaria(n):
    div2 = []
    sup = n
   
    for i in range(1, sup + 1):
        if n%i == 0:
            div2.append(i)
            sup = int(sup/i)    
        
    if len(div2) == 2:
        print(f"El numero {n} es primo, sus divisores son {div2}")
    else:
        print(f"""El numero {n} tiene los divisores {div2},
        por tanto no es primo""") 

t3 = time.time()
busqueda_binaria(n)
t4 = time.time() 
print(f"t inicial busqueda binaria = {t3}")
print(f"t final busqueda binaria = {t4}") 
print(f"tiempo de la busqueda binaria es: {t4-t3}")    


# a veces gana la busqueda la ingenua,
# para comprobarlo mejor vale la pena hacer un ciclo
# con 10 0 100 veces el mismo cálculo para
# evaluar cual es mejor en promedio :)
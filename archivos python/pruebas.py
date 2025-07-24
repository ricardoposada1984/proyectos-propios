
import time

# crear un reloj digital
# 00, 01, 02, 03, ..., 59

# 1. crear una lista de dobles digitos 

doble_digito_1 = [f"0{i}" for i in range (0, 10)]
doble_digito_2 = [f"{i}" for i in range (10, 60)]
doble_digitos = doble_digito_1 + doble_digito_2

# 2. crear los componentes de las horas, minutos y segundos
# mediante slices:


horas = doble_digitos[:24]
minutos = doble_digitos
segundos = doble_digitos

# 3. crear la funcion que da la hora, llamada reloj

def reloj(h,m,s):
    return f"{horas[h]}:{minutos[m]}:{segundos[s]}"


# 4. iniciar el reloj
 
s = 0
h = 0
m = 0

# 5. crear el ciclo que da inicio a la impresion de la hora !!! 

while s < 60 and m < 60:
    
    print (reloj(h,m,s))
    s = s + 1
    time.sleep(1)

    if s == 60:
       s = 0
       m = m+1
       time.sleep(1)
    if m == 60:
       m = 0
       h = h+1
       time.sleep(1)
    if h == 24:
       h = 0    
       time.sleep(1)
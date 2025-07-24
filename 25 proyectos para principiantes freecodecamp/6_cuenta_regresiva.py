import time

# Cuenta regresiva para algunos segundos
t1 = input("Por favor ingrese el inicio de la cuenta regresiva: ")
t1 = int(t1)
for i in range(0,t1):
    print(t1-i)
    time.sleep(1)
     
print("Se acabó el tiempo !")

# podemos mejorarlo haciendo un reloj digital asi:

t2 = input("Por favor ingrese el tiempo en segundos, para la cuenta regresiva: ")
t2 = int(t2)
for t2 in range(t2, 0, -1):
    segundos = t2 % 60
    minutos = int(t2/60)%60
    horas = int(t2/3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)
print("Se acabó el tiempo !")
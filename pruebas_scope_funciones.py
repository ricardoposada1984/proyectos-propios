
import random
import time


def rondas(ronda):
    print(f"Listo vamos con la ronda {ronda} !!!")
    jugada = int(input(f"Dame un numero entre 0 y 10  "))
    ronda += 1
    return jugada, ronda


print(rondas(1))






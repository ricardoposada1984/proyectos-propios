import string
import random

print("Bienvenido a tu generador de contraseñas")
print("Acá podras varias contraseñas de la longitud que quieras")
print("Ejemplo HfTmKim9€ ES 1 contraseña de longitud 9")
print("Porque contiene 9 caracteres, es tu turno !!!")
print(" ")


longitud = input("Por favor ingrese la longitud deseada: ")
longitud = int(longitud)
numero = input("Por favor ingresa, cuantas contraseñas quieres: ")
numero = int(numero)
caracteres = string.ascii_lowercase+string.ascii_uppercase+"1234567890"+"!@·$%&/()=?¿"



for j in range(numero):
    contraseña = ""
    for i in range(longitud):
        contraseña = contraseña+random.choice(caracteres)
    print(contraseña) 

# porque el print va a ese nivel de identación? 

# el primer for va a a empezar un ciclo, por cada
# contraseña pedida, asi que lo hará numero veces.
# el for anidado hará las contraseñas como tal
# por eso en el es que está el print, cada que se hace una
# contraseña imprime y empieza de nuevo el for principal
# con la contraseña vacia lista para ser llenada aleatoriamente.      

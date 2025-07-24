import random
import time

# M.A.S.H significa mansion_apartamento_choza_casa



# Version 1. Listas de posibles resultados por defecto

# listas y variables principales, van dentro de la funcion
# maestra despues de la primera indentacion y antes del ciclo.

homes = ['Mansion', 'Apartment', 'Shack', 'House', 'Street']  # 5 elementos
cars = ['Lamborghini', 'Toyota', 'Bicycle', 'Motorcycle']   # 4 elementos
careers = ['Doctor', 'Engineer', 'Artist', 'Unemployed']    # 4 elementos
loves = ['Alex', 'Jamie', 'Pat', 'Sam'] # 4 elementos

lista_destino1 = [homes, cars, careers, loves]
lista_destino2 = ["homes", "cars", "careers", "loves"]
lista_general = homes + cars + careers + loves
random.shuffle(lista_general)



# Como se va a modular entonces, las funciones quedaran 
# dependientes de varios parámetros, casi nunca sin argumento.

# 1. una bienvenida que puede venir dentro de el archivo maestro,
# o en la funcion maestra

# print("*************** Bienvenido al juego ***********************************  ")
# print("Sabrás con quien te casaras, donde viviras y que carrera y carro tendrás ")
# print("******************* Mucha suerte ****************************************")


# 2. una funcion que crea los mensajes del inicio de cada ronda,
# ronda = 1 viene dentro del archivo maestro o funcion maestra.

def rondas(ronda):
        print(f"Listo vamos con la ronda {ronda} !!!")
        jugada = int(input(f"Dame un numero entre 0 y {len(lista_general)}  "))
        return jugada

# 3. Una funcion que tome la elección del usuario  (jugada)
# y con ella elimine una de las opciones, ademas le diga al 
# usuario lo que ha desaparecido de su destino y las opciones
# que le quedan de cada cosa.

# como lista destino tiene 4 elementos, cada vez podemos elegir al azar 
# uno de los 4 y eliminar de ahi uno?

    
def elegir(jugada, lista_general): 
    
    print(f"Haz escogido el numero {jugada}, veamos que haz eliminado de tu destino:  ")
    time.sleep(1.2)
    
    for i in range(jugada-1):
        print(lista_general[i])
        time.sleep(1.2)
    
    eleccion =  lista_general[jugada] 
    print(eleccion) 
    print(f" Haz decidido eliminar la opción {eleccion}")
    
    return eleccion   

def eliminacion_y_estado_del_juego(eleccion):

    if eleccion in homes and len(homes) > 1:
        homes.remove(eleccion)
        lista_general.remove(eleccion)
        mensaje_de_eliminacion = f""" No podrás vivir en un/una {eleccion},
        No te preocupes, todavia puedes vivir en un/una {homes}"""
    elif eleccion in cars and len(cars) > 1:
        cars.remove(eleccion)
        lista_general.remove(eleccion)
        mensaje_de_eliminacion = f""" No podrás conducir en un/una {eleccion},
        No te preocupes, todavia conducir {cars}"""
    elif eleccion in careers and len(careers) > 1:
        careers.remove(eleccion)
        lista_general.remove(eleccion)
        mensaje_de_eliminacion = f""" No podrás trabajar como {eleccion}
        No te preocupes, todavia puedes trabajar como {careers}"""   
    elif eleccion in loves and len(loves) > 1:
        loves.remove(eleccion)
        lista_general.remove(eleccion)
        mensaje_de_eliminacion = f""" No podrás casarte con {eleccion}
        No te preocupes, todavia puedes casarte con {loves}"""
           
    return mensaje_de_eliminacion

# y finalmente la función mash_game, hará uso de las 3 anteriores
# con un código sencillo   


homes = ['Mansion', 'Apartment', 'Shack', 'House', 'Street']  # 5 elementos
cars = ['Lamborghini', 'Toyota', 'Bicycle', 'Motorcycle']   # 4 elementos
careers = ['Doctor', 'Engineer', 'Artist', 'Unemployed']    # 4 elementos
loves = ['Alex', 'Jamie', 'Pat', 'Sam'] # 4 elementos
lista_general = homes + cars + careers + loves
random.shuffle(lista_general)

lista_destino1 = [homes, cars, careers, loves]
lista_destino2 = ["homes", "cars", "careers", "loves"]




def mash_game():
    
    # Mensaje de Bienvenida :)
    
    print("*************** Bienvenido al juego **************************************** ")
    print("Sabrás con quien te casaras, donde viviras y que carrera y carro tendrás *** ")
    print("******************* Mucha suerte :) **************************************** ")
    
    # variables iniciales de las funciones internas:
    
    
    ronda = 1
    
    # ciclo para las rondas, la eleccion de la jugada, lo que se
    # elimina y como queda las opciones
    
    
    while len(lista_general) > 4:
        jugada = rondas(ronda)
        eleccion = elegir(jugada, lista_general)
        
        try :
            mensaje_de_eliminacion = eliminacion_y_estado_del_juego(eleccion)
            print(mensaje_de_eliminacion)
        except UnboundLocalError:
            continue
        
        random.shuffle(lista_general)
        
        # reiniciar las funciones
        ronda += 1
        print(homes)
        print(cars)
        print(careers)
        print(loves)
        print(lista_general)
        
        
    print(" Ha acabado el juego, sabemos lo que pasará con tu futuro: ")
    time.sleep(1)
    print (" ")
    
    
    print(f" Viviras en un/una {homes[0]} ") 
    print (" ")
    time.sleep(1)
     
    print(f" Conduciras un {cars[0]} ")  
    print (" ")
    time.sleep(1)  
        
    print(f" Trabajaras como {careers[0]} ") 
    print (" ")
    time.sleep(1)     
     
    print(f" Y te casaras con ......") 
    print(" ")
    time.sleep(3)
    
    print(f" {loves[0]} !!!")
      
      

            
mash_game()




# Version 2. Si fuera interactivo seria pedirle al usuario las opciones
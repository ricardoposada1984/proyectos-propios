
# Vamos a usar POO
# Para modelar las principales caracteristicas
# de una caminata aleatoria
# mediante las clases Borracho y borracho tradicional

import random

class Borracho():
    def __init__(self, nombre):
        self.nombre = nombre
    # Simplemente, le da nombre al borracho si se quiere.
class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)
    # hereda las propiedades de Borracho
    # en este caso simplemente tener nombre
    # y le agrega otras funcionalidades 
    # como las siguientes:
    def camina():
        return random.choice((1, 0), (0, 1), (-1, 0), (0, -1))
    # como devuelve coordenadas, esta funcion es la que
    # permite unir las anteriores clases con las siguientes:

class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Asigna una cooredenada x,y:
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
        # mover transforma una coordenada en otra
        # moviendo cada uno de sus componentes
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x 
        delta_y = self.y - otra_coordenada.y 
        # calcula la distancia euclidiana entre dos puntos asi: 
        return (delta_x**2 + delta_y**2)**0.5

class Campo():

    def __init__(self):
        self.coordenadas_de_borracho = {}

    def añadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borracho[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borracho[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):    
        return self.coordenadas_de_borracho[borracho]

           
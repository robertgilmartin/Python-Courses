# Declaración de la clase
# class Pajaro:
#     pass
#
# # mi_pajaro es una instancia de la clase Pajaro
# mi_pajaro = Pajaro()
# otro_pajaro = Pajaro()
# print(type(mi_pajaro))
# print(mi_pajaro)
# print(otro_pajaro)

# Atributos son los parámatros que se añaden a las clases para definirlas
# Atributos de instancia, quiere decir que cada vez que instancies
# un objeto de esta clase podrá tener un atributo distinto.

# Los atributos de clase son iguales para todos los objetes que crees.
class Pajaro:
    #Atributo de clase
    alas = True

    # Constructor de la clase  Pajaro se define como una función (__init__).
    # En este caso hemos agregado un atributo de color. Que será
    # obligatorio a la hora de instanciar un objeto.
    # Color en los paréntesis es el argumento de la función constructora,
    # y el self.color es el atributo de la clase
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('negro', 'Tucán')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)
print(mi_pajaro.alas)

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
casa_blanca = Casa('blanco', 4)

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color
cubo_rojo = Cubo('rojo')

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje("Humano", True, 17)
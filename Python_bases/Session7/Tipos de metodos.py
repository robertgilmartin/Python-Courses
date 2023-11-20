# 1- Métodos de instancia: son los que se declaran con 'def' y self como argumento.
# 2- Métodos de clase: Se declaran igual pero poniendo @classmethod antes. Diferencia se puede llamar no
# solo desde la instancia sino desde la clase misma. No pueden acceder a métodos de instancia pero si
# métodos de clase.
# 3- Métodos de estáticos: No pueden aceptar ni atributos de clase ni de instancia, pero si parámetros de entrada.
# Hay que poner @staticmethod.

class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    # Método de instancia. Cambiar atributos de instancia.
    # Tambien puede llamar a métodos.
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros.")
        self.piar()


    # Método de instancia. Cambiar atributos de instancia.
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pájaro es {self.color}")

    # Método de clase. Pone 'cls' del tiron en vez de 'self'.
    # Este accede a la clase en si misma.
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos.")
        # print(f"Es de color{self.color}") --> Sale error no puedes acceder
        # Pero si se puede accedera atributos de clase como 'alas'
        cls.alas = False
        print(Pajaro.alas)

    # Método estático
    @staticmethod
    def mirar():
        #self.color = 'rojo' --> no se puede acceder a atr de instancia
        #cls.alas = False --> no se puede acceder a atr de clase
        # Justo sirve para eso, para asegurarte de que estos métodos
        # no acceden a esos atributos
        print("El pajaro mira")

piolin = Pajaro('amarillo', 'canario')
piolin.pintar_negro()
piolin.alas = False
print(piolin.alas)

# La diferencia es que este metodo lo podemos llamar sin necesidad
# de hacer una instancia. De hecho los métodos de instancia no se pueden
# llamar si no es a partir de una instancia de esa clase.
Pajaro.poner_huevos(8)

# El método estático se puede llamar del tiri también
Pajaro.mirar()

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1


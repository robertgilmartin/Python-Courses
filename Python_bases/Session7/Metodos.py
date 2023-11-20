# Siempre que quieras usar los atributos de la clase en los métodos debes poner self delante siempre.
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros.")

piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(17)

class Perro:
    def ladrar(self):
        print('Guau!')
dog = Perro()
dog.ladrar()

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
merlin = Mago()
merlin.lanzar_hechizo()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


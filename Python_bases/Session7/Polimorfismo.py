# Polimorfismo, es el uso de mismos métodos para distintos objetos

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beeee")


vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

# vaca1.hablar()
# oveja1.hablar()

# En este ejemplo se ve algo mejor el polimorfismo, vemos que en el loop for llamamos la función animal.hablar()
# y el resultado es distinto para cada animal como era de esperar. Pero en este caso es más difícil de visualizar
# Pero si sabes de que objeto se trata cada animal de la lista, entonces ya le ves el sentido.

animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()

# Vamos a verlo por una función. Como argumento pasamos un objeto y llamamos la función hablar.
# El polimorfismo permite ejecutar esa función respectiva de cada objeto

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

# Ejercicios

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


for element in palabra, lista, tupla:
    print(len(element))

###################################################

class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")



mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()
character_list = [arquero1, mago1, samurai1]


for character in character_list:
    character.atacar()


class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()


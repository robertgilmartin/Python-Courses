# Se usa para heredar atributos y metodos de otro clase
# E.g. tenemos dos clases "Animal" y "Pajaro". Queremos que Pajaro hereder los elementos de la clase
# Animal. Lo podemos heredar de esta manera --> class Pajaro(Animal):

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    
    # Aqui se repiten dos atributos que Animal ya tiene como edad y color 
    # por lo que vamos a usar el __super__ para usar los atributos de Animal
    def __init__(self, edad, color, altura_vuelo):
        # self.edad = edad
        # self.color = color
        super().__init__(edad, color) # --> Se asigna las heredadas así y solo añadiremos las nuevas
        self.altura_vuelo = altura_vuelo
    

    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f"El pájaro vuela {metros}")

# Los metodos __bases__ te dice el parent de esa clase
# El metodo __subclasses__ te dice que clases heredan de esa
print(Pajaro.__bases__)
print(Animal.__subclasses__())

# Usando métodos de mi objeto que proviene de la clase heredada
mi_pajaro = Pajaro(2, 'amarillo', 60)
mi_pajaro.nacer()
print(mi_pajaro.color)
print(mi_pajaro.edad)


# Ejercicios
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass


class Mascota:
    def __init__(self, nombre, edad, cantidad_patas):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass


class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass


# Herencia extendida (super) y múltiple(Class1, Class2 --> El orden importa)
# El objeto de mi_animal solo verá los atributos y métodos de la clase Animal, pero que pasa
# si queremos usar los atributos de Animal como (edad y color) en nuestra clase pájaro sin tener que
# declarlas otra vez? Pues se usa el término '__super__'
piolin = Pajaro(3, 'amarillo', 60)
mi_animal = Animal(5, 'negro')
piolin.nacer()

# Que pasa si hay dos métodos que se escriben iguales tanto en el método de la clase como
# la clase que hereda (Animal)? Pues lo que hace que es ejecutar el método de la clase
piolin.hablar()

piolin.volar(100)


class Padre:
    def hablar(self):
        print('Hola')


class Madre:
    def reir(self):
        print("jajajaja")

    def hablar(self):
        print('que tal')


# Hijo tiene una herencia múltiple en este caso Padre y Madre
class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.reir()

# Que pasa si Padre y Madre tienen el mismo método con el mismo nombre?
# Que método llamará Nieto cuando se ejecute el método hablar
# Pues va a decir 'Hola' el método del padre, porque primero hereda de Padre y luego de Madre
# según el orden que pongamos la Herencia.
mi_nieto.hablar()

# Para ver el orden de prioridad puedes hacerlo a partir del método __mro__
print(Nieto.__mro__)


# Ejercicios
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre, Padre):
    pass

mi_hija = Hija()
print(mi_hija.trabajar())


class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    def __init__(self, tiene_pico, vertebrado, venenoso):
        super().__init__(tiene_pico, vertebrado, venenoso)


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    # No hace falta porque son de clase los atributos de Padre no son atributos de instancia
    # def __init__(self, color_ojos, tipo_pelo, altura, voz, deporte_preferido):
    #     super().__init__(color_ojos, tipo_pelo, altura, voz, deporte_preferido)

    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"


















#Generar números aleatorios. Importaremos una libreria
# from random import randint ## Si pones * al importar, importas toda la libreria
from random import *

#Int
aleatorio = randint(0, 100)

print(aleatorio)

#Float
aleatorio = uniform(0, 50)

print(aleatorio)

#Round with 3 decimals
aleatorio = round(uniform(0, 50), 3)

print(aleatorio)

#Between 0 and 1
aleatorio = random()

print(aleatorio)

#Escoger

colores = ['azul', 'rojo', 'verde', 'amarillo']

aleatorio = choice(colores)

print(aleatorio)

# Mezclar numeros
numeros = list(range(5, 50, 5))

shuffle(numeros)

print(numeros)


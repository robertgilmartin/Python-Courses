# Básicamente lo que hacen los generadores, es producir lo que requerimos a medida de lo que vamos
# necesitando. Se usa para tener una mayor eficiencia de nuestra capacidad de memoria.

def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion())
print(mi_generador()) # --> aun no lo ha generado
g = mi_generador()
print(next(g)) # --> con next() si podemos acceder a ese valor
# si tuviesemos una lista con la funcion next nos iria dando ese numero cada vez que lo necesitemos


def mi_funcion2():
    lista =  []
    for x in range(1, 6):
        lista.append(x)
    return lista


# Como puedes ver, al usar generadores tambien ahorramos en lineas de código
def mi_generador2():
    for x in range(1, 6):
        yield x * 10


print(mi_funcion2())
g = mi_generador2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # --> Si nos pasamos nos da error de StopIteration


def mi_generador3():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador3()

print(next(g))
print(next(g))
# Aqui podemos hacer lo que queramos, las funciones que vayan aqui no interrumpen el generador
print("Hola Mundo")
print(next(g))

# Ejercicios


def mi_generador4():
    x = 0
    while True:
        x += 1
        yield x

g = mi_generador4()

print(next(g))
print(next(g))

def mi_generador5():
    x = 0
    while True:
        x += 1
        yield x * 7


generador = mi_generador5()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

def mi_generador6():
    lista = ["Te quedan 3 vidas", "Te quedan 2 vidas", "Te queda 1 vida", "Game Over"]
    for l in lista:
        yield l


perder_vida = mi_generador6()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

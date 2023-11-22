# Los decoradores son funciones que modifican el comportamiento de otras funciones
# A dia de hoy ya hemos visto 2 tipos de decoradores: @classmethod y @staticmethod

# Ejemplo: en este caso queremos enviar 'Hola' un texto y 'Adios' al final por lo que tenemos 2 opciones
# O poner prints de 'Hola' y 'Adios' al principio y final del texto o poner esos prints dentro de ambas
# funciones. Pero ambas opciones son poco eficientes.
# Opcion 1:

# print('hola')
# mayuscula('Hoy es Martes')
# print('Adios')

def mayuscula(texto):
    # Opcion 2:
    # print('hola')
    print(texto.upper())
    # print('Adios')

def minuscula(texto):
    # Opcion 2:
    # print('hola')
    print(texto.lower())
    # print('Adios')


def una_funcion(funcion):
    return funcion


def cambiar_letras(tipo):
    def mayuscula(texto):
        # Opcion 2:
        # print('hola')
        print(texto.upper())
        # print('Adios')

    def minuscula(texto):
        # Opcion 2:
        # print('hola')
        print(texto.lower())
        # print('Adios')

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula



# Veamos la logica de los decoradores. En python tod0 son objetos, una función es un objeto.
# Como se asigna a una variable una funcion como objeto. Es como instanciar una variable a partir de una funcion
# sin parentesis!!


mi_funcion = mayuscula

mi_funcion("python")

# Otro ejemplo para ver que las funciones pueden ser objeto, y por ende, pueden ser un argumento de otra
# función, es creando una funcion que tenga otra funcion como argumento.

una_funcion(mayuscula("probando"))

# Ahora creamos una función que contiene dos funciones y retorna un objeto de función u otra (linea30)

operacion = cambiar_letras('may') # operacion es una variable de tipo funcion mayuscula
operacion('palabra') # Podemos ejecutar esto asi directamente


# Ahora ya podemos definir un decorador

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')

    return otra_funcion

# Si queremos decorar nuestras funciones con nuestro decorador xd, ponemos el @ delante y listo
# De esta manera siempre estará decorada. Pero si queremos decorarla a veces hay que hacerlo de otra manera,
# que vemos en la linea 97.

@decorar_saludo
def mayusculass(texto):
    print(texto.upper())

# @decorar_saludo
def minusculas(texto):
    print(texto.lower())


minusculas("Python")
mayusculass("python")

# El tema es que puede que no querramos ejecutar siempre nuestro decorador, es decir tener como un Switch
# Para ello hacemos eliminamos el @decorar_saludo del principio de ambas funciones y creamos una variable
# decorada de esta manera.

mayuscula_decorada = decorar_saludo(mayuscula)
mayusculass('robert')
mayuscula_decorada('Robert')

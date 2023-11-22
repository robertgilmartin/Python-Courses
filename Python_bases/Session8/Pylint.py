# Biblioteca que analiza tu codigo y deduce possibles problemas
# Desde el terminal ejecutamos la siguiente consigna --> pytlint file.py -r y --> -r: reported y:yes
# Ejemplo de error:
# numero1 = 500
# print(Numero1)

# Tipo de errores
# C items --> Problemas de estilo, se ejecuta igual el codigo
# E items --> errores de verdad.
# Al final te da un ratio de puntuacion que debería de estar de 7/10 para arriba.
# Te dice lo que seria guai que tuviese como los docstrings, comentarios, etc.
# Tambien recomienda que tod0 esté dentro de funciones y no haya codigo suelto


# Ejemplo de buenas prácticas
"""
Esto es un modulo que imprime algo
"""


def one_function():
    '''
    Esta funcion imprime un numero
    :return: none
    '''

    number = 600
    print(number)


one_function()

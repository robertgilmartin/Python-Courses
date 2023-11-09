# Si usamos *args podemos llamar a la función con el número de variables que querramos.
# Dato: no hace falta que se llame *args si no con solo poner el '*' delante de una palabra es suficiente.
# args es una tupla
def suma(a,b):
    return a+b

print(suma(5,6))
# print(suma(5, 6, 7))

def suma_con_args(*args):
    total = 0
    # return sum(args) --> esto funciona tambien
    for arg in args:
        total += abs(arg)
    return total

print(suma_con_args(5, 6, 7, 8))
# from random import shuffle
from random import randint
# # Lista incial
# palitos = ['-', '--', '---', '----']
#
# #Mezclar palitos
# def mezclar(lista):
#     shuffle(lista)
#     return lista
#
# # Pedir un intento
# def probar_suerte():
#     intento = ''
#
#     while intento not in ['1', '2', '3', '4']:
#         intento = input("Elige un numero del 1 al 4: ")
#     return int(intento)
#
# # Comprobar el intento
# def check_intento(lista, intento):
#     if lista[intento -1] == '-':
#         print("A lavar los platos!!!")
#     else:
#         print("Esta vez te has salvado")
#     print(f"Te ha tocado {lista[intento - 1]}")
#
# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# check_intento(palitos_mezclados, seleccion)

def lanzar_dados():
    return (randint(1, 6), randint(1, 6))


def evaluar_jugada(n1, n2):
    suma_dados = n1 + n2

    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados in range(7, 10):
        return (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    if suma_dados > 10:
        return (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

num1, num2 = lanzar_dados()
print(num1, num2)
print(evaluar_jugada(num1, num2))

lista_numeros = [9, 6, 8, 4, 5, 7, 6]

def reducir_list(lista):
    mi_set = set(lista)
    new_list = list(mi_set)
    new_list.pop(-1)
    return new_list

def promedio(lista):
    resultado = 0
    for i in lista:
        resultado += i
    return resultado/len(lista)

lista_reducida = reducir_list(lista_numeros)
r = promedio(lista_reducida)


def lanzar_moneda():
    if randint(0, 1) == 0:
        return "Cara"
    else:
        return "Cruz"

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista


moneda = lanzar_moneda()
suerte = probar_suerte(moneda, lista_numeros)

print(suerte)
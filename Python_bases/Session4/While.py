# monedas = 5
#
# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     monedas -= 1
# else:
#     print("No tengo más dinero")
#
# respuesta = 's'
#
# while respuesta == 's':
#     respuesta = input("Quieres seguir? (s/n)")
# else:
#     print("Gracias")
#
# # Pass --> Passar del while i poder ejecutar mi codigo sin errores. Para rellenear luego.
# while respuesta == 's':
#     pass
# # Break --> Salir del while
# nombre = input("Tu nombre: ")
#
# for letra in nombre:
#     if letra == 't':
#         break # Para el loop
#     elif letra == 'e':
#         continue # saltará la letra per seguirá ejecutando el resto del loop
#     print(letra)

# numero = 10
# lista = []
# while numero >= 0:
#     lista.append(numero)
#     numero -= 1
# print(lista)

numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(f"Este numero es divisible por 5: {numero}")
        numero -= 1
    else:
        numero -= 1


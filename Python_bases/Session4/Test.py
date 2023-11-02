from random import *

nombre_jugador = input("Como te llamas? ")
print(f"Bueno, {nombre_jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
numero_secreto = randint(1, 101)
intentos = 1

while intentos < 9:

    valor_elegido_usuario = int(input(f"Intento número {intentos}. Elige un valor: "))

    if valor_elegido_usuario < 1 or valor_elegido_usuario > 100: ### Aqui se podria haber hecho tambien ""if valor_elegido_usuario not in range(1,101):""
        print(f"{valor_elegido_usuario} no está permitido.")
        intentos += 1
    elif valor_elegido_usuario < numero_secreto:
        print(f"{valor_elegido_usuario} es INCORRECTO! {valor_elegido_usuario} es menor al valor que tengo en mente.")
        intentos += 1
    elif valor_elegido_usuario > numero_secreto:
        print(f"{valor_elegido_usuario} es INCORRECTO! {valor_elegido_usuario} es mayor al valor que tengo en mente.")
        intentos += 1
    else:
        print(f"ENHORABUENA!!! Has acertado!!  Los has logrado en {intentos} intentos!!")
        break

if intentos == 9:
    print("Se han acabado los intentos :(. Vuelve a intentarlo otra vez")
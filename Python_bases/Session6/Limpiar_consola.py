from os import system

# clear console system('cls')

nombre = input("dime tu nombre: ")
edad = input("dime tu edad: ")
# Queremos hacer un clear de la consola y solo ver el resultado
system('cls')
print(f"Tu nombre es {nombre} y tienes {edad} años.")

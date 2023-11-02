palabra = 'Python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Eficiencia

lista = [letra for letra in palabra]

print(lista)

lista = [n for n in range(0,100,2)]

print(lista)

lista = [n / 2 for n in range(0,21,2)]

print(lista)

lista = [n for n in range(0,100,2) if n * 2 > 10]

print(lista)

lista = [n if n * 2 > 10 else 'no' for n in range(0,100,2)]

print(lista)

## En Resumen, el costo es menor pero es menos legible

#Pasar de pies a metros
pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]

print(metros)


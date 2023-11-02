# For
lista = ['a', 'b', 'c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

# Refactor -> cambiar nombre de iterador en todas las lineas

personas = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in personas:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza por L: ' + nombre)

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(f"Mi valor es: {mi_valor}")

# List iterations
lista_de_listas = [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]

for a, b in lista_de_listas:
    print(a + " " + b)

# Dic iterations
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for key, value in dic.items():
    print(key + " " + value)
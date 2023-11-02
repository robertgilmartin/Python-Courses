lista = ['a', 'b', 'c', 'd']
# indice = 0
#
# for item in lista:
#     print(indice, item)
#     indice += 1

# Substitute
#Return tuple
for item in enumerate(lista):
    print(item)
# Return values
for indice, item in enumerate(lista):
    print(indice, item)

for indice, item in enumerate(range(50, 55)):
    print(indice, item)

##########################################################
#Lista de tuplas con sus indices
mis_tuple = list(enumerate(lista))
print(mis_tuple)
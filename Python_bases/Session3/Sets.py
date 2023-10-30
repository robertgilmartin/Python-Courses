# Solo permite un solo argumento. Elimina los elementos duplicados
# No admite ni listas ni diccionaios pero tuplas si

mi_set = set([1,2,3,4,5, (1,4), (1,4), 20.0])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(otro_set)
print(type(otro_set))

print(len(mi_set))

print(2 in mi_set)

#===========================================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)

print(s3)

print(s1.add(5))
print(s1.discard(2))
print(s1.pop()) # Si no añades ningun argmento, popeo un número aleatorio.

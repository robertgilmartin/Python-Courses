##Se usan para eficiencia y para usarse en listas que no queramos conmutar
mi_tuple = (1, 2, 3, 4)
mi_tuple2 = 1, 2, 3, 4
print(type(mi_tuple))
print(type(mi_tuple2))
print(mi_tuple[0])
mi_tuple3 = (1, 2, (10, 2), 5)
print(mi_tuple3)

mi_tuple = list(mi_tuple3)

t = 1, 2, 3, 1
x, y, z, a = t

print(x, y, z)
print(t.count(1))
print(t.index(2))


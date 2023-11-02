#Obtienes los valores más bajos y más altos de una colección
minimo = min(1,2,3,4,5,6)
maximo = max(1,2,3,4,5,6)
print(minimo)
print(maximo)

lista = [4,5,6,7,8]
print(max(lista))
print(f"El menor es {min(lista)}")
print(f"El mayor es {max(lista)}")

dic = {'C1': 45, 'C2': 65}
print(min(dic.values()))
print(min(dic))

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
nombre = max(diccionario_edades.keys())

print(edad_minima)
print(nombre)
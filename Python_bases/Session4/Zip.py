# Va muy bien para COMBINAR LISTAS
nombre = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]

#Tienes que castear siempre el zip como lista si no se ve la direccion de memoria
combinados = list(zip(nombre, edades))

print(combinados)

#Zip solo llega al largo de la lista más corta, las listas que querramos combinar deben tener el mismo lenght.
edades = [65, 29, 42, 55]

combinados = list(zip(nombre, edades))

print(combinados)

#Puedes combinar más de dos listas
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombre, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
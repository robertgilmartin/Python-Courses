# El archivo debe estar en la misma ruta dónde se encuentra el py

mi_archivo = open('prueba.txt')
print(mi_archivo)
print(mi_archivo.read())

# Se pueden usar todos los metodos de strings como "upper" por ejemplo
una_linea = mi_archivo.readline()
print(una_linea.upper())

# Aunque obreescribamos la una_linea con el mismo metodo de readline(), igualmente el programa
# imprimirá la siguiente línea respecta la que leyó anteriormente
una_linea = mi_archivo.readline()
print(una_linea)

# Imprimir una linea en concreto. Segunda línea en este caso
lineas = mi_archivo.readlines()
print(lineas[1])

# Se escribe al final un salto de linea que no se ve en el archivo. pero ahi está!
# Si no quieres la linea vacía entre medias se puede usar rstrip.
una_linea = mi_archivo.readline()
print(una_linea.rstrip())

# Se puede iterar en cada línea
for l in mi_archivo:
    print("aquí dice: " + l)

# También se puede hacer una lista con todas la líneas con el readlines()
todas = mi_archivo.readlines()
print(todas)

# Se pueden usar los métodos de listas
todas = todas.pop()
print(todas)

# Para guardar el espacio de memoria, hacer siempre un close()!!
mi_archivo.close()



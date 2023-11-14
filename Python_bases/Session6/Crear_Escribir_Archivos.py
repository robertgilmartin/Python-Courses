# Antes haciamos cambios a parti de la variable que asignabamos a la apertura del archivo
# Pero para hacer cambios al archivo de texto hay que hacerlo de la siguiente manera:

# Hay distintos modos, open('archivo.txt', modo de apertura)
# Modos de apertura:
# r: solo lectura
# w: solo escritura
# a: solo escritura posicionandose al final del archivo, para que puedas escribir
# a partir del final y conservar lo anterior

# Modo solo lectura: r
#
# archivo = open('prueba.txt', 'r')
# archivo.write('Soy el nuevo texto') # -> Salta error no se puede escribir en modo lectura, obviamente...

# Modo solo escritura: w
#
archivo = open('prueba.txt', 'w')

#Haciendo esto sobreescribirá tod0 el contenido del archivo. Cuidado con esto
# archivo.write('Soy el nuevo texto')

# Writelines, es para pasar una lista de strings para meter en el archivo, como readlines para leer.
# Es un poco confuso porque concatena los strings de la lista, no escribe cada elemento en una nueva linea
archivo.writelines(['hola', 'aqui', 'estoy\n'])

lista = ['hola', 'aqui', 'estoy']

# Así habría que hacerlo para cada linea
for p in lista:
    archivo.writelines(p + '\n')

# Modo solo escritura a final de linea: a
# archivo = open('prueba.txt', 'a')

archivo.close()


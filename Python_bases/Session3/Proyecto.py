##############################################################################################################
"""
Texto: La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información.
"""
##############################################################################################################

texto = input("Añade el texto aquí: ").lower()
letras = input("Añade tres letras aquí: ")

lista_letras = list(letras)
lista_palabras = texto.split()

# Part 1
rep_letra = texto.count(lista_letras[0])
rep_letra1 = texto.count(lista_letras[1])
rep_letra2 = texto.count(lista_letras[2])

print(rep_letra)
print(rep_letra1)
print(rep_letra2)

# Part 2
print(len(lista_palabras))

# Part 3
primera_letra_texto = texto[0]
ultima_letra_texto = texto[-1]

print(primera_letra_texto)
print(ultima_letra_texto)

# Part 4
lista_palabras.reverse()
texto_invertido = "".join(lista_palabras)

print(texto_invertido)

# Part 5
print("Python".lower() in texto.lower())

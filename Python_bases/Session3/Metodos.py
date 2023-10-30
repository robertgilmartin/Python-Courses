texto = "Este es el texto de Robert"

minusculas = texto.lower()
mayusculas = texto.upper()
separar = texto.split()
separar2 = texto.split("t")

print(minusculas)
print(mayusculas)
print(separar)
print(separar2)

# ==========================================

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
juntos = "-".join([a,b,c,d])
juntos2 = " ".join([a,b,c,d])

print(juntos)
print(juntos2)

# ==========================================

buscar = texto.find("texto")

print(buscar)

# ==========================================

reemplazar = texto.replace("Robert", "Andrea")
reemplazar2 = texto.replace("e", "x")

print(reemplazar)
print(reemplazar2)

# ==========================================

lista_palabras = ["La","legibilidad","cuenta."]

juntos = " ".join(lista_palabras)
print(juntos)


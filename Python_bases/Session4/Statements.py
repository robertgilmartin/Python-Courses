# if, elif, else

if 10 > 9:
    print("es correcto")

x = True

if x:
    print("es correcto")

if 5 == 2:
    print("es correcto")
else:
    print("no es correcto")

mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "conejo":
    print("Tienes un conejo")
else:
    print("No sé que animal tienes")

edad = 16
calificacion = 9

if edad < 18:
    print("Eres menor de edad")
    if calificacion > 7:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres adulto")


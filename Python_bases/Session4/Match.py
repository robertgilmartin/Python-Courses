# No existe swtich case, por lo que han hecho match
serie = "N-02"

match serie:
    case "N-01":
        print("Xiaomi")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorolla")
    case _:
        print("No existe ese producto")

cliente = {'nombre': "robert",
           "edad": 30,
           "profesion": "cocinero"}
pelicula = {"titulo": "Star Wars",
            "Ficha_tecnica": {"protagonista": "Ewan McGregor",
                              "Director": "George Lucas"}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "profesion": profesion}:
            print("Es un cliente")
            print(nombre, edad, profesion)
        case {"titulo": titulo,
              "Ficha_tecnica": {"protagonista": protagonista,
                                "Director": director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")
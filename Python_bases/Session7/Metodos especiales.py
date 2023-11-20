# Son esos métodos que son están entre __metodo__ guiones bajos.
# Ejemplos: __init__, __bases__, __mro__, __subclasses__

mi_lista = [1,1,1,1,1]

print(len(mi_lista))

class Objeto:
    pass

# Por ejemplo el len no es aplicable en classes que tu has creado, solo en esasa que son intrinsecas de pyton
# Como es en el caso anterior, las Listas.
mi_objeto = Objeto()
# print(len(mi_objeto)) --> Doesn't work


class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # Esta función especial nos permite que nos devuelva un string cuando llamemos la función print de
    # nuestro objeto fuera de la función. Si está función no estuvise, nos devolvería la direccion de memoria
    # donde se encuentra ese objeto, como siempre hemos visto.
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}."

    # Tambien podemos hacerlo para la funcion de len()
    def __len__(self):
        return self.canciones

    # Cuando se elimine una instancia nos diga QUE ha eliminado
    def __del__(self):
        print("Se ha eliminado el cd")

mi_CD = CD('Pink Floyd', 'The Wall', 24)
print(mi_CD)
print(len(mi_CD))

# Existe una función 'del' que sirve para eliminar instancias


del mi_CD
# print(mi_CD) --> Da error. Mejor usar el metodo especial __del__

# Ejercicios

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f"\"{self.titulo}\", de {self.autor}"

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        print("\"Libro eliminado\", mostrándolo en pantalla ")
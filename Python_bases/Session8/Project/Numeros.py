# Decorador: le pasamos como argumento un objeto-funcion que dentro de esta habrá otra_funcion con el argumento
# que nuestro objeto necesite
def decorar_turno(funcion):
    def otra_funcion(seccion):
        print("Su turno es:")
        funcion(seccion)
        print("Aguarde a la espera.")
    return otra_funcion


# Generador
def generador(seccion):
    x = 0
    y = 0
    z = 0
    while True:
        if seccion == 'C':
            x += 1
            yield f"C-{x}"
        elif seccion == 'F':
            y += 1
            yield f"F-{y}"
        elif seccion == 'P':
            z += 1
            yield f"P-{z}"

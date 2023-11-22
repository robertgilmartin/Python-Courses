# Import de los Generadores y Decorador de Numeros
import Numeros


# Función Escoger Sección
def escoger_seccion():
    secciones_permitidas = ['C', 'F', 'P', 'S']
    while True:
        seccion = input("Escoja una opción:\nCosmética (C) - Farmacia (F) - Perfumería (P) - Salir (S)\nSelección: ")
        if seccion not in secciones_permitidas:
            print("Esa sección es incorrecta, por favor no me toque las pelotas.")
        else:
            return seccion


# Esta es la función con el decorador
@Numeros.decorar_turno
def crear_tiquet(generador):
    print(next(generador))


def inicio():
    print("Bienvenido a la mejor tienda del mundo!")
    generador_cosmetico = Numeros.generador('C')
    generador_farmacia = Numeros.generador('F')
    generador_perfumeria = Numeros.generador('P')
    while True:
        eleccion = escoger_seccion()
        match eleccion:
            case 'C':
                crear_tiquet(generador_cosmetico)
            case 'F':
                crear_tiquet(generador_farmacia)
            case 'P':
                crear_tiquet(generador_perfumeria)
            case 'S':
                print("Vuelva pronto!")
                break


inicio()


# Notas: La liada que he tingut en aquest problema es que declarava de nou tot el rato el generador,
# el generador l'has d'iniciar un cop!! I després anar fent next() sobre el mateix generador creat abans.
# Si anem creant el generador tot el rato, el generador reiniciarà el contador també.

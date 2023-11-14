def abrir_leer(arch):
    return open(arch, "r").read()

texto = abrir_leer("Prueba.txt")
print(texto)

def sobrescribir(arc):
    file = open(arc, 'w').write("contenido eliminado")

def registro_error(arc):
    file = open(arc, 'a').write("se ha registrado un error de ejecución")
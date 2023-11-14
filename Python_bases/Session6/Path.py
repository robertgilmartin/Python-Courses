from pathlib import Path

# Path puede crear una ruta de acceso a partir de una tupla de strings
mi_ruta = Path('Europa', 'España', 'Catalunya', 'Lleida', 'Tremp.txt')
print(mi_ruta)

guia = Path('Barcelona', 'Sagrada_Familia')
print(guia)

# Devuelve una ruta absoluta al directorio principal
base = Path.home()
print(base)

guia_final = Path(base, mi_ruta)
print(guia_final)

# copiar la ruta anterior pero con un archivo distinto
guia2 = guia_final.with_name("La_Pedrera.txt")
print(guia2)

# Parent es un atributo de path el cual va dando el nivel más alto si vas concatenando el atributo
print(guia.parent)
print(guia.parent.parent)

# NEW: Get all the txt from global path

guiaa = Path(Path.home(), 'Europa')
# Metodo glob: si pones solo '*' incluirá solo los archivo txt que están en ese path.
# Pero si añadimos '**/*.txt' incluirá T0DO lo que haya dentro de esa carpeta en todos los niveles
for txt in Path(guiaa).glob("*.txt"):
    print(txt)

for txt in Path(guiaa).glob("**/*.txt"):
    print(txt)

# NEW: Paths relativos

guiaaa = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guiaaa.relative_to(Path("Europa"))
en_espania = guiaaa.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_espania)

ruta_base = Path.home()
ruta = Path("Curso Python", "Día 6", "practica_path.py")
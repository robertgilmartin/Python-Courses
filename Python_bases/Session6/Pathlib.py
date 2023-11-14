from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/robermood/OneDrive/Escritorio/QA_UDEMY/PYTHON/Python_bases/Python_bases/Session6/Data/prueba.txt")
print(carpeta.read_text())
# nombre del archivo, no lleva parentesis porque es un atributo de la clase Path
print(carpeta.name)
# sufijo del archivo, formato del archivo, no lleva parentesis porque es un atributo de la clase Path
print(carpeta.suffix)
# nombre del archivo sin sufijo, no lleva parentesis porque es un atributo de la clase Path
print(carpeta.stem)

# Como averiguar si un archivo existe en un path o no
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe!")

# Pure windows path, transforma cualquier ruta de que tengas a ruta de windows con los '\'
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
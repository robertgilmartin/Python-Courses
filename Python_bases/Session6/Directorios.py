# importamos la libreria de sistema operativo
import os
from pathlib import Path

# Windows '\' para el path pero duplido '\\'
# Get current word directory
ruta = os.getcwd()

print(ruta)
# Change directory
ruta = os.chdir("C:\\Users\\robermood\\OneDrive\\Escritorio\\QA_UDEMY\\PYTHON\\Python_bases\\Python_bases\\Session6\\Data")
archivo = open('Prueba.txt')
print(archivo.read())

# Crear un directorio nuevo
ruta = os.mkdir("C:\\Users\\robermood\\OneDrive\\Escritorio\\QA_UDEMY\\PYTHON\\Python_bases\\Python_bases\\Session6\\Data\\Otra")

#Conseguir nombre de un archivo en un directorio
ruta2 = "C:\\Users\\robermood\\OneDrive\\Escritorio\\QA_UDEMY\\PYTHON\\Python_bases\\Python_bases\\Session6\\Data\\prueba.txt"
elemento = os.path.basename(ruta2)
print(elemento)

# conseguir el directorio donde se encuentra el archivo prueba.txt
elemento = os.path.dirname(ruta2)
print(elemento)

# Split hace una tupla con dos strings, el path de la carpeta donde está el archivo y el archivo en qüestion.
elemento = os.path.split(ruta2)
print(elemento)

# Remove directory
os.rmdir("C:\\Users\\robermood\\OneDrive\\Escritorio\\QA_UDEMY\\PYTHON\\Python_bases\\Python_bases\\Session6\\Data\\Otra")

otro_archivo = open("C:\\Users\\robermood\\OneDrive\\Escritorio\\QA_UDEMY\\PYTHON\\Python_bases\\Python_bases\\Session6\\Data\\prueba.txt")
print(otro_archivo.read())

# Path es una clase de la libreria pathlib y las barras del directorio se ponen así '/'
carpeta = Path("C:/Users/robermood/OneDrive/Escritorio/QA_UDEMY/PYTHON/Python_bases/Python_bases/Session6/Data")
# Concatencación de path y archivo va con '/'
archivo2 = carpeta / 'prueba.txt'

mi_archivo = open(archivo2)
print(mi_archivo.read())
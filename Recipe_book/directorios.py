import os
from pathlib import Path

"""ruta = os.getcwd()
print(ruta)"""

"""ruta2 = os.chdir("C:\\Users\\Rafa García\\PycharmProjects\\Alternativo\\otro_archivo.txt")

archivo = open('otro_archivo.txt')
print(archivo)"""

"""ruta3 = os.makedirs("C:\\Users\\Rafa García\\PycharmProjects\\Alternativo\\Otra")"""

ruta4 = "C:\\Users\\Rafa García\\PycharmProjects\\Python\\Recipe_book\\Prueba.txt"
elemento = os.path.basename(ruta4)
elemento2 = os.path.dirname(ruta4)
elemento3 = os.path.split(ruta4)
print(elemento)
print(elemento2)
print(elemento3)

"""os.rmdir("C:\\Users\\Rafa García\\PycharmProjects\\Alternativo\\Otra")"""

# De esta manera, se puede abrir el archivo desde cualquier sistema operativo
carpeta = Path("/Users/Rafa García/PycharmProjects/Alternativo/Otra")
archivo = carpeta / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())

"""carpeta = Path("/Users/Rafa García/PycharmProjects/Alternativo/Otra") / "otro_archivo.txt
mi_archivo = open(carpeta)
print(mi_archivo.read())
"""
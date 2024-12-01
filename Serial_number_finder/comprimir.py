import zipfile

# Crear un archivo comprimido

mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")

mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")

mi_zip.close()

# Descomprimir un archivo

zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")

zip_abierto.extractall()

zip_abierto.close()

import shutil

# Comprimir un directorio

carpeta = 'C:/Users/Rafa García/PycharmProjects/Python/Serial_number_finder'

shutil.make_archive("mi_directorio_comprimido", "zip", carpeta)

# Descomprimir un directorio

shutil.unpack_archive("mi_directorio_comprimido.zip", "mi_directorio_descomprimido", "zip")

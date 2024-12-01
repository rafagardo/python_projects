import zipfile

archivo_zip = zipfile.ZipFile("Proyecto_Dia_9.zip", "r")
archivo_zip.extractall()
archivo_zip.close()
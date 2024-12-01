import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:/Users/Rafa García/PycharmProjects/Python/Serial_number_finder/Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpetas, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            resultado = buscar_numero(Path(carpetas, archivo), mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(archivo.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('Archivo \t\t\tNro. Serie')
    print('-------\t\t\t\t-----------')
    for archivo in archivos_encontrados:
        print(f'{archivo} \t\t\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Total de archivos encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()
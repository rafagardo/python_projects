from cv2 import cv2
import face_recognition as fr
import os
import numpy as np
from datetime import datetime

# Crear base de datos
ruta = 'Empleados'
empleados = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    empleados.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imagenes
def codificar_imagenes(imagenes):

    # Creacion de lista nueva
    lista_codificada = []

    # Codificacion de imagenes
    for imagen in imagenes:
        empleado = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(empleado)[0]
        lista_codificada.append(codificado)
    return lista_codificada

# Registrar los ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    lista_nombres = []
    for linea in lista_datos:
        entrada = linea.split(',')
        lista_nombres.append(entrada[0])

    if persona not in lista_nombres:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificados = codificar_imagenes(empleados)

# Tomar una imagen de camara web
camara = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Lectura de camara
exito, imagen = camara.read()

if not exito:
    print("No se ha podido acceder a la camara")
    exit()
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Comparar caras
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):

        comparacion = fr.compare_faces(lista_empleados_codificados, caracodif)
        distancia = fr.face_distance(lista_empleados_codificados, caracodif)

        # Indice de comparacion
        indice = np.argmin(distancia)

        # Mostrar coincidencia
        if distancia[indice] > 0.6:
            print("No se ha encontrado coincidencia")
        else:
            # Buscar nombre de empleado
            nombre_empleado = nombres_empleados[indice]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre_empleado, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            # Registrar ingreso
            registrar_ingresos(nombre_empleado)


            # Mostrar imagen de empleado
            cv2.imshow('Imagen web', imagen)

            # Mantener ventana abierta
            cv2.waitKey(0)
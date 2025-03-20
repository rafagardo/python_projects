from cv2 import cv2
import face_recognition as fr

# Carga de imagenes
foto_control = fr.load_image_file("FotoA.jpg")
foto_prueba = fr.load_image_file("FotoB.jpg")

# Conversion de imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
localizacion_control = fr.face_locations(foto_control)[0]

# Extraer caracteristicas de la cara control
caracteristicas_control = fr.face_encodings(foto_control)[0]

# Mostrar localizacion de la cara control
cv2.rectangle(foto_control, (localizacion_control[3], localizacion_control[0]), (localizacion_control[1], localizacion_control[2]), (0, 255, 0), 2)

# Localizar cara prueba
localizacion_prueba = fr.face_locations(foto_prueba)[0]

# Extraer caracteristicas de la cara prueba
caracteristicas_prueba = fr.face_encodings(foto_prueba)[0]

# Mostrar localizacion de la cara prueba
cv2.rectangle(foto_prueba, (localizacion_prueba[3], localizacion_prueba[0]), (localizacion_prueba[1], localizacion_prueba[2]), (0, 255, 0), 2)

# Mostrar comparacion de las caras
comparacion = fr.compare_faces([caracteristicas_control], caracteristicas_prueba)

# Medida de distancia
distancia = fr.face_distance([caracteristicas_control], caracteristicas_prueba)

# Mostrar resultado de la comparacion
cv2.putText(foto_prueba, f"{comparacion} {distancia.round(2)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Muestra de imagenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# Mantener las ventanas abiertas
cv2.waitKey(0)


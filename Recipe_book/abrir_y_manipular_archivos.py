mi_archivo = open('prueba.txt')

"""print(mi_archivo.read())"""

#-----------------------------------------

"""una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea)

#una_linea = mi_archivo.readline()
#print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea)"""

#----------------------------------------

""" for l in mi_archivo:
        print("Aqui dice: " + l)"""

#----------------------------------------

todas = mi_archivo.readlines() # Aplicar solamente a archivos pequeños
print(todas)

todas = todas.pop()
print(todas)

mi_archivo.close()
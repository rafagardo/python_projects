archivo = open("Prueba1.txt", 'w')

archivo.write("Soy el nuevo texto\n")
archivo.write("""Hola
Mundo
Aqui
Estoy
""")

archivo.writelines(['hola', 'mundo', 'aqui', 'estoy\n'])

lista = ['hola', 'mundo', 'aqui', 'estoy\n']
for p in lista:
    archivo.writelines(p + ' ')

#---------------------------------------------------------------

archivo = open("Prueba1.txt", 'a')

archivo.write('Bienvenido'.rstrip(' '))

archivo.close()
import os
# import shutil
# import send2trash

print(os.getcwd())  # C:\Users\Rafa García\PycharmProjects\Python\Serial_number_finder

archivo = open('curso.txt', 'w')
archivo.write('Esto es un curso de Python')
archivo.close()

print(os.listdir())

# shutil.move('curso.txt', 'C:/Users/Rafa García/PycharmProjects/Python/Serial_number_finder')
# shutil.rmtree('C:/Users/Rafa García/PycharmProjects/Python/Serial_number_finder/curso.txt') PELIGRO AL EJECUTAR ESTA LINEA

# send2trash.send2trash('curso.txt')
# send2trash es más seguro que shutil.rmtree porque envía el archivo a la papelera de reciclaje

# walk() devuelve un generador que recorre el árbol de directorios
for carpeta, subcarpetas, archivos in os.walk('C:/Users/Rafa García/PycharmProjects/Python/Serial_number_finder'):
    print(f'Estás en la carpeta: \t{carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpetas:
        print(f'\t{subcarpetas}')
    print('Los archivos son:')
    for arch in archivos:
        print(f'\t{archivos}')
    print('\n')



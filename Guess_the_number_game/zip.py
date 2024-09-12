nombres = ['Ana','Hugo','Valeria']
edades = [65,12,29]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')
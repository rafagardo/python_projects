from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio_1 = round(uniform(1,5), 1)
print(aleatorio_1)

aleatorio_2 = random()
print(aleatorio_2)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio_3 = choice(colores)
print(aleatorio_3)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
import time, timeit

# time.time() nos permite obtener la hora actual en segundos desde el 1 de enero de 1970.
# Por ejemplo, si queremos obtener la hora actual, podemos hacerlo de la siguiente manera:
# hora_actual = time.time()
# En este caso, hora_actual contendrá la hora actual en segundos desde el 1 de enero de 1970.
# Ejemplo:
# import time
# hora_actual = time.time()
# print(hora_actual)
# En este ejemplo, se obtiene la hora actual en segundos desde el 1 de enero de 1970 y se
# imprime en pantalla.
# Nota: time.time() es una función muy útil para obtener la hora actual en Python y
# realizar cálculos de tiempo.

def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(100000)
final = time.time()
print(final-inicio)

inicio = time.time()
prueba_while(100000)
final = time.time()
print(final-inicio)


# timeit es una herramienta que nos permite medir el tiempo de ejecución de un código
# en Python. Para usarla, debemos importarla y pasarle como argumentos el código que
# queremos medir y el número de veces que queremos que se ejecute. Por ejemplo, si
# queremos medir el tiempo de ejecución de una función llamada prueba_for que recibe
# un número como argumento y queremos que se ejecute 1000 veces, podemos hacerlo de
# la siguiente manera:
# timeit.timeit('prueba_for(100)', number=1000)
# En este caso, timeit devolverá el tiempo de ejecución de la función prueba_for(100)
# ejecutada 1000 veces.
# Ejemplo:
# import timeit
# def prueba_for(numero):
#     lista = []
#     for num in range(1,numero+1):
#         lista.append(num)
#     return lista
# tiempo = timeit.timeit('prueba_for(100)', number=1000)
# print(tiempo)
# En este ejemplo, se mide el tiempo de ejecución de la función prueba_for(100)
# ejecutada 1000 veces.
# Nota: timeit es una herramienta muy útil para medir el tiempo de ejecución de un
# código en Python y comparar diferentes implementaciones para ver cuál es más
# eficiente.

declaracion = """
prueba_for(10)
"""

mi_setup = """
def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista
"""

duracion = timeit.timeit(declaracion, setup=mi_setup, number=100000)
print(duracion)

declaracion2 = """
prueba_while(10)
"""

mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion2 = timeit.timeit(declaracion2, setup=mi_setup2, number=100000)
print(duracion2)



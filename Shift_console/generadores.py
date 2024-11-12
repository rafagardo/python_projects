"""
Los generadores son funciones que nos permiten generar una secuencia de valores sobre la marcha.
Esto significa que no necesitamos almacenar todos los valores en la memoria antes de devolverlos,
sino que podemos devolverlos uno a uno, haciendo uso de la palabra reservada yield.
"""


def mi_funcion():
    lista = []
    for i in range(1,5):
        lista.append(i*10)
    return lista

def mi_generador():
    for i in range(1,5):
        yield i*10

# La función mi_funcion() devuelve el valor 4, mientras que la función mi_generador() devuelve un generador que
# produce el valor 4. La diferencia es que el generador no almacena el valor en la memoria, sino que lo devuelve
# sobre la marcha. Para obtener el valor de un generador, necesitamos iterar sobre él, por ejemplo con un bucle for.


print(mi_funcion())
print(mi_generador())

gen = mi_generador()
print(next(gen)) # 10
print(next(gen)) # 20
print(next(gen)) # 30
print(next(gen)) # 40
# print(next(gen)) # Error: StopIteration

def mi_generador1():
    x=1
    yield x

    x+=1
    yield x

    x+=1
    yield x

gen1 = mi_generador1()
print(next(gen1)) # 1
print(next(gen1)) # 2

print("Hola Mundo")

print(next(gen1)) # 3
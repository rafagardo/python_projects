mi_lista = ['a', 'b', 'c']
otra_lista = ['hola', 55, 6.1]
resultado = mi_lista[0:]
mi_lista_2 = ['d', 'e', 'f']
mi_lista_3 = mi_lista + mi_lista_2

#mi_lista_3[0] = 'alfa'

mi_lista_3.append('g') #agrega elementos a la lista
eliminado = mi_lista_3.pop() #remueve uno de los elementos de la lista (si no agregas nada en () elimina el ultimo)

print(mi_lista_3)
print(eliminado)

lista = ['g', 'o', 'm', 'b', 'c']
lista.sort() #reordena la lista
lista.reverse() #reordena al reves la lista

print(lista)
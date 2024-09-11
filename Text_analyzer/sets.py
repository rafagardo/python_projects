mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_Set = {1,2,3}
print(type(otro_Set))
print(otro_Set)

print(2 in mi_set)

#-----------------------------------
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)

print(s3)
# podemos agregar valores con .add(): s1.add(4)
# podemos eliminar valores con .remove(3): s1.remove(3)
# podemos descartar elementos con .discard(): s1.discard(6)
# .pop(): elimina un elemento aleatorio
# podemos limpiar el set completo con .clear(): s1.clear()

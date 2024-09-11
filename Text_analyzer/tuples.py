mi_tuple = 1,2,(10,20),4

mi_tuple = list(mi_tuple)

mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))

#-----------------------------
a = (1,2,3)

x,y,z = a

print(a)

#----------------------------
t = (1,2,3,1)

print(t.count(1)) #cantidad de apariciones del numero 1 en mi tuple
print(t.index(2))

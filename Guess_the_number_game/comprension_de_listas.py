palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#------------------------------------------
lista_2 = [letra for letra in palabra] #tiene que ser la misma variable interna
print(lista_2)

#----------------------------------------------
lista_3 = [n for n in range(0,21,2)]
print(lista_3)

lista_4 = [n/2 for n in range(0,21,2)]
print(lista_4)

lista_5 = [n for n in range(0,21,2) if n*2 > 10]
print(lista_5)

lista_6 = [n if n*2 > 10 else 'no' for n in range(0,21,2)]
print(lista_6)

#------------------------------------------------------
pies = [10,20,30,40,50]
metros = [n/3.218 for n in pies]
print(metros)
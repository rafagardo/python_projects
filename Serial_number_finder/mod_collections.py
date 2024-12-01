from collections import Counter, defaultdict, namedtuple

numeros = [1, 2, 2, 6, 8, 6, 7, 8, 9, 10]
print(Counter(numeros))  # Counter({2: 2, 6: 2, 8: 2, 1: 1, 7: 1, 9: 1, 10: 1})
print(Counter("mississippi")) # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))  # Counter({'al': 2, 'pan': 2, 'vino': 2, 'y': 1})

serie = Counter([1,1,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5,5,5])
print(serie.most_common()) # [(1, 5), (5, 5), (2, 4), (3, 3), (4, 2)]
print(serie.most_common(2)) # [(1, 5), (5, 5)]
print(list(serie)) # [1, 2, 3, 4, 5]

mi_dicc = {'uno': 'verde', 'dos': 'rojo', 'tres': 'azul'}
print(mi_dicc['uno'])  # verde

mi_dicc1 = defaultdict(lambda: 'nada')
mi_dicc1['uno'] = 'verde'
print(mi_dicc1['uno'])  # verde
print(mi_dicc1['dos'])  # nada
print(mi_dicc1)  # defaultdict(<function <lambda> at 0x7f8b1c1b7d30>, {'uno': 'verde', 'dos': 'nada'})

mi_tupla = (500,19,65)
print(mi_tupla[0])  # 500

Persona = namedtuple('Persona', ['nombre', 'apellido', 'edad'])
ariel = Persona('Ariel', 'Garcia', 35)
print(ariel.nombre)  # Ariel
print(ariel.apellido)  # Garcia
print(ariel.edad)  # 35
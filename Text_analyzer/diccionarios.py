cliente = {'nombre': 'Juan',
               'apellido': 'Perez',
               'peso': 88,
               'talla': 1.76}

consulta = (cliente['apellido'])

print(consulta)

#-----------------------------------------------------------------------------

dicc = {'c1':55,
        'c2':[10,20,30],
        'c3':{'s1':100,
              's2':200}
        }

print(dicc['c3']['s2'])

#-------------------------------------------------------------------------------

dic = {'c1': ['a','b','c'],
       'c2': ['d','e','f']}

upper_case_dic = dic['c2'][1].upper()
print(upper_case_dic)

#------------------------------------------------------------------------------

dic_1 = {1:'a',
         2:'b'}
print(dic_1)

dic_1[3] = 'c'
print(dic_1)

dic_1[2] = 'B'
print(dic_1)

print(dic_1.keys())
print(dic_1.values())
print(dic_1.items())
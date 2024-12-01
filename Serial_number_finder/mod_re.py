import re

texto = "Si necestias ayuda, llama al 555-555-5555 o al 555-555-5556 las 24 horas del día"

patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

patron2 = 'al'
for hallazgo in re.finditer(patron2, texto):
    print(hallazgo.span())

patron3 = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron3, texto)
print(resultado.group())

patron4 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado2 = re.search(patron4, texto)
print(resultado2.group(1))
print(resultado2.group(2))
print(resultado2.group(3))

# clave = input("Introduce la clave: ")
# patron5 = r'\D{1}\w{7}'
# chequear = re.search(patron5, clave)
# print(chequear)

frase = "No atendemos lunes por la tarde ni los festivos"
buscar = re.search(r'lunes|martes', frase)
print(buscar)
buscar2 = re.search(r'....demos...', frase)
print(buscar2)
buscar3 = re.search(r'^\D', frase)
print(buscar3)
buscar4 = re.search(r'\D$', frase)
print(buscar4)
buscar5 = re.findall(r'[^\s]', frase)
print(buscar5)
buscar6 = re.findall(r'[^\s]+', frase)
print(buscar6)
print(' '.join(buscar6))
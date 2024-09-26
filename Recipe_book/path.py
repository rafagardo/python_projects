from pathlib import Path

base = Path.home()
guia = Path(base, 'Eurpoa', 'España', Path('Barcelona', 'Sagrada_Familia.txt'))
#guia2 = guia.with_name("La_Pedrera.txt")
#print(base)
print(guia)
#print(guia2)
print(guia.parent)
print(guia.parent.parent)
print(guia.parent.parent.parent)

# Para enumerar archivos existentes en una carpeta que contenga otras carpetas con archivos txt

#Para enumerar archivos txt que existan dentro de la carpeta Europa
guia3 = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print(txt)

#Para enumerar TODOS los archivos existentes dentro de la misma carpeta (aunque esten en sub carpetas)
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

# Rutas para ubicar carpetas especificas con relative_to
guia4 = Path('Eurpoa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)


from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/Rafa García/PycharmProjects/Python/Recipe_book/Prueba.txt")

ruta_windows = PureWindowsPath(carpeta)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, si existe")

print(ruta_windows)
name = input("Nombre completo: ")
ventas = int(input("Cantidad de las ventas generadas del mes: "))

comisiones = round(ventas * (13/100), 2)

print(f"¡Felicidades {name}! Has generado en comisiones este mes de ${comisiones}.")
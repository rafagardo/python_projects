"""  Crea una funcion llamada devolver_distintos() que reciba 3
 integers como parámetros.

 Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.

 Si la suma de los 3 numeros es menos a 10, va a devolver el número menor.

 Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a
 devolver el número de valor intermedio."""

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if  suma > 15:
        return max(num1,num2,num3)
    elif suma < 10:
        return min(num1,num2,num3)
    else:
        return sorted([num1,num2,num3])[1]

resultado = devolver_distintos(0,1,8)
print(f"El resultado es: {resultado}")
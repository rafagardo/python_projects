# def suma():
#     n1 = int(input("Ingrese el primer número: "))
#     n2 = int(input("Ingrese el segundo número: "))
#     print(f"La suma de {n1} y {n2} es {n1 + n2}")
#
# try:
#     # Intenta ejecutar el bloque de código
#     suma()
# except TypeError:
#     # Si hay un error, ejecuta este bloque de código
#     print("Estas intentando sumar un número con una cadena")
# except ValueError:
#     # Si hay un error, ejecuta este bloque de código
#     print("Estas ingresando un valor no numérico")
# else:
#     # Si no hay errores, ejecuta este bloque de código
#     print("No ha ocurrido ningún error")
# finally:
#     # Siempre se ejecuta, haya o no errores
#     print("Fin del programa")

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
        except:
            print("El valor ingresado no es un número entero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Fin del programa")

pedir_numero()


# def cambiar_letras(tipo):
#     def mayuscula(texto):
#         print(texto.upper())
#
#     def minuscula(texto):
#         print(texto.lower())
#
#     def una_funcion(funcion):
#         return funcion
#
#     una_funcion(mayuscula("Hola"))
#
#     if tipo == "mayuscula":
#         return mayuscula
#     elif tipo == "minuscula":
#         return minuscula
#
# operacion = cambiar_letras("mayuscula")
# operacion("Hola")

def decorar_saludo(funcion):
    def nueva_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return nueva_funcion

def mayuscula(palabra):
    print(palabra.upper())

def minuscula(palabra):
    print(palabra.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
# mayuscula("Python")
mayuscula_decorada("python")
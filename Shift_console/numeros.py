def numeros_perfumeria():
    for i in range(1, 10000):
        yield f"P - {i}"

def numeros_farmacia():
    for i in range(1, 10000):
        yield f"F - {i}"
def numeros_cosmetica():
    for i in range(1, 10000):
        yield f"C - {i}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(funcion):
    print("\n" + "*" * 23)
    print("Su numero es:")
    if funcion == "P":
        print(next(p))
    elif funcion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde su turno")
    print("*" * 23 + "\n")

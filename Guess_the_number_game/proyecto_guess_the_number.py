from random import *

nombre = input("Dime tu nombre: ")

print(f"""Bienvenido {nombre}, he pensado en un numero entre el 1 y el 100. 
Tienes solamente 8 intentos para adivinar el numero.""")

intentos = 0
numero_azar = randint(1,100)
estimado = 0

while intentos < 8:
    estimado = int(input("Cual es el numero? "))
    intentos += 1
    if estimado not in range(1,101):
        print("Eres tonto acaso?  Te dije que del 1 al 100 cabron")
    elif estimado < numero_azar:
        print("El numero es mas alto")
    elif estimado > numero_azar:
        print("""El numero es mas bajo""")
    else:
        print(f"Felicidades {nombre}! Eres un crack! Has acertado en {intentos} intentos!")
        break

if estimado != numero_azar:
    print(f"Lo siento, eres muy malo, se han acabo los intentos. El numero secreto era {numero_azar}")
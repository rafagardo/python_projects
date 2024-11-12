import numeros

def preguntar():
    print("Bienvenido a la Famracia Dominguez")
    while True:
        print("¿Que desea comprar?")
        print("[P] Perfumeria")
        print("[F] Farmacia")
        print("[C] Cosmetica")
        opcion = input("Ingrese una opcion: ")
        eleccion = opcion.upper()
        try:
            ["P", "F", "C"].index(eleccion)
        except ValueError:
            print("Opcion invalida")
        else:
            break

    numeros.decorador(eleccion)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Desea realizar otra compra? (s/n): ")
            opcion = otro_turno.upper()
            ["S", "N"].index(opcion)
        except ValueError:
            print("Opcion invalida")
        else:
            if opcion == "N":
                print("Gracias por su visita")
                break

inicio()

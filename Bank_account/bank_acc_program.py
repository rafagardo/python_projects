class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: ${self.balance}'

    def depositar(self, cantidad_deposito):
        self.balance += cantidad_deposito

    def retirar(self, cantidad_retiro):
        if self.balance >= cantidad_retiro:
            self.balance -= cantidad_retiro
            print('Retiro exitoso')
        else:
            print('Fondos insuficientes')

def crear_cliente():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    numero_cuenta = input('Ingrese su número de cuenta: ')
    return Cliente(nombre, apellido, numero_cuenta)

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 3:
        print('1. Depositar')
        print('2. Retirar')
        print('3. Salir')
        opcion = int(input('Ingrese una opción: '))
        if opcion == 1:
            cantidad_deposito = float(input('Ingrese la cantidad a depositar: '))
            mi_cliente.depositar(cantidad_deposito)
            print(mi_cliente)
        elif opcion == 2:
            cantidad_retiro = float(input('Ingrese la cantidad a retirar: '))
            mi_cliente.retirar(cantidad_retiro)
            print(mi_cliente)
        elif opcion == 3:
            print('Gracias por utilizar nuestros servicios')
        else:
            print('Opción inválida')

inicio()
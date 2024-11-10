# class Animal:
#
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
#
#     def nacer(self):
#         print("Este animal ha nacido")
#
#     def hablar(self):
#         print("Este animal emite un sonido")
#
# class Pajaro(Animal):
#
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo
#
#     def hablar(self):
#         print("Pio pio")
#
#     def volar(self, metros):
#         print(f"El pajaro ha volado {metros} metros")
#
# piolin = Pajaro(2, "amarillo",60)
# mi_animal = Animal(5, "negro")
#
# piolin.nacer()  # Este animal ha nacido
# piolin.volar(10)  # El pajaro ha volado 10 metros

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja ja")

    def hablar(self):
        print("Que tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar() # Hereda el metodo de la clase que este en la primera posicion, en este caso "Hola"

mi_nieto.reir()

print(Nieto.__mro__)


class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio pio pio")

    def volar(self, metros):
        print(f"Volando {metros} metros")

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(3)
Pajaro.mirar()

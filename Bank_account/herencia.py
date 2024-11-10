class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, "amarillo")
piolin.nacer() # Este animal ha nacido
print(piolin.edad) # 2
print(piolin.color) # amarillo

print(Pajaro.__bases__) # (<class '__main__.Animal'>,)
print(Animal.__subclasses__()) # [<class '__main__.Pajaro'>]


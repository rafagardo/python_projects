class Pajaro:

    alas = True #Atributo de clase

    def __init__(self, color, especie): #Constructor
        self.color = color
        self.especie = especie

pajaro = Pajaro('rojo', 'cardenal')

print(f'El color del pájaro es {pajaro.color} y es de la especie {pajaro.especie}')

print(Pajaro.alas)
print(pajaro.alas)
# mi_lista = [1,1,1,1]
# print(len(mi_lista)) # 4
#
# class Objeto:
#     pass
#
# mi_objeto = Objeto()
# print(len(mi_objeto)) # TypeError: object of type 'Objeto' has no len()
class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.autor} - {self.titulo}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el objeto")

mi_cd = CD("The Beatles", "White Album", 4)
print(mi_cd) # Album: The Beatles - White Album
# print(len(mi_cd)) # TypeError: object of type 'CD' has no len()
print(len(mi_cd)) # 4

# del mi_cd # Eliminamos la variable mi_cd

# print(mi_cd) # NameError: name 'mi_cd' is not defined
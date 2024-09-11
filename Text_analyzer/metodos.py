texto = "Este es el texto de Rafael"
a = "Aprender"
b = "Python"
c = "es"
d = "genial"

resultado_upper = texto[2].upper()
resultado_lower = texto[2].lower()
resultado_split = texto.split("t")
resultado_join = " ".join([a,b,c,d])
resultado_find = texto.find("texto")
resultado_replace = texto.replace("Rafael", "todos")

print(resultado_upper)
print(resultado_lower)
print(resultado_split)
print(resultado_join)
print(resultado_find)
print(resultado_replace)
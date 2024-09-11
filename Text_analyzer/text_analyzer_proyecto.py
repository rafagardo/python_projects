texto = input("Ingrese el texto a analizar: ")
primera_letra = input("Ingresa la primera letra que deseas analizar: ")
segunda_letra = input("Ingresa la segunda letra que deseas analizar: ")
tercera_letra = input("Ingresa la tercera letra que deseas analizar: ")

#Cuantas veces aparece cada letra
texto = texto.lower()
letras = [primera_letra.lower(), segunda_letra.lower(), tercera_letra.lower()]
contador_primera_letra = texto.count(letras[0])
contador_segunda_letra = texto.count(letras[1])
contador_tercera_letra = texto.count(letras[2])
print(f"""------------------------------------------------------
Se ha encontrado que la letra {letras[0]} aparece {contador_primera_letra} vez/veces. 
Se ha encontrado que la letra {letras[1]} aparece {contador_segunda_letra} vez/veces.
Se ha encontrado que la letra {letras[2]} aparece {contador_tercera_letra} vez/veces.
------------------------------------------------------""")

#Cuantas palabras hay en total
texto_lista = texto.split(" ")
contador_palabras = len(texto_lista)
print(f"""El texto introducido tiene exactamente {contador_palabras} palabras.
------------------------------------------------------""")

#Primera y ultima letra
primera_letra_texto = texto[0]
ultima_letra_texto = texto[-1]
print(f"""La primera letra del texto es "{primera_letra_texto}" y la última palabra es "{ultima_letra_texto}".
------------------------------------------------------""")

#Palabra en orden inverso
texto_lista.reverse()
texto_invertido = " ".join(texto_lista)
print(f"""El texto con las palabras en inverso es de esta forma: "{texto_invertido}".
------------------------------------------------------""")

#Aparece 'python'?
palabra_python = 'python' in texto
dicc = {True:'si', False:'no'}
print(f"""¿La palabra Python aparece? En este caso, la palabra 'python' {dicc[palabra_python]} se encuentra en el texto.
------------------------------------------------------""")

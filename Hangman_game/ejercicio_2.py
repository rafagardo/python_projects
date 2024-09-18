"""  Escribe una funcion (puedes ponerle cualquier nombre que quieras)
que reciba cualquier palabra como parametro, y que devuelva todas sus
letras unicas (sin repetir) pero en orden alfabetico.

Por ejemplo, si al invocar esta funcion pasamos la palabra 'entretenido',
deberia devolver ['d','e','i','n','o','r','t']"""

"""def letras_unicas(palabra):
    palabra_lista = []
    for letra in palabra:
        palabra_lista = list(letra)
    return palabra_lista

letras_unicas('ornitorrinco')"""


def letras_unicas_ordenadas(palabra):
    # Convertir la palabra a un conjunto para obtener las letras únicas
    letras_unicas = set(palabra)

    # Convertir el conjunto a una lista y ordenarla alfabéticamente
    letras_ordenadas = sorted(letras_unicas)

    return letras_ordenadas


# Ejemplo de uso
resultado = letras_unicas_ordenadas("entretenido")
print(f"Letras únicas ordenadas: {resultado}")
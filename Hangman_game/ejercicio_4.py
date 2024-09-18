"""  Escribe una funcion llamada contar_primos() que requiera un
solo argumento numerico.

Esta funcion va a mostrar en pantalla todos los numeros primos
existentes en el rango que va desde cero hasta ese numero incluido,
y va a devolver la cantidad de numeros primos que encontro.

Aclaracion, por convencion el 0 y el 1 no se consideran primos."""


def contar_primos(numero):
    # Función auxiliar para determinar si un número es primo
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Lista para almacenar los números primos
    primos = []

    # Recorrer desde 0 hasta el número proporcionado
    for num in range(2, numero + 1):
        if es_primo(num):
            primos.append(num)

    # Mostrar los números primos encontrados
    print(f"Números primos encontrados: {primos}")

    # Devolver la cantidad de números primos
    return len(primos)


# Ejemplo de uso
cantidad_primos = contar_primos(13)
print(f"Cantidad de números primos encontrados: {cantidad_primos}")
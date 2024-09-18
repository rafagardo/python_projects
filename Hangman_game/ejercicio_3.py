"""  Escribe una funcion que requiera una cantidad indefinida de argumentos.
 Lo que hara esta funcion es devolver True si en algun momento se ha ingresado
 al numero cero repetido dos veces consecutivos.

 Por ejemplo:

 (5,6,1,0,0,9,3,5) >>> True
 (6,0,5,1,0,3,0,1) >>> False"""

def cero_repetido(*args):
    # Recorrer la lista de números y verificar si en algún punto hay dos ceros consecutivos
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False
resultado = cero_repetido(1,2,3,0,0,5,7,8)
print(resultado)
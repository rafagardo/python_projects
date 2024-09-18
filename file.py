def solution(inputarray):
    cont = 0
    mult2 = []
    for number in inputarray:
        mult = number * (inputarray[cont+1])
        mult2.append(mult)
        cont += 1
        if cont == (len(inputarray) - 1):
            break
    return max(mult2)

resul = solution([3, 6, -2, -5, 7, 3])
print(resul)


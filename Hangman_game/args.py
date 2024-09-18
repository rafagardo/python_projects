def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5,6,10,500,100))

def sumas(*args):
    return sum(args)

print(sumas(5,6,10,500,100))
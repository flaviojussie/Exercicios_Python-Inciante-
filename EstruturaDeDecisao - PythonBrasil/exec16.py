import math

def calculaDelta(a, b, c):
    delt = math.pow(b, 2) - 4*a*c
    if delt >= 0:
        print('O valor de delta é:', delt)
        print('    X`:', calculaValorX1(delt, a, b))
        print('    X``:', calculaValorX2(delt, a, b))
    else:
        print('Não há raizes para a equação.')
def calculaValorX1(delt, a, b):
    x1 = ((-1*b) + math.sqrt(delt))/(2*a)
    return x1

def calculaValorX2(delt, a, b):
    x2 = ((-1*b) - math.sqrt(delt))/(2*a)
    return x2

a = int(input('Indique um valor para a: '))
b = int(input('Indique um valor para b: '))
c = int(input('Indique um valor para c: '))

if a != 0:
    calculaDelta(a, b, c)
else:
    print('Não é uma equação de segundo grau.')
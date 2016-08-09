num = int(input('Insira um numero: '))
fatorial = num
cont = num-1
if num <= 16:
    while cont != 0:
        fatorial *= cont
        cont -=1
else:
    print('Numero Invalido.')

print('Fatoria de %d é %d'%(num, fatorial))
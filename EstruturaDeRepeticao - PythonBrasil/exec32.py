num = int(input('Digite um numero: '))
fatorial = num
for i in range(1,num):
    fatorial *= i
print('O fatorial de %d é %d'%(num, fatorial))
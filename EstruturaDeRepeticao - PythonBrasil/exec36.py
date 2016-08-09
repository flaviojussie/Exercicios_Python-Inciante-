num = int(input('Digite um numero: '))
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o final: '))
for i in range(inicio,(fim+1)):
    res = num * i
    print('%d X %d = %d'%(num, i, res))
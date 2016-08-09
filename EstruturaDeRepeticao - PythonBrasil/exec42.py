numVezes = int(input('Quantos numeros você que inserir: '))
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
for i in range(numVezes):
    num = int(input('Digite o %d numero: '%(i+1)))
    if num >= 0 and num <= 25:
        intervalo1 += 1
    elif num >=26 and num <= 50:
        intervalo2 += 1
    elif num >= 51 and num <= 75:
        intervalo3 += 1
    elif num >= 76 and num <= 100:
        intervalo4 += 1

print('\n%d no intervalo [0-25]'%intervalo1)
print('%d no intervalo [26-50]'%intervalo2)
print('%d no intervalo [51-75]'%intervalo3)
print('%d no intervalo [76-100]'%intervalo4)
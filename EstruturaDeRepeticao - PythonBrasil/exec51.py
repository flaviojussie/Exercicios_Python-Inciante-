soma = 0
repetir = int(input('Digite a quantidade vezes que você quer que repita a sequência: '))
print('\nS = ', end = '')
for i in range(1, repetir+1):
    x = i
    y = i+2
    print('%d/%d'%(x,y), end = '')
    if i < repetir:
        print(' + ', end = '')
    soma += x/y
print('\n\nA soma das frações é iqual a: %2.2f'%soma)
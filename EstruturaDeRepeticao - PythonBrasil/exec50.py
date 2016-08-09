soma = 1
repetir = int(input('Quantas vezes deve se repetir o processo? '))
print('H = ', end='')
for i in range(1, 1+repetir):
    print('1/%d'%i,end='')
    if i < repetir:
        print(' + ', end='')
    soma += 1/i
print('\n\nA soma das frações é: %2.2f'%soma)
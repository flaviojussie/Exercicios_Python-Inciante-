cont = 1
soma = 0
maior = 0
temp = 1
while temp != 0:
    temp = float(input('Temperatura %d: '%cont))
    if temp > maior:
        maior = temp
    soma += temp
    cont += 1
media = soma/cont
print('A maior nota registrada no periodo foi %d e a media geral foi %5.1f'%(maior, media))
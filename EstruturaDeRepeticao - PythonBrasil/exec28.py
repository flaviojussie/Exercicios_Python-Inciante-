numtotal = int(input('Quantidade de CDs na coleção:'))
soma = 0
for i in range(numtotal):
    valorUni = float(input('Valor unitário do CD %d: ' %(i+1)))
    soma += valorUni
media = soma/numtotal
print('O valor medio por CD é de %5.2f'%media)
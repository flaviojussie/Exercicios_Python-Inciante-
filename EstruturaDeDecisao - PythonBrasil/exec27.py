def calculaPreco(arq, prec):
    precoTotal = prec*arq[1]
    if arq[1] >= 8 or precoTotal == 25:
        precoTotal -= (precoTotal * 0.10)
    return precoTotal

print('''Compre sua frutas.
PREÇOS:\n
        Até 5 Kg          Acima de 5 Kg\n
Morango R$ 2,50    por    Kg R$ 2,20 por Kg
Maçã R$ 1,80       por    Kg R$ 1,50 por Kg\n''')

arquivo = [int(input('Digite qual a fruta (1 - morago/ 2 - maçã): ')), int(input('Digite quantos quilos voce deseja comprar: '))]
if arquivo[0] == 1 and arquivo[1] > 5:
    preco = 2.50
elif arquivo[0] == 1 and arquivo[1] >= 5:
    preco = 2.20
elif arquivo[0] == 2 and arquivo[1] > 5:
    preco = 1.80
elif arquivo[0] == 2 and arquivo[1] >= 5:
    preco = 1.50
else:
    print('Fruta invalida!')

print('\nValor total da compra: R$',calculaPreco(arquivo, preco))



print('''LOJAS TABAJARA
\npara sair digite 0\n''')
cont = 1
valorUni = 1
valorTotal = 0
while valorUni != 0:
    valorUni = float(input('Produto %d R$: ' %cont))
    valorTotal += valorUni
    cont += 1

dinheiro = float(input('Valor recebido R$: '))
troco = dinheiro - valorTotal

print('Troco %5.2f' %troco)
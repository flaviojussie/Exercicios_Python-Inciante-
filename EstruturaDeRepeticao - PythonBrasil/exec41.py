cont = 0
valorParcela = 0
parcela = 1
valorDivida = float(input('Insira o valor da divida: '))
print('\nValor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela')
for i in [0,10,15,20,25]:
    dividaTotal = valorDivida
    valorJuros = valorDivida*(i/100)
    dividaTotal += valorJuros
    valorParcela = dividaTotal/parcela
    print('R$ %5.2f            %d                    %d                     R$ %5.2f'%(dividaTotal,valorJuros,cont, valorParcela))
    cont += 3
    parcela = cont


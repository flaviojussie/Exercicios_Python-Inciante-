preco = float(input('Digite o valor do pão: '))
print('Padaria pão de Ontem - Tabela de Preços')
for i in range(50):
    i += 1
    print('%d - %5.2f' %(i, i*preco))

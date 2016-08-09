def ajustes(sal, reaj):

    aumento = (sal*reaj)
    novosal = sal + aumento

    imprimeTela(sal, reaj, aumento, novosal)

def imprimeTela(sa, re, au, ns):
    print()
    print('O salario atual é R$', sa)
    print('Reajuste aplicado foi %2f', (re*100),'%')
    print('O valor do aumento é R$', au)
    print('Novo salarios é R$', ns)

salario = float(input('Digite o salario: '))
if salario < 280:
    ajustes(salario, 0.20)
elif salario > 280 and salario < 700:
    ajustes(salario, 0.15)
elif salario > 700 and salario < 1500:
    ajustes(salario, 0.10)
elif salario >= 1500:
    ajustes(salario, 0.05)
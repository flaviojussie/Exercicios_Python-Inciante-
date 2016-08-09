soma = 0
saltos = []
cont = 0
nome = input('Atleta: ')
for i in range(5):
    salto = float(input('Entre com o %d salto: '%(i+1)))
    saltos.append(salto)
for i in saltos:
    if i != max(saltos) and i != min(saltos):
        soma += i
media = soma/3
for i in ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']:
    print('%s salto: %2.2f'%(i, saltos[cont]))
    cont += 1
print('\nMelhor salto %2.2f'%max(saltos))
print('Melhor salto %2.2f'%min(saltos))
print('\nMédia dos demais saltos %2.2f'%media)
print('''\nResultado final:
%s: %2.2f'''%(nome, media))
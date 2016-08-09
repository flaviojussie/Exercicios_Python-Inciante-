notas = []
soma = 0
for i in range(4):
    notas.append(float(input('Informe a %d nota: '%(i+1))))
    soma += notas[i]
print('A media geral é: %2.1f'%(soma/4))
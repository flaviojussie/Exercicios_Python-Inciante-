vetor = []
soma = 0
produto = 1
for i in range(5):
    vetor.append(int(input('Digite um numero: ')))
    soma += vetor[i]
    produto *= vetor[i]
print('O vetor é composto pelos numeros: ', vetor)
print('A multiplicação dos valores do vetor é ', produto)
print('A soma dos valores do vetor é ', soma)
vetor = []
impares = []
pares = []
for i in range(20):
    vetor.append(int(input('Digite o %d número: '%(i+1))))
for i in vetor:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('O vetor é formado pelos numeros:',vetor)
print('Os numeros pares do vetor são: ', pares)
print('Os numeros impares do vetor são: ', impares)
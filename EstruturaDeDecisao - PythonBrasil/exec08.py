num = [(input('Digite um preço:'))for i in range(3)]
cont=0
menor = num[cont]
for i in num:
    if menor > i:
        menor = i
    cont += 1

print('O menor preço é: ',menor)

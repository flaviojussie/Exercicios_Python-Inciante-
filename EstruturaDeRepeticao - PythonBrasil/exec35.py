num = int(input('Inserir o interivalo: '))
verif = 0
primos = []
for i in range(1,(num+1)):
    for j in range(1,(i+1)):
        if i % j == 0:
            verif += 1
    if verif <= 2:
        primos.append(i)
    verif = 0
print('Primos no internalo', primos)
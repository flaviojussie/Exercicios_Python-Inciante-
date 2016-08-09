num = int(input('Digite o final do intervalo desejado: '))
i, j = 1, 1
primos = []
verificador = 0

while i <= num:
    while j <= i:
        if i % j == 0:
            verificador += 1
        j += 1
    if verificador <= 2:
        primos.append(i)
    i += 1
    j = 1
    verificador = 0
print(primos)
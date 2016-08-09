def escolherCedulas(valor, div):
    cedulas = valor//div
    resto = valor%div
    if cedulas == 0:
        cedulas = 1

    return resto, cedulas

saque = int(input('Valor do saque: '))
resto = [saque]

for i in [100, 10, 5, 1]:
    resto = escolherCedulas(resto[0], i)
    print(resto[1],'cedulas de R$',float(i))



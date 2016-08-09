salarioInicial = 1000
salarioAtual = salarioInicial
aumento = 0.015
anoInicial = 1995
anoAtual = 2004

while anoInicial <= anoAtual:
    salarioAtual += (salarioAtual*aumento)
    aumento *= 2
    anoInicial += 1
    print(anoInicial)

print('O salario atual é %5.2f' %salarioAtual)
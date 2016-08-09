def impostoRenda(sal, des):
    desconto = sal * des
    return desconto


hs = int(input('Digite as horas trabalhadas no mês: '))
vh = int(input('Valor da hora: '))

salBruto = hs*vh
sindicato = salBruto*0.03
fgts = salBruto*0.11
salLiquido = salBruto - sindicato - fgts
print('')

if salBruto < 900:
    ir = 'Insento.'
elif salBruto >= 900 and salBruto < 1500:
    ir = impostoRenda(salBruto, 0.05)
elif salBruto >= 1500 and salBruto < 2500:
    ir = impostoRenda(salBruto, 0.10)
else:
    ir = impostoRenda(salBruto, 0.20)

print('Salario bruto: ', salBruto)
print('Descontos:')
print('   - Sindicato: ', sindicato)
print('   - Fgts: ' , fgts)
print('Imposto de renda: ', ir)
print('Salario liquido: ', salLiquido)
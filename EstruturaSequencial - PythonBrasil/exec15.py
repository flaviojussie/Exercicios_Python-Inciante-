valorHora = 10.60
horasTrabalhadas = 200
salarioBruto = valorHora*horasTrabalhadas
impostos = salarioBruto*0.11
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
salarioLiquido = salarioBruto-(impostos+inss+sindicato)

print 'Salario Bruto = R$', salarioBruto
print 'Impostos = R$', impostos
print 'Inss = R$', inss 
print 'Sindicato = R$', sindicato
print 'Salario Liquido = R$', salarioLiquido

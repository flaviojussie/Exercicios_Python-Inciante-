nome = ''
idade = 0
sexo = ''
salario = 0
estadocivil = ''
while len(nome) <= 3:
    nome = input('nome: ')

while idade <= 0 or idade > 150:
    idade = int(input('idade: '))

while salario == 0:
    salario = float(input('salario: '))

while sexo not in ['f', 'm']:
    sexo = input('sexo (M/F): ')

while estadocivil not in ['s','c','v','d']:
    estadocivil = input('estado civil: (s/c/v/d): ')

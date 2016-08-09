notas = []
media = 0
x = 0
cont = 0
for i in range(3):
    soma = 0
    media = 0
    notas.append(input('Nome do aluno: '))
    for j in range(1,5):
        nota = float(input('Insira a nota %d: '%j))
        notas.append(nota)
        soma += nota
    media = soma/j
    notas.append(media)

print('\n\nOs alunos que ficaram acima da media 7.0 foram:')
while cont < len(notas):
    if notas[cont+5] >= 7:
        print(notas[cont],'com nota parciais ', end=' ')
        for i in range(1,5):
            print(notas[cont+i], end=' ')
        print('e média', notas[cont+5])
    cont += 6
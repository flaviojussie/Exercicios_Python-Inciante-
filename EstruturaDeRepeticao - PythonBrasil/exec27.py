porturmas = int(input('Numero de turmas: '))
turmas = []
cont = 0
while cont < porturmas:
    alunos = int(input('Numero de alunos da turma: '))
    if alunos > 0 and alunos <= 40:
        turmas.append(alunos)
        cont += 1
    else:
        print('Numero Invalido!')
cont = 1
print('\n')
for i in turmas:
    print('%d alunos na turma %d' %(i, cont))
    cont += 1

n1, n2 = int(input('Nota 1: ')), int(input('Nota 2: '))
media = (n1 + n2)/2

if media >= 7:
    print('Aluno nota,', media, 'Aprovado')
elif media == 10:
    print('Aluno nota,', media ,'Aprovado com distinção')
elif media < 7:
    print('Aluno Repovado, nota:', media)

nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

media = (nota1+nota2+nota3)/3

if media >= 7 and media > 10:
    print('Aprovado com média ', media)
elif media < 7:
    print('Reprovado com média ', media)
elif media == 10:
    print('Parabáns aprovado com média ', media)
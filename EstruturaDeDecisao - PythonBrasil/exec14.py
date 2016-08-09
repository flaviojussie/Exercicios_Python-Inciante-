def conceito(med):
    if med >= 9:
        idx = 0
    elif med >= 7.5 and med < 9:
        idx = 1
    elif med >= 6 and med < 7.5:
        idx = 2
    elif med >= 4 and med < 6:
        idx = 3
    else:
        idx = 4
    con = ['A', 'B', 'C', 'D', 'E']
    return con[idx]

n1, n2 = int(input('Insira a nota 1: ')), int(input('Insira a nota 2: '))
media = (n1+n2)/2
conc = conceito(media)

print('A media geral é: ', media)
print('O conceito é ', conc)

if conceito(media) in 'ABC':
    print('Aprovado')
else:
    print('Reprovado')

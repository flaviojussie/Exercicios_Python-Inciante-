eleitores = int(input('Insira o numero de eleitores: '))
print('''\nPara votar em fulano - 1
Para votar em cicrano - 2
Para votar em beltrano - 3
Para votar em branco - 4\n''')

cont = 0
fulano = 0
cicrano = 0
beltrano = 0
branco = 0
nulos = 0

candidatos = ['Fulano','Cicrano','Beltrano']

while cont < eleitores:
    voto = int(input('Digite seu voto: '))
    if voto == 1:
        fulano += 1
    elif voto == 2:
        cicrano += 1
    elif voto == 3:
        beltrano += 1
    elif voto == 4:
        branco += 1
    else:
        nulos += 1
    cont += 1

print('''\n\nRelação dos votos:
FULANO - %d
CICRANO - %d
BELTRANO - %d
BRANCO - %d
NULOS - %d'''%(fulano, cicrano, beltrano, branco, nulos))

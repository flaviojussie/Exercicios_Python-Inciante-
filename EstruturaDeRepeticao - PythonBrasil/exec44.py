sair = 's'
print('''Complete seu voto.
1 - para votar em Fulano
2 - para votar em Cicrano
3 - para votar em Beltrano
4 - para votar em Zezinho
5 - para nulo
6 - para branco''')
fulano = 0
cicrano = 0
beltrano = 0
zezinho = 0
nulo = 0
branco = 0
totalEleitores = 0

while sair == 's':
    voto = int(input('Digite seu voto: '))
    sair = input('Deseja continuar votando (S/N): ')
    if voto == 1:
        fulano += 1
    elif voto == 2:
        cicrano += 1
    elif voto == 3:
        beltrano += 1
    elif voto == 4:
        zezinho += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    totalEleitores += 1

perNulos = (nulo*100)/totalEleitores
perBranco = (branco*100)/totalEleitores

print('Fulano %d votos.'%fulano)
print('Cicrano %d votos.'%cicrano)
print('Beltrano %d votos'%beltrano)
print('Zezinho %d votos'%zezinho)
print('A soma dos votos nulos %d'%nulo)
print('A soma dos votos em branco %d\n'%branco)
print('O percentual de votos nulos é %5.1f'%perNulos)
print('O percentual de votos brancos é %5.1f'%perBranco)

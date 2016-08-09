codigo = 0
somaVeiculos = 0
somaAcidentes = 0
media = 0
cid = 0
i = True
while codigo < 5:
    print('\nEntre coma as informações da cidade %d\n'%((codigo+1)))
    numVeiculos = int(input('Insira o numero de veiculos de passeio em 1999: '))
    numAcidentes = int(input('Insira o numero de acidentes com vitima registrados em 1999: '))
    if i == True:
        menorIndice = numAcidentes
        maiorIndice = numAcidentes
        codMenor = (codigo+1)
        codMaior = (codigo+1)
        i = False

    if numAcidentes < menorIndice:
        menorIndice = numAcidentes
        codMenor = (codigo+1)
    if numAcidentes > maiorIndice:
        maiorIndice = numAcidentes
        codMaior = (codigo+1)

    if numVeiculos < 2000:
        somaAcidentes += numAcidentes
        cid +=1

    somaAcidentes += numAcidentes
    somaVeiculos += numVeiculos
    codigo += 1

mediaAcidentes = somaAcidentes/codigo
mediaVeiculos = somaVeiculos/cid

print(codigo)
print('\nA cidade com maior numero de acidentes com morte é a cidade %d com %d mortes.'%(codMaior, maiorIndice))
print('A cidade com meor numreo de acidentes com morte é a cidade %d com %d de mortes.'%(codMenor, menorIndice))
print('A media de veiculos de passeio nas cidades pesquisadas é %d'%mediaVeiculos)
print('Nas cidades com menos de 2000 veiculos de passeio a media de acidentes com morte é %d mortes.'%mediaAcidentes)
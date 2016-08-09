idades = 1
somaIdades = 0
cont = 0
while idades != 0:
    idades = int(input('Digite uma idade ou 0 para sair: '))
    somaIdades += idades
    if idades > 0:
        cont += 1
media = somaIdades//cont
if media >= 0 and media <=25:
    print('A turma é jovem, media %d anos.'%media)
elif media >= 26 and media <= 60:
    print('A turma é adulta, media %d anos.'%media)
else:
    print('A turma é idosa, media %d anos.'%media)

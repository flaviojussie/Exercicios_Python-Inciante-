cont = 0
soma = 0
sair = 's'
while sair == 's' or sair == 'S':
    notas = float(input('Digite a %d Nota: ' %(cont+1)))
    sair = input('Deseja incluir outra nota? S/N ')
    soma += notas
    cont += 1

print(soma, cont)
media = soma / cont

print('A media das %d notas é %5.1f' %(cont, media))
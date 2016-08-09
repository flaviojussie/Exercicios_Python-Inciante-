codigo = 1
alto = 0
baixo = 0
magro = 0
gordo = 0
i = True
while codigo != 0:
    codigo = int(input('Digite seu o código: '))
    if codigo != 0:
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura '))
    if i == True:
        baixo = altura
        baixcod = codigo
        magro = peso
        magcod = codigo
        i = False

    if altura > alto:
        alto = altura
        altcod = codigo
    if altura < baixo:
        baixo = altura
        baixcod = codigo
    if peso > gordo:
        gordo = peso
        gordcod = codigo
    if peso < magro:
        magro = peso
        magcod = codigo

print('\nMais alto  - cod. %d | altura %5.2f' %(altcod, alto))
print('Mais baixo - cod. %d | altura %5.2f' %(baixcod, baixo))
print('Mais gordo - cod. %d | peso %5.1f' %(gordcod, gordo))
print('Mais magro - cod. %d | peso %5.1f' %(magcod, magro))
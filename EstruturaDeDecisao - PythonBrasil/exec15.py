def triangulo(lad):
    trian = 3
    cont = 1
    idx = 2
    for i in range(3):
        soma = lad[cont] + lad[i]
        subtracao = lad[cont] - lad[i]
        if lad[cont]!=lad[i]:
            trian -= 1
        if subtracao < lad[idx] and soma > lad[idx]:
            return trian
        else:
            return False
        cont += 1
        idx += 1
        if idx >= 2:
            idx = 0
        if cont > 2:
            cont = 0

lados = [(int(input('Digite a media do lado: ')))for i in range(3)]
if triangulo(lados) == 3:
    print('Forma um triangulo equiltero')
elif triangulo(lados) == 2:
    print('Forma um triangulo isóciles')
elif triangulo(lados) == 1:
    print('Forma um triangulo escaleno')
elif triangulo(lados) == False:
    print('Não forma nenhum triangulo')



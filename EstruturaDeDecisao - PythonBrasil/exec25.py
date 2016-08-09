print('Vamos começar o interrogatorio...')
perg = ['' for i in range(5)]
perg[0] = input('Telefonou para a vítima? (S/N)')
perg[1] = input('Esteve no local do crime? (S/N)')
perg[2] = input('Mora perto da vítima? (S/N)')
perg[3] = input('Devia para a vítima? (S/N)')
perg[4] = input('Já trabalhou com a vítima? (S/N)')

indicio = 0
for i in perg:
    aux = str(i)
    if aux == 's' or aux == 'S':
        indicio += 1

print()
if indicio == 2:
    print('Suspeito')
elif indicio ==3 or indicio == 4:
    print('Cumplice')
elif indicio == 5:
    print('Assassino')
else:
    print('Inocente')
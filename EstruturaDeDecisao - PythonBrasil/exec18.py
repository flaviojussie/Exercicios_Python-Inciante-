data = input('Informe uma data (dd/mm/aaaa): ')

if len(data)==10:
    dias = int(data[:2])
    meses = int(data[3:5])
    anos = int(data[6:])

    if dias <= 31 and meses <= 12 and anos >= 0:
        print('Ano Válido!')
    else:
        print('Ano Invalido!')
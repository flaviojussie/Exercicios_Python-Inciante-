def arrendondar(n):
    arrend = n%int(n)
    return arrend

num = float (input('Entre com um numero:'))

if arrendondar(num) != 0:
    print('Numero decimal.')
else:
    print('Numero inteiro.')


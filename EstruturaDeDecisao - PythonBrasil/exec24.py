def calculadora(x, y, op):
    if op == 1:
        z = x + y
        operacao = 'adição'
    elif op == 2:
        z = x - y
        operacao = 'subtração'
    elif op == 3:
        z = x * y
        operacao = 'multiplicação'
    elif op == 4:
        z = x / y
        operacao = 'divisão'
    else:
        print('Opção invalida!')
    resp = analizadorderesposta(z, operacao)
    return resp

def analizadorderesposta(n, oper):
    if n%2==0:
        a = 'par, '
    else:
        a = 'impar, '
    if n >= 0:
        b = 'positivo '
    else:
        b = 'negativo '
    if n%int(n)==0:
        n = int(n)
        c = 'inteiro.'
    else:
        c = 'decimal.'

    resp = 'A resposta da '+ oper + ' é ' + str(n) + ' que é um numero é '+ a + b + 'e ' + c
    return resp


num1 = float(input('digite o primeiro numero: '))
num2 = float(input('digite o segundo numero: '))
print('qual operação deseja realizar?')
print('')
print('(1 - adição, 2 - subitração, 3 - multiplicação, 4 - divisão)')
opcao = int(input('qual a sua opção?'))

print(calculadora(num1, num2, opcao))




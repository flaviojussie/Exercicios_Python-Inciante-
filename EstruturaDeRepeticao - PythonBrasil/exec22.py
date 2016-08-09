num = int(input('Digite um numero: '))
cont = 1
divisor = []
primo = 0
while cont <= num:
    if num % cont == 0:
        primo += 1
        divisor.append(cont)
    cont += 1
if primo == 1:
    print(num, 'é primo, pois é divisivel apenas por', divisor)
else:
    print(num, 'não é primo pois é divisivel por', divisor)
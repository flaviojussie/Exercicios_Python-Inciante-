num = int(input('Digite um numero: '))
cont = 1
primo = 0
while cont < num:
    if num % cont == 0:
        primo += 1
    cont += 1
if primo == 1:
    print('%d é um numero primo.'%num)
else:
    print('%d não é primo.'%num)
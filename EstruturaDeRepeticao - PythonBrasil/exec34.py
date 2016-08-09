num = int(input('Digite o numero: '))
primo = 0
for i in range(1,(num+1)):
    if num % i == 0:
        primo += 1
if primo <= 2:
    print('%d é um numero primo.'%num)
else:
    print('%d não é um numero primo.'%num)
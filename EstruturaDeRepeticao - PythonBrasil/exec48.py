num = int(input('Digite um numero: '))
aux = 0
i = (len(str(num))) - 1
j = 1
while i >= 0:
    invert = num % 10
    num = num//10
    aux += invert * (10**i)
    i -= 1
num = aux
print(num)
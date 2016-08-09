num = [(int(input('Insira o valor:')))for i in range(3)]
cont = 0

while cont < len(num):
    for i in num:
            if i > num[cont]:
                menor = num[cont]
                num[cont] = i
                num[i-1] = menor
            else:
                num[cont] =

    cont += 1

print(num)
par, impar = 0, 0

for i in range(10):
    num = int(input('Digite os numeros: '))
    if num%2==0:
        par += 1
    else:
        impar += 1
print(par, 'são pares e', impar,'são impares.')
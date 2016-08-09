print('Insira 3 numeros:')
n1 = input()
n2 = input()
n3 = input()

aux = 0
if n1 < n2:
    maior = n2
else:
    maior = n1
if maior < n3:
    maior = n3

print(maior)
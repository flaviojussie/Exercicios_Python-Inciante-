base = int(input('Digite a base:'))
exp = int(input('Digite o expoente: '))

i = 0
potencia = 1

while i < exp:
    potencia *= base
    i += 1
print(potencia)
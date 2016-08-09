a,b,c,d,e = int(input('Insira cinco numeros:\n ')),int(input()),int(input()),int(input()),int(input())

menor = a
if a > b:
    menor = b
if b > c:
    menor = c
if c > d:
    menor = d
if d > e:
    menor = e

print(menor)
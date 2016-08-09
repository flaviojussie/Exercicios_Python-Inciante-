letra = input("Digite uma letra: ")
aux = ''
for i in ['a','e','i','o'','u'']:
    if i == letra:
        aux = i
if letra == aux:
    print('A letra digitada é uma vogal.')
else:
    print('A letra digitada é uma consoante.')
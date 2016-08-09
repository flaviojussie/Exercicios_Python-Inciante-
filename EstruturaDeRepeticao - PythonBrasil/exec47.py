atleta = input('Nome do atleta: ')
notas = []
soma = 0
for i in range(7):
    nota = float(input('Nota %d: '%(i+1)))
    notas.append(nota)
for i in notas:
    if i != max(notas) and i != min(notas):
        soma += i
media = soma/(len(notas)-2)
for i in range(7):
    print('Nota %d: %1.1f'%((i+1), notas[i]))
print('''\nResultado Final:
Atleta: %s
Melhor nota: %2.1f
Pior nota: %2.1f
Media: %2.1f'''%(atleta, max(notas), min(notas), media))
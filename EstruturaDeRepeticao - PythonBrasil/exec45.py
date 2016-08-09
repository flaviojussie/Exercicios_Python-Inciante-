gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
novo = 'S'
maior = ['', 0]
menor = ['',10]
cont = 1
usuarios = 0
acertosGerais = 0
while novo.upper() == 'S':
    nome = input('Digite seu nome: ')
    respostas = []
    for i in range(10):
        item = input('Informe o item assinalado na questão %d:' %cont )
        respostas.append(item.upper())
        cont +=1
    j = 0
    i = 0
    acertos = 0
    while i < len(gabarito):
        if gabarito[i] == respostas[j]:
            acertos += 1
            acertosGerais += 1
        j += 1
        i += 1

    if maior[1] < acertos:
        maior[1] = acertos
        maior[0] = nome

    if menor[1] > acertos:
        menor[1] = acertos
        menor[0] = nome

    usuarios += 1
    cont = 0
    novo = input('Deseja continuar com outro usuario? (S/N) ')

media = acertosGerais/usuarios
print('\n%d alunos usaram o sistema.'%usuarios)
print('A maior nota foi do aluno %s: %2.1f'%(maior[0], maior[1]))
print('A menor nota foi do aluno %s: %2.1f'%(menor [0], menor[1]))
print('A media geral da turma foi %2.1f'%media)
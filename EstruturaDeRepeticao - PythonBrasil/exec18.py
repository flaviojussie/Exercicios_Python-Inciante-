num = 1
maior = 0
menor = 0
soma = 0
while True:
    num = int(input('Insira um valor: '))
    if num == 0:
        print('O menor numero digitado foi %d e o maior é %d e a soma dos nomes digitados é %d.' %(menor, maior, soma))
        break

    if num > maior:
        menor = maior
        maior = num
    soma += num
def calculadora(tipo, quilos, pagamento):
    unidade = tabelapreco(tipo, quilos)
    precototal = unidade*quilos
    desconto = precototal*formadepagamento(pagamento)
    valorpago = precototal - desconto
    return precototal, desconto, valorpago

def tabelapreco(tip, quilo):
    if tip == 1 and quilo <= 5:
        preco = 4.90
    elif tip == 1 and quilo > 5:
        preco = 5.80
    elif tip == 2 and quilo <= 5:
        preco = 5.90
    elif tip == 2 and quilo > 5:
        preco = 6.80
    elif tip == 3 and quilo <= 5:
        preco = 6.90
    elif tip == 8 and quilo >5:
        preco = 7.80
    else:
        print('Invalido')

    return preco

def formadepagamento(pag):
    if pag == 1:
        desc = 0
    elif pag == 2:
        desc = 0.05
    else:
        print('Invalido')
    return desc

carnes = ['File Duplo', 'Alcatra', 'Picanha']
formPag = ['Dinheiro', 'Cartão Tabajara']

print('''Bemvindo ao supermecado TABAJATA!
    VEJA NOSSA PROMOÇÕES\n
            Até 5 Kg             Acima de 5 Kg\n
File Duplo   R$ 4,90 por Kg      R$ 5,80 por Kg
 Alcatra     R$ 5,90 por Kg      R$ 6,80 por Kg
 Picanha     R$ 6,90 por Kg      R$ 7,80 por Kg\n''')

tipo = int(input('Escolha qual o tipo de carne: 1-file Duplo / 2-Alcatra / 3-Picanha: '))
quilos = int(input('Digite o quantos quilos deseja comprar: '))
pagamento = int(input('Escolha a forma de pagamento: 1-Dinheiro / 2-Cartão Tabajara: '))
detalheCompra = calculadora(tipo,quilos, pagamento)

print('''----------- Recido de Compras ------------\n
Tipo                  ''',carnes[tipo-1],'''
quantidade            ''',quilos,'''Kg
preço total           ''',detalheCompra[0],'''
tipo de pagamento     ''',formPag[pagamento-1],'''
desconto              ''',detalheCompra[1],'''
valor a pagar         ''',detalheCompra[2])

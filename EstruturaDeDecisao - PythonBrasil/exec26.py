def calculadoracombustivel(lt, prec, desc):
    precoTotal = (lt*prec)
    precoTotal -= (precoTotal*desc)
    return precoTotal

def calculoDesconto(lt, opcao):
    if opcao == 'G' and lt > 0 and lt <= 20:
        preco = 2.50
        desconto = 0.03
    elif opcao == 'G' and lt > 20:
        preco = 2.50
        desconto = 0.05
    elif opcao == 'A' and lt < 0 and lt <= 20:
        preco = 1.90
        desconto = 0.03
    elif opcao == 'A' and lt > 20:
        preco = 1.90
        desconto = 0.05

    return preco, desconto

litros = int(input('digite quantos litros: '))
opcao = input('digite (G - para gasolina) ou (A - para alcool): ')

desconto = calculoDesconto(litros, opcao)
print(calculadoracombustivel(litros, desconto[0], desconto[1]))


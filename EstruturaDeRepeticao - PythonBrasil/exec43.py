print('''\nEspecificação   Código    Preço
Cachorro Quente   100     R$ 1,20
Bauru Simples     101     R$ 1,30
Bauru com ovo     102     R$ 1,50
Hambúrguer        103     R$ 1,20
Cheeseburguer     104     R$ 1,30
Refrigerante      105     R$ 1,00\n''')

codigo = 1
cont, i = 0, 0
cq, bs, bo, hb, ch, re = 0, 0, 0, 0, 0, 0
valTotal = 0
while codigo != 0:
    codigo = int(input('Insira o codigo do produto: '))
    if codigo != 0:
        quant = int(input('Quantidade: '))
        if codigo == 100:
            cq += quant
        elif codigo == 101:
            bs += quant
        elif codigo == 102:
            bo += quant
        elif codigo == 103:
            hb += quant
        elif codigo == 104:
            ch += quant
        elif codigo == 105:
            re += quant


print("--------Cupom Fiscal -------")
if cq != 0:
    val = 1.20
    valTotal += cq*val
    print('Cachorro Quente %d - R$ %5.2f'%(cq,(cq*val)))
if bs != 0:
    val = 1.30
    valTotal += bs*val
    print('Bauru Simples %d - R$ %5.2f' % (bs,(bs*val)))
if bo != 0:
    val = 1.50
    valTotal += bo*val
    print('Bauru com ovo %d - R$ %5.2f' % (bo,(bo*val)))
if hb != 0:
    val = 1.20
    valTotal += hb*val
    print('Hambúrguer %d - R$ %5.2f' % (hb,(hb*val)))
if ch != 0:
    val = 1.30
    valTotal += ch*val
    print('Cheeseburguer  %d - R$ %5.2f' % (ch,(ch*val)))
if re != 0:
    val = 1.00
    valTotal += re*val
    print('Refrigerante  %d - R$ %5.2f' % (re,(re*val)))
print('\nValor total a pagar - R$ %5.2f'%valTotal)

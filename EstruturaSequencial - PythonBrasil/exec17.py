# Esse programa e uma variacao do anterios so que mais aprimorado.

# Informar a quantidade de metros quadrados que deseja pintar
# A 

metrosQuad = 5661
print 'O valor informado de metros quadrados foram:', metrosQuad,'m2'
print ''
litros = metrosQuad/6
latas_M=litros//18+1
preco_M = latas_M*80

latas_P= int((litros//3.6)+1)
preco_P = latas_P*25

restante = litros%18
latas_LM = litros//18
latas_LP = int(((restante +(restante * 0.10))//3.6)+1)
preco_Mscl = (80*latas_LM) + (25*latas_LP)
print 'Eh necessario', latas_M, 'latas (18 litros) que custarao R$', preco_M
print 'Ou', latas_P, 'latas (3,6 litros) que custarao R$', preco_P
print 'Ou', latas_LM, 'e', latas_LP, 'latas (3,6 litros) que custarao R$', preco_Mscl
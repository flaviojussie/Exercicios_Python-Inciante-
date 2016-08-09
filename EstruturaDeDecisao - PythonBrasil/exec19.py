def grafiaExtensso(num, quant):
    c = 'centena'
    d = 'dezena'
    u = 'unidade'
    compl = ''
    if num == 0:
        return compl

    elif num == 1:
        if quant == 100:
            compl = ','
            return str(num)+' '+ c + compl
        elif quant == 10:
            compl = ' e'
            return str(num)+' '+ d + compl
        else:
            return str(num)+' '+ u
    elif num >= 2:
        if quant == 100:
            compl = ','
            return str(num)+' '+ c +'s' + compl
        elif quant == 10:
            compl = ' e'
            return str(num)+' '+ d +'s' + compl
        else:
            return str(num)+' '+ u +'s'

num = int(input('Insira um numero menor que 1000: '))
cent = num//100
deze = (num%100)//10
unid = num%10

print(grafiaExtensso(cent,100), grafiaExtensso(deze,10), grafiaExtensso(unid,1))

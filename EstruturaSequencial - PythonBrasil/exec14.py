#Joao pescou 10 peixes de segintes pesos
peixes = [12, 54, 23, 50, 56, 2, 67, 78, 30, 50]

multa=0
for i in peixes:
	if i >= 50:
		multa = multa + 4.00
print(multa)
paisA, taxaA = int(input('Qual a população do pais A? ')), float(input('Qual a taxa de crecimento incial de A?'))
paisB, taxaB = int(input('Qual a população do pais B? ')), float(input('Qual a taxa de crecimento incial de B?'))
anos=0

while paisA <= paisB:
    paisA += paisA*(taxaA/100)
    paisB += paisB*(taxaB/100)
    anos += 1
print('A população do pais A ultrpassará a do pais B em aproximadamente', anos,'anos.')
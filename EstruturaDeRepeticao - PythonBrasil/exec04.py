paisA = 80000
paisB = 200000
cont = 0

while paisA <= paisB:
    paisA += (paisA*0.03)
    paisB += (paisB*0.015)
    cont += 1

print('Em', cont,'anos a população do pais A ultrapassará a do pais B')
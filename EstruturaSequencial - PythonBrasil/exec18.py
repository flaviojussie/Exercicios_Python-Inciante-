# programa que estima o tempo de download de um arquivo.
arquivo = 2000
link = 2

lim_max = (link*1024)/8
print (lim_max)
a = (lim_max/1024)
tempo = arquivo/a
min = int(tempo//60)
seg = int(tempo%60)

print ('Tempo de download eh:', min, 'minutos e', seg, 'segundos.')

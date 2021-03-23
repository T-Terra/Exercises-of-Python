#Desafio 024 verificar uma str no começo da frase
cidade = str(input('Em qual cidade você mora? ').strip())
#print('santo' in cidade)
print(cidade[:5].upper() == 'SANTO')



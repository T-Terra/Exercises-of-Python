#Desafio 31
distancia = float(input('\033[0;35mqual é a distância da sua viagem? '))
print('\033[0;31mVocê está prestes a começar uma viagem de {:.0f}km'.format(distancia))
preco = (distancia * 0.50)
preco2 = (distancia * 0.45)
if distancia <= 200:
    print('\033[0;35msua passagem custará \033[0;33mR${:.2f}'.format(preco))
else:
    print('\033[0;35msua passagem custará \033[0;33mR${:.2f}'.format(preco2))

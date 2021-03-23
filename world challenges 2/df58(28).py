palpite = 0
from random import randint
from time import sleep
pc = randint(0, 10)
print('\033[33m=' * 50)
print('\033[35mVou pensar em um número de 0 a 10 tente adivinhar!')
print('\033[33m=' * 50)
player = int(input('\033[30mQual foi o número que o PC escolheu? '))
print('PROCESSANDO...')
sleep(2)
while pc != player or pc > player or pc < player:
    if pc < player:
        player = int(input('Menos... Você tem mais um palpite: '))
    else:
        player = int(input('Mais... Você tem mais um palpite: '))
    print('PROCESSANDO...')
    sleep(2)
    palpite += 1
if pc == player:
    print('\033[34mVocê ganhou!!!')
print('\033[30mMas precisou de \033[34m{} \033[30mpalpites para vencer!'.format(palpite))
print('O PC escolheu o número {}'.format(pc))

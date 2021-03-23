#desafio 028
from random import randint
from time import sleep
pc = randint(0, 5)
#print(pc)
print('-=-' * 20)
print('VOU PENSAR EM UM NÚMERO DE 0 A 5 TENTE ADIVINHAR...')
print('-=-' * 20)
jogador = int(input('Qual número o computador escolheu? '))
print('PROCESSANDO...')
sleep(3)
if pc == jogador:
    print('Você venceu, Parabéns!!!')
else:
    print('Eu venci!!! eu pensei no número {} e não no número {}'.format(pc, jogador))

from random import randint
from time import sleep
print(10 * '\033[31m=', '\033[33mJOKENPÔ', 10 * '\033[31m=')
pc = randint(1, 3)
user = int(input('''\033[30mEscolha um...
[1] PEDRA
[2] PAPEL
[3] TESOURA
Qual é a jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
sleep(1)
if user == 1:
    print('você escolheu PEDRA!')
elif user == 2:
    print('Você escolheu PAPEL!')
elif user == 3:
    print('Você escolheu TESOURA!')
if user == pc:
    print('EMPATE!!! Os dois escolheram igual.')
elif user == 1 and pc == 2:
    print('O PC ganhou!!! Ele escolheu papel.')
elif user == 2 and pc ==3:
    print('O PC ganhou!!! Ele escolheu tesoura.')
elif user == 1 and pc == 3:
    print('Você ganhou!!! O PC escolheu tesoura.')
elif user == 2 and pc == 1:
    print('Você ganhou!!! O PC escolheu pedra.')
elif user == 3 and pc == 2:
    print('Você ganhou!!! O PC escolheu papel.')
else:
    print('\033[31mOpção incorreta tente novamente!')

#Desafio 030
num = int(input('\033[0;35mdigite um número: '))
resultado = num % 2
if resultado == 0:
    print('o número {} é \033[0;33mPAR!!!'.format(num))
else:
    print('o número {} é \033[0;33mÍMPAR!!!'.format(num))

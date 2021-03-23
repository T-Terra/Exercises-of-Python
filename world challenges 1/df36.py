#desafio 35
print('\033[0;33m-=' * 25)
print('\033[0;37mANALISADOR DE TRIÂNGULOS')
print('\033[0;33m-=' * 25)
r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas \033[0;36mPODEM \033[0;33mformar um TRIÂNGULO!!!')
else:
    print('As retas \033[0;31mNÃO \033[0;33mpodem formar um TRIÂNGULO!!!')


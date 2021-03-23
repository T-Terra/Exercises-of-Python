r = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da terceira reta: '))
if r < r2 + r3 and r2 < r3 + r and r3 < r + r2:
    print('\033[35mCom essas medidas podemos formar um triângulo.')
    if r == r2 == r3:
        print('\033[30mComo todos os lados são iguais isso forma um \033[36mEQUILÁTERO!')
    elif r != r2 != r3:
        print('\033[30mEssa figura tem todos os lados diferentes e é um \033[36mESCALENO!!!')
    else:
        print('\033[30mEssa figura tem dois lados iguais então é um \033[36mISÓSCELES!!')
else:
    print('\033[31mEssas medidas não podem formar um triângulo!')

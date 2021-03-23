from time import sleep
num = int(input('\033[30mDigite um valor: '))
num2 = int(input('\033[30mDigite outro valor: '))
r = 0
lista = [1, 2, 3, 4]
while r != 5:
    print('''    \033[34m[1] soma
    [2] multiplicar
    [3] maior 
    [4] novos números
    [5] sair do programa ''')
    r = int(input('\033[35mQual opção: '))
    if r == 1:
        soma = num + num2
        print('\033[30mA soma entre {} + {} é {}.'.format(num, num2, soma))
        print('-=' * 15)
    elif r == 2:
        mult = num * num2
        print('\033[30m{} X {} tem como resultado {}'.format(num, num2, mult))
        print('-=' * 15)
    elif r == 3:
        if num > num2:
            maior = num
        else:
            maior = num2
        print('\033[30mentre {} e {} o maior número é o {}'.format(num, num2, maior))
        print('-=' * 15)
    elif r == 4:
        print('\033[33minforme os valores novamente.')
        num = int(input('\033[30mDigite um valor: '))
        num2 = int(input('\033[30mdigite outro valor: '))
    elif r != lista and r != 5:
        print('\033[31mOpção inválida! tente novamente.')
print('\033[36mFINALIZANDO...')
sleep(2.5)
print('\033[33mPROGRAMA ENCERRADO.')


from time import sleep

def cont_c():
    print(20 * '-=')
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        sleep(0.5)
        print(f'{c}', end=' ')
    print('FIM!')
    print(20 * '-=')
    print('Contagem de 10 até 0 de 2 em 2')
    for d in range(10, 0 - 1, -2):
        sleep(0.5)
        print(f'{d}', end=' ')
    print('FIM!')
    print(20 * '-=')


# main program
cont_c()
from time import sleep

def cont_c(i, f, p):
    if p < 0:
        p *= -1 # for numbers negative||
    if p == 0:
        p = 1
    print(20 * '-=')
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM!')
print(20 * '-=')


# main program
cont_c(1, 10, 1)
cont_c(10, 0, 2)
print(20 * '-=')
print('Agora é sua vez de personalizar a contagem!')
init = int(input('Início: '))
finish = int(input('Fim: '))
step = int(input('Passo: '))
cont_c(init, finish, step)
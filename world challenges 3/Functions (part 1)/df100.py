from random import randint
from time import sleep

def draw():
    sum_list = []
    par = []
    cont = 0
    print(f'Sorteando 5 valores da lista: ', end='')
    while True:
        sleep(0.4)
        num = randint(0, 50)
        sum_list.append(num)
        if num % 2 == 0 and num not in sum_list:
            par.append(num)
        print(f'{num}', end=' ')
        if cont == 4:
            break
        cont += 1
    print('PRONTO!')
    print(f'Somando os valores pares de {sum_list}, temos {sum(par)}')
#def sum_v():
    

# main program
draw()
#sum_v()
from random import randint
from time import sleep

def draw():
    sum_list = []
    cont = sum_tot = 0
    print(f'Sorteando 5 valores da lista: ', end='')
    while True:
        sleep(0.4)
        num = randint(0, 50)
        sum_list.append(num)
        for v in sum_list:
            if v % 2 == 0:
                sum_tot += v
        print(f'{num}', end=' ')
        if cont == 4:
            break
        cont += 1
    print('PRONTO!')
    print(f'Somando os valores pares de {sum_list}, temos {sum_tot}')
#def sum_v():
    

# main program
draw()
#sum_v()
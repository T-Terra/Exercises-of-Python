from random import randint
from time import sleep
# function to sorted numbers
def numbers(mainlist):
    global cont
    for cont in range(0, 5):
        n = randint(1, 10)
        mainlist.append(n)
        print(f'{n}', end=' ')
        sleep(0.4)
    print('PRONTO!')

# function to sum 
def sum_tot(mainlist):
    sum_finish = 0
    for value in main_list:
        if value % 2 == 0:
            sum_finish += value
    print(f'Somando os valores pares de {main_list} , temos {sum_finish}')

# main program
cont = 5
print(f'Sorteando {cont} valores da lista:', end=' ')
main_list = []
numbers(main_list)
sum_tot(main_list)

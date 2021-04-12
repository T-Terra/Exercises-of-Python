from time import sleep

def bigger(*num):
    cont = bigger = 0
    print(30 * '-=')
    print('Analisando os valores passados...')
    for value in num:
        print(f'{value}', end=' ')
        sleep(0.4)
        if cont == 0:
            bigger = value
        else:
            if value > bigger:
                bigger = value
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior número informado foi {bigger}')
        
# main program
bigger(2, 9, 4, 5, 7, 1)
bigger(2, 5, 11, 6)
bigger(55, 101, 3)
bigger()
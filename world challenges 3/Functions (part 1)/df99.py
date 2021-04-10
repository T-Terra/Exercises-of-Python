from time import sleep

def bigger(*num):
    tam = len(num)
    max_n = max(num)
    for c in num:
        sleep(0.5)
        print(f'{c}', end=' ')
    if tam == max_n:
        
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior número informado foi {max_n}')
    print(30 * '-=')
        
# main program
print(30 * '-=')
print('Analisando os valores passados...')
bigger(2, 9, 4, 5, 7, 1)
bigger(2, 5, 11)
bigger()
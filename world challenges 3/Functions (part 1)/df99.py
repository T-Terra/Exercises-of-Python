from time import sleep

def bigger(*num):
    tam = len(num)
    print(num)
    print(f'Foram informados {tam} valores ao todo.')
        
# main program
print('Analisando os valores passados...')
sleep(1)
bigger(2, 9, 4, 5, 7, 1)
sleep(1)
bigger(2, 9)
from time import sleep
n1 = int(input('Digite o 1° termo: '))
razao = int(input('Razão: '))
cont = 1
termo = n1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        cont += 1
        termo += razao
    print('PAUSA')
    mais = int(input('\nVocê quer mostrar mais quantos termos dessa PA? '))
sleep(2.5)
print('A soma de todos os termos mostrados são de {} termos.'.format(total))
print('\033[33mFIM')


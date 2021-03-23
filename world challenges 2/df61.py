# minha solução
'''num = int(input('Digite o 1° termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao
c = num
while c <= decimo:
    print('{}'.format(c), end=' >> ')
    c += razao
print('\033[35mACABOU.')'''

# solução ideal com dois contadores
primeiro = int(input('Digite o 1° termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} >>'.format(termo), end=' ')
    termo += razao
    cont += 1
print('ACABOU.')




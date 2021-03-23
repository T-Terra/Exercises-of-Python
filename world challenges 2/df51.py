num = int(input('Digite o 1° termo: '))
razao = int(input('razão: '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print('{}'.format(c), end='--')
print('ACABOU')

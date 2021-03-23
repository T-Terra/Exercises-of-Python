print('\033[33m=' * 20)
num = int(input('\033[30mDigite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))

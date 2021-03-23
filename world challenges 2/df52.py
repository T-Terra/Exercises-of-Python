num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1 # vai pegar os números do conjunto C e ver quantos é divisivel pelo num
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[30mO total de divisores do número \033[34m{} \033[30mfoi de \033[34m{}'.format(num, total))
if total == 2: # vai pegar os números que tiver 2 divisores
    print('\033[30mE por isso ele é PRIMO!')
else:
    print('\033[30mE por isso ele NÃO É PRIMO.')

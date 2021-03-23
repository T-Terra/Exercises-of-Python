from random import randint
v = 0
print('=' * 30)
print('Vamos jogar PAR OU ÍMPAR...')
print('=' * 30)
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o PC {pc}. e o total é {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes.')

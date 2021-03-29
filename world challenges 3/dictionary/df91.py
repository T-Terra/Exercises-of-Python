from random import randint
from time import sleep
players = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}
for k, v in players.items():
    sleep(1)
    print(f'O {k} tirou {v}')
    sleep(1.2)
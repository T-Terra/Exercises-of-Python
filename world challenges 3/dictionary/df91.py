from random import randint
from time import sleep
from operator import itemgetter
players = {
    # parte 0     parte 1
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
for k, v in players.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('  ======= Ranking =======')
for i, values in enumerate(ranking):
    print(f'  {i+1}° lugar: {values[0]} com {values[1]}')
    sleep(1)
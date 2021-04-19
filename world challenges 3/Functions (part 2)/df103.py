def player_record(name='<desconhecido>', num_g=0):
    print(f'O jogador {name} fez {num_g} gol(s) no campeonato.')

# main program
name_player = str(input('Nome do jogador: '))
num_goals = str(input('Número de gols: '))
if num_goals.isnumeric():
    num_goals = int(num_goals)
else:
    num_goals = 0
if name_player.strip() == '':
    player_record(num_g=num_goals)
else:
    player_record(name_player, num_goals)
def player_record(name='', num_g=0):
    if name == '':
        return f'O jogador <desconhecido> fez {num_g} gol(s) no campeonato' 
    else:
        return f'O jogador {name} fez 0 gol(s) no campeonato.'
# main program
name_player = str(input('Nome do jogador: '))
num_goals = int(input('Número de gols: '))
print(player_record(name_player, num_goals))
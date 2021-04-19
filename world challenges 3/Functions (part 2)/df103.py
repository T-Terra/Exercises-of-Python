def player_record(name='', num_g=''):
    if name == '' and num_g == '':
        return f'O jogador <desconhecido> fez 0 gol(s) no campeonato'
    elif name == '' and len(num_g) > 0:
        return f'O jogador <desconhecido> fez {num_g} gol(s) no campeonato.'
    elif len(name) > 0 and len(num_g) == 0:
        return f'O jogador {name} fez 0 gol(s) no campeonato'
    else:
        return f'O jogador {name} fez {num_g} gol(s) no campeonato.'

# main program
name_player = str(input('Nome do jogador: '))
num_goals = str(input('Número de gols: '))
print(player_record(name_player, num_goals))
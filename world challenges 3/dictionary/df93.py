main_dict = dict()
goals = []

main_dict['name'] = str(input('Nome do jogador: '))
match = int(input(f'Quantas partidas {main_dict["name"]} jogou?: '))
for c in range(1, match + 1):
    goals.append(int(input(f'Quantos gols na partida {c}°: ')))
    main_dict['goals'] = goals[:]
    main_dict['tot'] = sum(goals)
print(30 * '-=')
print(main_dict)
print(30 * '-=')
for k, v in main_dict.items():
    print(f'O campo {k} tem o valor {v}')
print(30 * '-=')
print(f'O jogador {main_dict["name"]} jogou {match} partidas.')
for key, value in enumerate(goals):
    print(f'   => Na partida {key + 1}°, fez {value} gols.')
print(f'Foi um total de {sum(goals)} gols.')
main_dict = dict()
goals = []

main_dict['name'] = str(input('Nome do jogador: '))
match = int(input(f'Quantas partidas {main_dict["name"]} jogou?: '))
for c in range(1, match + 1):
    num = int(input(f'Quantos gols na partida {c}°: '))
    goals.append(num)
    main_dict['goals'] = goals
    main_dict['tot'] = sum(goals)
print(30 * '-=')
print(main_dict)
print(30 * '-=')
for k, v in main_dict.items():
    print(f'O campo {k} tem o valor {v}')
print(30 * '-=')

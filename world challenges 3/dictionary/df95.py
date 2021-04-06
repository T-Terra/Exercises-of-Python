main_dict = dict()
goals = list()
list_m = list()
while True:
    main_dict.clear()
    main_dict['name'] = str(input('Nome do jogador: '))
    match = int(input(f'Quantas partidas {main_dict["name"]} jogou?: '))
    for c in range(1, match + 1):
        goals.append(int(input(f'Quantos gols na partida {c}°: ')))
        main_dict['goals'] = goals[:]
        main_dict['tot'] = sum(goals)
    goals.clear()
    list_m.append(main_dict.copy())
    while True:
        response = str(input('Quer continuar? [S/N] ')).upper()[0]
        if response in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if response == 'N':
        break
print(30 * '-=')
print(f'cod  nome          gols         total')
print(30 * '-')
for i, v in enumerate(list_m):
    print(f' {i:<3} {v["name"]} {v["goals"]} {v["tot"]}')
print(30 * '-')

# Fazer a opção de ver dados de jogadores separadamente
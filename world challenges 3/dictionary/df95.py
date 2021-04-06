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
# Faz o cabeçalho
print(f'cod ', end='')
for i in main_dict.keys():
    print(f'{i:<15}', end='')
print()
print(40 * '-')
for i, v in enumerate(list_m):
    print(f' {i:<3}', end='')
    for val in v.values():
        print(f'{str(val):<15}', end='')
    print()
print(40 * '-')
while True:
    date_player = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if date_player == 999:
        break
    if date_player >= len(list_m):
        print(f'ERRO! Não existe jogador com o código {date_player}.')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {v["name"]}: ')
        for i, g in enumerate(list_m[date_player]["goals"]):
            print(f'   No jogo {i+1}° fez {g} gols.')
        print(40 * '-')
print('Volte sempre!')
# Fazer a opção de ver dados de jogadores separadamente
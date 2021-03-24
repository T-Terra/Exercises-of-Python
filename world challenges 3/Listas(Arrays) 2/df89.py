from time import sleep
main_list = []
response = 'S'

while response == 'S':
    name = str(input('Nome: '))
    note1 = float(input('Nota 1: '))
    note2 = float(input('Nota 2: '))
    media = (note1 + note2) / 2
    main_list.append([name, [note1, note2], media])
    response = str(input('Quer continuar? [S/N]: '))[0].upper()
print(30 * '-=')
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print(30 * '_')
for i, a in enumerate(main_list):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print(35 * '-')
    menu = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if menu == 999:
        print('Finalizando...')
        sleep(2)
        break
    elif menu <= len(main_list) -1:
        print(f'Notas de {main_list[menu][0]} são {main_list[menu][1]}')
print('Volte sempre!!!')
    
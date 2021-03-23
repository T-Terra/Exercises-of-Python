main_list = [[], [], []]
response = 'S'

while response == 'S':
    name = str(input('Nome: '))
    note1 = float(input('Nota 1: '))
    note2 = float(input('Nota 2: '))
    response = str(input('Quer continuar? [S/N] '))[0].upper()

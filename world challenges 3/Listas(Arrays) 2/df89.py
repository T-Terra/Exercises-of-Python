main_list = [[], []]
response = 'S'

while response == 'S':
    name = str(input('Nome: '))
    note1 = float(input('Nota 1: '))
    note2 = float(input('Nota 2: '))
    response = str(input('Quer continuar? [S/N]: '))[0].upper()
    main_list[0].append(name)
    main_list[1].append(note1)
    main_list[1].append(note2)
    media = sum(main_list[1]) / len(main_list[1]) # sum --> the sum of all items divided by the size of the array
    for k, v in enumerate(main_list[0]):
        print(20 * '-=')
        print(f'NO.  NOME       MEDIA')
        print(f'{k}    {v}     {media}')
        print(15 * '-')
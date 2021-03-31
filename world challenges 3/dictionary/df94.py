main_dict = {}
cont = 0
average = []
people = []
genre = []
while True:
    people.append(str(input('Nome: ')))
    main_dict['name'] = people
    genre.append(str(input('Sexo: [M/F] '))[0].upper())
    main_dict['genre'] = genre
    average.append(int(input('Idade: ')))
    m = sum(average) / len(average)
    main_dict['age'] = average
    cont += 1
    response = str(input('Quer continuar? [S/N] '))[0].upper()
    if response == 'N':
        break
print(30 * '-=')
print(main_dict)
print(f'  - O grupo tem {cont} pessoas.')
print(f'  - A média de idade é de {m} anos.')
#print(f'  - As mulheres cadastradas foram:')


            
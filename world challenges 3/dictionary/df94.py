people = {}
crowd = []
added = average = 0 

while True:
    people.clear()
    people['name'] = str(input('Nome: '))
    while True:
        people['genre'] = str(input('Sexo: [M/F] ')).upper()[0]
        if people['genre'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    people['age'] = int(input('Idade: '))
    added += people['age']
    crowd.append(people.copy())
    while True:
        response = str(input('Quer continuar? [S/N] ')).upper()[0]
        if response in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if response == 'N':
        break
print(30 * '-=')
print(f'A) Ao todo temos {len(crowd)} pessoas cadastradas.')
average = added / len(crowd)
print(f'B) A média de idade é de {average:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in crowd:
    if p['genre'] in 'Ff':
        print(f'{p["name"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in crowd:
    if p['age'] >= average:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
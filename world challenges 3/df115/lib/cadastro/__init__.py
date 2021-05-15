def cadastro():
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    print(f'Novo registro de {name} adicionado.')
    with open('registros.txt', 'a') as file:
        name = file.write(f'{name} ')
        age = file.write(str(f'{age} anos\n'.strip()))
def mostra_p():
    with open('registros.txt', 'r') as file:
        for content in file:
            print(f'{content}')
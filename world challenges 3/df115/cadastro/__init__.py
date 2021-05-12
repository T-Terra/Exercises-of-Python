def title(msg):
    print(50 * '-')
    print(f'{msg}'.center(50))
    print(50 * '-')

def menu(msg):
    print(f'{msg}')
    print(50 * '-')

def cadastro():
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    print(f'Novo registro de {name} adicionado.')
    with open('registros.txt', 'a') as file:
        name = file.write(f'{name} ')
        age = file.write(str(f'{age} anos\n'.rjust(35)) )
def mostra_p():
    with open('registros.txt', 'r') as file:
        for content in file:
            print(end='')
            print(f'{content}')

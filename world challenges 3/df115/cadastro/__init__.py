from os import terminal_size


def title(msg):
    tam = len(msg) + 24
    print(tam * '-')
    print(f'{msg}'.center(tam))
    print(tam * '-')

def menu(msg):
    tam = len(msg) - 91
    print(f'{msg}')
    print(tam * '-')

def cadastro():
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    print(f'Novo registro de {name} adicionado.')
    with open('registros.txt', 'a') as file:
        name = file.write(f'{name} ')
        age = file.write(str(f'{age} \n'))
        
    #with open('registros.txt', 'r') as file:


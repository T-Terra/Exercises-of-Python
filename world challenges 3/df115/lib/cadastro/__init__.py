def cadastro():
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    print(f'Novo registro de {name} adicionado.')
    with open('registros.txt', 'a') as file:
        name = file.write(f'{name} ')
        age = file.write(str(f'{age} anos\n'.rjust()))

def mostra_p():
    with open('registros.txt', 'r') as file:
        for content in file:
            print(content)

def fileexist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def create_file(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!! ')
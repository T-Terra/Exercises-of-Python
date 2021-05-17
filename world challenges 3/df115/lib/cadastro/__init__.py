from df115.lib.interface import *

def cadastro(arq, name='desconhecido', age=0):
    try:
        file = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            file.write(f'{name};{age}\n')
        except:
            print('Houve um ERRO na hora de escrever no arquivo.')
        else:
            print(f'Novo registro de {name} adicionado.')
            file.close()


def mostra_p(name):
    try:
        a = open(name, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        title('PESSOAS CADASTRADAS')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos') 
    finally:
        a.close()

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
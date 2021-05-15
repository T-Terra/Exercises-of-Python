def cadastro():
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    print(f'Novo registro de {name} adicionado.')
    with open('registros.txt', 'a') as file:
        name = file.write(f'{name} ')
        age = file.write(str(f'{age} anos\n'.rjust(35).strip()))
def mostra_p():
    with open('registros.txt', 'r') as file:
        for content in file:
            print(f'{content}')



    """try:
        resp = int(input('\33[33m''Sua opção: ''\33[0m'))
    except (ValueError, TypeError):
        print('\33[31m''ERRO! Digite um número inteiro válido.''\33[0m')
        continue
    except (KeyboardInterrupt):
        print('\33[31m''\nO usuário preferiu não informar os dados''\33[0m')
        title('Saindo do sistema... Até logo!')
        break
    else:
        if resp == 1:
            title('PESSOAS CADASTRADAS')
            mostra_p()
        elif resp == 2:
            title('NOVO CADASTRO')
            cadastro()
        elif resp == 3:
            title('Saindo do sistema... Até logo!')
            break
        elif resp > 3:
            print('\33[31m''ERRO! Digite uma opção válida!''\33[0m')"""

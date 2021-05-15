def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31m''ERRO! Digite um número inteiro válido.''\33[0m')
            continue
        except (KeyboardInterrupt):
            print('\33[31m''\nO usuário preferiu não informar os dados''\33[0m')
            return 0
        else:
            return n

def line(tam = 42):
    return '-' * tam

def title(txt):
    print(line())
    print(f'{txt}'.center(42))
    print(line())

def menu(array):
    title('MENU PRINCIPAL')
    count = 1
    for item in array:
        print(f'\33[33m{count}\33[0m - \33[34m{item}\33[0m')
        count += 1
    print(line())
    opc = readint('\33[32mSua opção: \33[0m')
    return opc
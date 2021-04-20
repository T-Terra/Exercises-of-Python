def write(msg):
    tam = len(msg) + 4
    print(tam * '~')
    print(f'  {msg}')
    print(tam * '~')
def terminal():
    from time import sleep
    write('Sistema de ajuda PYhelp')
    while True:
        response = str(input('Função ou Biblioteca > '))
        if response != 'fim':
            sleep(1)
            write(f'Acessando o manual do comando "{response}"')
            sleep(1.5)
        else:
            break

# main program
terminal()
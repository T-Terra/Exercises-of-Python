from time import sleep
c = ('\033[m', # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m'     # 6 - branco
);

def terminal(com):
    sleep(1)
    write(f'Acessando o manual do comando \'{com}\'', 4)
    sleep(1.5)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def write(msg, color=0):
    tam = len(msg) + 4
    print(c[color], end='')
    print(tam * '~')
    print(f'  {msg}')
    print(tam * '~')
    print(c[0], end='')
    

# main program
response = ''
while True:
    write('Sistema de ajuda PYhelp', 3)
    response = str(input('Função ou Biblioteca > '))
    if response.upper() == 'FIM':
        break
    else:
        terminal(response)
write('Até logo!!', 1)
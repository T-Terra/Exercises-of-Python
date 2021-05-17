from df115.lib.interface import *
from df115.lib.cadastro import *
from time import sleep

arq = 'registros.txt'
if not fileexist(arq):
    create_file(arq)

# main program
while True:
    resp = menu(['Listar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        title('PESSOAS CADASTRADAS')
        mostra_p()
    elif resp == 2:
        title('CADASTRANDO NOVA PESSOA')
        cadastro()
    elif resp == 3:
        title('Saindo do sistema... Até logo!')
        break
    else:
        print('\33[31m''ERRO! Digite uma opção válida!''\33[0m')
    sleep(1.5)

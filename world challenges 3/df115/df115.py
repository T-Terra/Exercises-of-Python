from cadastro import title, menu, cadastro

# main program
title('MENU PRINCIPAL')
menu('\33[33m''1''\33[0m'' - ''\33[34m''Ver pessoas cadastradas''\33[0m'' \n''\33[33m''2''\33[0m'' - ''\33[34m''Cadastrar nova pessoa''\33[0m'' \n''\33[33m''3''\33[0m'' - ''\33[34m''Sair do sistema''\33[0m''')
resp = int(input('Qual é sua opção: '))
if resp == 2:
    cadastro()
from cadastro import title, menu
c = ('\033[m', # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m'     # 6 - branco
);

# main program
title('MENU PRINCIPAL')
menu('\33[33m''1''\33[0m'' - ''\33[34m''Ver pessoas cadastradas''\33[0m'' \n''\33[33m''2''\33[0m'' - ''\33[34m''Cadastrar nova pessoa''\33[0m'' \n''\33[33m''3''\33[0m'' - ''\33[34m''Sair do sistema''\33[0m''')
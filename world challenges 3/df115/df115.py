from cadastro import title, menu, cadastro, mostra_p

# main program
while True:
    title('MENU PRINCIPAL')
    menu('\33[33m''1''\33[0m'' - ''\33[34m''Ver pessoas cadastradas''\33[0m'' \n''\33[33m''2''\33[0m'' - ''\33[34m''Cadastrar nova pessoa''\33[0m'' \n''\33[33m''3''\33[0m'' - ''\33[34m''Sair do sistema''\33[0m''')
    try:
        resp = int(input('\33[33m''Sua opção: ''\33[0m'))
    except (ValueError, TypeError):
        print('\33[31m''ERRO! Digite um número inteiro válido.''\33[0m')
        continue
    except (KeyboardInterrupt):
        print('\33[31m''\nO usuário preferiu não informar os dados''\33[0m')
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
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

def readfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31m''ERRO! Digite um número real válido.''\33[0m')
            continue
        except (KeyboardInterrupt):
            print('\33[31m''\nO usuário preferiu não informar os dados''\33[0m')
            return 0
        else:
            return n

# main program
numb = readint('Digite um número inteiro: ')
numbfloat = readfloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {numb} e o número real {numbfloat}')
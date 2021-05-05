def readint(msg=0):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        try:
            value = int(n)
            ok = True
        except (ValueError, TypeError):
            print('\33[31m''ERRO! Digite um número inteiro válido.''\33[0m')
        except KeyboardInterrupt:
            print('\33[31m''O usuário preferiu não informar os dados''\33[0m')
        if ok:
            break
    return value

def readfloat(msg=0):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        try:
            value = float(n)
            ok = True
        except (ValueError, TypeError):
            print('\33[31m''ERRO! Digite um número real válido.''\33[0m')
        except KeyboardInterrupt:
            print('\33[31m''O usuário preferiu não informar os dados''\33[0m')
        if ok:
            break
    return value

# main program
numb = readint('Digite um número inteiro: ')
numbfloat = readfloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {numb} e o número real {numbfloat}')
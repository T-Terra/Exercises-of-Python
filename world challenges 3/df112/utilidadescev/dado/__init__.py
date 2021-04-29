def readmoney(text):
    while True:
        p = str(input(text)).strip()
        if p == '':
            print('\033[31m ERRO! "" não é um preço inválido!\033[0m')
        elif not p.isnumeric():
            print(f'\033[31m ERRO! {p} não é um preço inválido!\033[0m')
        if p.isnumeric():
            return p.isnumeric()
            break

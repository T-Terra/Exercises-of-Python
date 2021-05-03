def readmoney(text):
    while True:
        p = str(input(text)).strip().replace(',', '.')
        if p.isalpha() or p == "":
            print(f'\033[31m ERRO! \"{p}\" não é um preço válido!\033[0m')
        else:
            return float(p)
            break
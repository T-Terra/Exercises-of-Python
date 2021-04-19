def readint(n=0):
    print(30 * '-')
    n = str(input(n))
    if n.isnumeric():
        return n
    while n.strip() == '' or n.isalpha():
        print('\33[31m''ERRO! Digite um número válido.''\33[0m')
        n = str(input('Digite um número: '))
    return n


# main program
numb = readint('Digite um número: ')
print(f'Você acabou de digitar o número {numb}')
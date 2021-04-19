## old solution ##
"""def readint(n=0):
    print(30 * '-')
    n = str(input(n))
    if n.isnumeric():
        return n
    while n.strip() == '' or n.isalnum():
        print('\33[31m''ERRO! Digite um número válido.''\33[0m')
        n = str(input('Digite um número: '))
        if n.isnumeric():
            return n"""
## old solution ##

def readint(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\33[31m''ERRO! Digite um número válido.''\33[0m')
        if ok:
            break
    return value



# main program
numb = readint('Digite um número: ')
print(f'Você acabou de digitar o número {numb}')
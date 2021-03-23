num = int(input('Digite um número inteiro: '))
print('\033[30mEscolha uma das bases para conversão:')
print('\033[36m[1] \033[30mconverter para \033[33mbinário')
print('\033[36m[2] \033[30mconverter para \033[33moctal')
print('\033[36m[3] \033[30mconverter para \033[33mhexadecimal')
escolhido = int(input('\033[30mSua escolha: '))
if escolhido == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif escolhido == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif escolhido == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mação incorreta!')

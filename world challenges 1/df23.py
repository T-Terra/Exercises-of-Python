#desafio 22
nome = input('digite seu nome completo: ').strip()
print('analisando seu nome...')
print('seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('seu nome com letras minúsculas é {}'.format(nome.lower()))
print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


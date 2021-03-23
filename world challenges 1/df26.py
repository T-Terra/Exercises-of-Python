#Desafio 025 verifica em qualquer parte da str
nome = str(input('Qual é seu nome? ')).strip()
print('seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

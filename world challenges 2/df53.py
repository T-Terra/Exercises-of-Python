frase = str(input('Digite uma frase: ')).strip().upper()
#desconsiderando os espaços
palavras = frase.split()
junto = ''.join(palavras)
#pegar a frase(junto) de trás para frente
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um POLíNDROMO!')
else:
    print('não temos um políndromo!')



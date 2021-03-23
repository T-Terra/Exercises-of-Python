lista_nuns = [] # Também posso criar um array com list()
continua = 'S'

while continua == 'S':
    n = int(input('Digite um valor: '))
    if n not in lista_nuns:
        lista_nuns.append(n)
        print('Valor adicionado com sucesso...') 
    elif lista_nuns == lista_nuns:
        print('Número duplicado! não vamos adiciona-lo na lista.')
    continua = str(input('Quer continuar? [S/N]: ')).upper()[0]
lista_nuns.sort() # ordena a lista crescente
print(15*'-=')
print(f'Você digitou os valores {lista_nuns}')

# código antigo com bug

'''lista_nuns = []
continua = 'S'

while continua == 'S':
    if lista_nuns not in lista_nuns:
        lista_nuns.append(int(input('Digite um valor: ')))
        print('Valor adicionado com sucesso...') 
    elif lista_nuns == lista_nuns:
        print('Número duplicado! não vamos adiciona-lo na lista.')
    continua = str(input('Quer continuar? [S/N]: ')).upper()[0]
print(15*'-=')
print(f'Você digitou os valores {lista_nuns}')'''

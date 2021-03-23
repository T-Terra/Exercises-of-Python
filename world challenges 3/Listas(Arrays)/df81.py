lista = []

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N]: ')).upper()[0]
print(30 * '-=')
print(f'Foram digitados {len(lista)} elementos.')
print(f'A lista ordenada de forma decrescente é {sorted(lista, reverse=True)}')
if 5 not in lista:
    print('O número 5 não foi encontrado na lista!')
else:
    print('O número 5 faz parte da lista.')


# Solução Gustavo Guanabara

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(30 * '-=')
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não foi encontrado na lista!')
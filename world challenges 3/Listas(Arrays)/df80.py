lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    '''if len(lista) == 0 or max(lista) <= n:
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    elif min(lista) >= n:
        lista.insert(0, n)
        print('Valor adicionado na posição 0...')
    elif min(lista) <= n:
        lista.insert(1, n)
        print('Valor adicionado na posição 1...')'''

# Resolução Gustavo Guanabara 

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}...')
                break
            pos += 1
print(30 * '-=')
print(f'Os valores digitados em ordem foram {lista}')
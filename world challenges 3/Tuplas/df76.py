produtos = ('Lapis', 1.75, 'Caderno', 5.50, 'Borracha', 1.10, 'Estojo', 7.50, 'Transferidor', 3.60, 'Compasso', 9.99, 'Mochila', 120.99, 'Canetas', 22.30, 'Livro', 34.90)

print(40*'=')
print(f'{"LISTAGEM DE PRECOS":^40}')
print(40*'=')

for c in produtos:
    index = produtos.index(c)
    if index % 2 == 0:
        print(f'{produtos[index]:.<30}', end='')
    elif index % 2 == 1:
        print(f'R$ {produtos[index]:.2f}')
    

print(40*'=')

# Resolução Gustavo Guanabara


print(40*'=')
print(f'{"LISTAGEM DE PRECOS":^40}')
print(40*'=')

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f' R$ {produtos[pos]:.2f}')

print(40*'=')
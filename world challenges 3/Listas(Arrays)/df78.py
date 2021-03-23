lista = []
# laço usando o método append para adicionar a lista
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
print(35*'=')
# printa a lista 
print(f'Você digitou os valores {lista}')
# mostra o maior número da lista 
print(f'O maior valor digitado é {max(lista)} nas posições', end=' ')
# acha o indice dos maiores números
for c, val in enumerate(lista):
    if val == max(lista):
        print(f'{c:.<4}', end=' ')
print()
# mostra o menor número da lista 
print(f'O menor valor digitado é {min(lista)} nas posições', end=' ')
# acha o indice dos menores números
for c, val in enumerate(lista):
    if val == min(lista):
        print(f'{c:.<4}', end=' ')
print()
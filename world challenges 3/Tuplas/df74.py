from random import randint
# Coloca os números aleatórios em uma tupla 
num_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# Usa o método sorted para ordenar a tupla decrescente
tupla_ordenada = sorted(num_aleatorios, reverse=True)

print('Os valores sorteados foram: ', end='')
for n in num_aleatorios:
    print(f'{n} ', end='')

# Pega o maior e o menor pelo index que já foi ordenado 
print(f'\nO maior número é {tupla_ordenada[0]}')
print(f'O menor número é {tupla_ordenada[4]}')


# Solução Gustavo Guanabara

# Usa o método max/min para determinar o maior e menor da tupla
print(f'\nO maior número é {max(num_aleatorios)}')
print(f'O menor número é {min(num_aleatorios)}')

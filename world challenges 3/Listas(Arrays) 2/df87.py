matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma = terceira_c = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número [{l}, {c}]: '))
        # soma os números pares
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        # soma a terceira coluna
        if matriz[l][2]:
           terceira_c += matriz[l][2]
        # Qual é o maior da 2° linha
        if c == 0:
            maior = matriz[1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
print(20*'-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c] :^5}]', end='')
    print()
print(20*'-=')

print(f'A soma dos números pares é {soma}.')
print(f'A soma dos números da terceira coluna é {terceira_c}.')
print(f'O maior número na 2° linha é o {maior}.')

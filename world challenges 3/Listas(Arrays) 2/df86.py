matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Redefine os valores dentro da matriz

# 2 for para alimentar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número [{l}, {c}]'))
print(30*'=-')
# 2 for para mostrar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

# Solução Guanabara
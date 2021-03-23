principal = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}° Número: '))
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)
principal[0].sort()
principal[1].sort()
print(30 * '-=')
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores ímpares digitados foram: {principal[1]}')

# Resolução Gustavo Guanabara

# n = 0

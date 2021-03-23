lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if r in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(30 * '-=')
print(f'Esta é a lista inteira {lista}')
print(f'A lista de pares são {pares}')
print(f'A lista de ímpares são {impares}')
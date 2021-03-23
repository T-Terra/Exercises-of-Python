lista = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(lista) == 0: # verificar o maior e menor
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if r == 'N':
        break
print(30 * '-=')
print(f'No total foram {len(lista)} pessoas cadastradas.')
print(f'O maior peso foi de {maior}kg', end=' ')
for p in lista: # laço para entrar no array 
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}kg', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()

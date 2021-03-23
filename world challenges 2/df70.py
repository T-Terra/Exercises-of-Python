print('--' * 10)
print('Supermercado Gabs')
print('--' * 10)
soma = maismil = menor = cont = barato = 0
while True:
    nomep = ' '
    preco = ' '
    continuar = ' '
    while continuar not in 'N':
        nomep = str(input('Nome do produto: '))
        preco = float(input('Preço:R$'))
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        soma += preco
        if preco > 1000:
            maismil += 1
        cont += 1
        if cont == 1 or preco < menor:
            menor = preco
            barato = nomep
    break
print(f'O total das suas compras foi de R${soma:.2f}')
print(f'{maismil} produtos custam mais de R$1000.00 reais')
print(f'O produto mais barato é o {barato} que custa R${menor:.2f}')

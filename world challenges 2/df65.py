r = 'Ss'
soma = quant = media = maior = menor = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média deles é de {}'.format(quant, media))
print('E o maior número é {} e o menor é {}'.format(maior, menor))

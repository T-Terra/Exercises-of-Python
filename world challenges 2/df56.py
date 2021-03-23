soma = 0
maior = 0
nomehvelho = ''
mulher = 0
for pess in range(1, 5):
    print('========== {}° Pessoa =========='.format(pess))
    nome = str(input('Qual é seu nome? ')).strip().upper().capitalize()
    idade = int(input('qual é sua idade? '))
    sexo = str(input('sexo [M/F]: ')).strip()
    if idade % 2 == 0:
        soma += idade
    else:
        soma += idade
    if pess == 1 and sexo in 'Mm':
        maior = idade
        nomehvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomehvelho = nome
    elif sexo in 'Ff' and idade < 20:
        mulher += 1
a = soma / 4
print('A média de idade das 4 pessoas é de {:.1f} anos'.format(a))
print('O Homem mais velho tem {:.0f} anos e é o {}'.format(maior, nomehvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))

print('=-' * 10)
print('Cadastro de pessoas')
print('=-' * 10)
pess = homens = mulher = 0
while True:
    print('=' * 30)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        print('=' * 30)
    if idade >= 18:
        pess += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{pess} pessoas tem mais de 18 anos, \n{homens} Homens foram cadastrados e \n{mulher} mulheres tem menos de 20 anos.')



maior = 0
menor = 0
from datetime import date
for c in range(1, 8):
    nasc = int(input('Qual é o ano de nascimento da {}° pessoa? '.format(c)))
    atual = date.today().year - nasc
    if atual >= 21:
        maior += 1
    elif atual <= 21:
        menor += 1
print('\033[34m{} \033[30mpessoas são maior de idade e \n\033[34m{} \033[30mpessoas são menor de idade.'.format(maior, menor))

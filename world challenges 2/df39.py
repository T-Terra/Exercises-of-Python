from datetime import date
sexo = input('Qual é seu sexo? ').upper()
ano = int(input('Em que ano você nasceu? '))
a = date.today().year - ano
print('Quem nasceu em {} tem {} anos em 2020.'.format(ano, a))
if a < 18 :
    print('O você ainda irá se alistar!')
    falta = 18 - a
    print('Ainda faltam {} anos para se alistar.'.format(falta))
    print('Você irá se alistar no ano de {}'.format(ano + 18))
elif a == 18:
    print('Está na hora de se alistar!!!')
elif a > 18:
    print('Você já passou do tempo de se alistar.')
    atraso = a - 18
    print('Você está atrasado {} anos'.format(atraso))
    print('Seu alistamento foi no ano {}'.format(ano + 18))
else:
    if sexo == 'F':
        print('você não precisa se alistar.')

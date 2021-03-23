#desafio 32
from datetime import date
ano = int(input('que ano você quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[0;30mO ano \033[0;33m{} \033[0;30mé bissexto!'.format(ano))
else:
    print('\033[0;30mo ano \033[0;33m{} \033[0;30mnão é bissexto!'.format(ano))

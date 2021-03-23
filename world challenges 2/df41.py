from datetime import date
nasc = int(input('Em que ano você nasceu? '))
print('De acordo com o ano que você nasceu...')
m = date.today().year - nasc
if m <= 9:
    print('Você tem {} anos e está na categoria MIRIM!'.format(m))
elif m <= 14:
    print('Você tem {} anos e está na categoria INFANTIL!'.format(m))
elif m <= 19:
    print('Você tem {} anos e está na categotia JUNIOR!'.format(m))
elif m <= 20:
    print('Você tem {} anos e está na categoria SÊNIOR!!!'.format(m))
elif m > 20:
    print('Você tem {} anos e está na categoria \033[36mMASTER!!!'.format(m))


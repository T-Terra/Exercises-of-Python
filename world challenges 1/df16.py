# DESAFIO 15
dia = float(input('quanros dias alugados? '))
km = float(input('quantos km rodados? '))
total = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))

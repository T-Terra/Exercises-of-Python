print('==== DESAFIO 12 ====')
valor = float(input('valor do produto:R$ '))
d = valor - (valor * 5/100)
vinte = valor - (valor * 20/100)
print('valor do produto é de R${:.2f}, mas com 5% de desconto vai para R${:.2f}'.format(valor, d))
print('e com 20% de desconto vai para R${:.2f}'.format(vinte))
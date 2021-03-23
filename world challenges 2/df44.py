print(10 * '\033[31m=', '\033[33mLOJAS TERRA', 10 * '\033[31m=')
preco = float(input('\033[30mQual é o valor do produto? R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista no dinheiro/cheque
[2] à vista no cartão 
[3] parcelado 2X no cartão 
[4] parcelado 3X ou mais no cartão ''')
pagamento = int(input('Qual é a forma de pagamento? '))
if pagamento == 1:
    desconto_10 = preco - (preco * 10 / 100)
    print('À vista no dinheiro ou cheque tem 10% de desconto e sairá \033[34mR${:.2f}'.format(desconto_10))
elif pagamento == 2:
    desconto_5 = preco - (preco * 5 / 100)
    print('À vista no cartão tem 5% de desconto e sairá \033[34mR${:.2f}'.format(desconto_5))
elif pagamento == 3:
    parcelamento = preco / 2
    print('''Sua compra será parcelado em 2x de R${:.2f} SEM JUROS 
Sua compra de {:.2f} vai custar \033[34mR${:.2f}'''.format(parcelamento, preco, preco))
elif pagamento == 4:
    parcelamento = int(input('Quantas parcelas? '))
    juros_20 = preco + (preco * 20 / 100)
    divi = juros_20 / parcelamento
    print('com o parcelamento em {}X de R${:.2f} com juros'.format(parcelamento, divi))
    print('Sua compra de R${:.2f} com 20% de juros vai custar \033[34mR${:.2f}'.format(preco, juros_20))
else:
    print('\033[31mOPÇÃO ERRADA! TENTE NOVAMENTO.')

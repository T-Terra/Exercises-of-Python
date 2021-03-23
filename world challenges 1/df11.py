print('==== DESAFIO 10 ====')
money = float(input('quanto dinheiro você tem? R$ '))
#d = money / 3.27
d = money / 4.07
e = money / 4.54
l = money / 5.32
print('R${:.2f} reais são\nUS${:.2f} dolares e \nEUR{:.2f} euros \n£{:.2f} libras esterlinas '.format(money, d, e, l))
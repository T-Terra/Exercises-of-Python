# DESAFIO 017 cálculo de hipotenusa
from math import hypot
o = float(input('qual é a medida do cateto oposto? '))
a = float(input('qual é a medida do cateto adjacente? '))
h = hypot(o, a)
print('a hipotenusa desse triângulo retângulo é {:.2f}'.format(h))

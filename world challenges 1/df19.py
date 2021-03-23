# desafio 18
from math import sin, cos, tan, radians
angulo = float(input('digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('o ângulo de {:.2f} tem o seno de {:.2f}'.format(angulo, seno))
print('o ângulo de {:.2f} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('o ângulo de {:.2f} tem a tangente de {:.2f}'.format(angulo, tangente))

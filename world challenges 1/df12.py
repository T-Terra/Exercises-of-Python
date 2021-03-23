print('==== DESAFIO 11 ====')
altura = float(input('qual é a altura? '))
base = float(input('qual é a largura? '))
s = base * altura
t = s / 2
print('sua parede tem a dimensão de {}x{} e sua área é de {}m².\npara pintar essa parede, você precisará de {}l de tinta'.format(altura, base , s, t))

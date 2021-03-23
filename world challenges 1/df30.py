#desafio 029
velocidade = float(input('qual é a velocidade atual do carro? '))
if velocidade <= 80:
  print('\033[0;33mtenha um bom dia e dirija com segurança!')
else:
    multa = (velocidade - 80) * 7
    print('\033[0;31mMULTADO! você excedeu o limite permitido que é de 80km/h')
    print('\033[0;31Você deve pagar uma multa de \033[0;33mR${:.2f}!'.format(multa))
    print('\033[0;33mtenha um bom dia e dirija com segurança!')

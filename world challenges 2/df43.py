altura = float(input('Qual é sua altura? (m) '))
peso = float(input('Qual é seu peso? (kg) '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Seu imc é de {:.1f} você está \033[31mabaixo do peso!!!'.format(imc))
elif imc <= 25:
    print('Seu imc é {:.1f} e você está no \033[33mPeso ideal!!!'.format(imc))
elif imc < 30:
    print('Seu imc é de {:.1f} e você está com \033[31mSOBREPESO!!!'.format(imc))
elif imc < 40:
    print('Seu imc é de {:.1f} e você está com \033[31mOBESIDADE!!'.format(imc))
elif imc >= 40:
    print('Seu imc é de {:.1f} e você está com \033[31mOBESIDADE MÓRBIDA!!!'.format(imc))

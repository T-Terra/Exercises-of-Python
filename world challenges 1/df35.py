#desafio 34
salario = float(input('digite seu salário: R$'))
n = salario + (salario * 10 / 100)
n2 = salario + (salario * 15 / 100)
if salario >= 1250:
    print('\033[0;35mseu salário com mais 10% de aumento é \033[0;33mR${:.2f}'.format(n))
if salario <= 1250:
    print('\033[0;35mseu salário com mais 15% de aumento é \033[0;33mR${:.2f}'.format(n2))

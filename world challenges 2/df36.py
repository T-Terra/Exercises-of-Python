casa = float(input('qual é o valor da casa? R$'))
salario = float(input('qual é o valor do seu salário? R$ '))
tempo = int(input('em quantos anos ou meses pretende pagar? '))
parcelas = casa / (tempo * 12)
trinta = 30 / 100 * salario
print('para pagar uma casa de \033[36mR${:.2f} em \033[33m{:.0f} anos'.format(casa, tempo))
print('\033[30mvocê terá uma parcela no valor de \033[34mR${:.2f}'.format(parcelas))
if parcelas <= trinta:
    print('\033[33mempréstimo concedido!')
else:
    print('\033[31mempréstimo negado!!!')

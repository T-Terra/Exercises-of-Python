despesas = {}
list_despesas = []
soma = sobra = 0
salario = float(input('Qual seu salário: R$ '))
while True:
    despesas.clear()
    d = str(input('Quais são suas despesas? '))
    value = float(input('Valor: R$ '))
    response = str(input('Quer continuar? [S/N] '))[0].upper()
    despesas['despesa'] = d
    despesas['valor'] = value
    list_despesas.append(despesas.copy())
    soma += value
    sobra = salario - soma
    if response == 'N':
        break

print()
print(40 * '=')
for k, v in enumerate(list_despesas):
    print(f'{k+1}° --> {v}')
print(40 * '=')
print()
print(f'Com um salário de R${salario:.2f} e um total de despesas de R${soma:.2f} sobra por mês R${sobra:.2f} reais.\n')
despesas = [[], [], [], []]
despesas_var = []
    
salario = int(input('Qual seu salário: R$ '))

''' moto é 0 
    casa é 1
    spotify 2 '''

for c in range(0, 3):
    d = str(input('Quais são suas despesas?: '))
    v = float(input('Valor: R$ '))
    if d == 'moto':
        despesas[0].append(d)
        despesas[0].append(v)
    elif d == 'casa':
        despesas[1].append(d)
        despesas[1].append(v)
    elif d == 'spotify':
        despesas[2].append(d)
        despesas[2].append(v)
soma = despesas[0][1] + despesas[1][1] + despesas[2][1]
sobra = salario - soma

# criado um laço infinito para valores adicionais
while True:
    d_var = str(input('Quais são as despesas adicionais?: '))
    v_var = float(input('Valor: R$ '))
    despesas_var.append(d_var)
    despesas_var.append(v_var)
    r = str(input('Tem mais alguma despesa para este mês? [S/N]: ')).upper()[0]
    if r in 'N':
        break
print(30 * '-=')
print(f'Seu salário é de R${salario:.2f}') 
print(f'O Total de suas despesas são R${soma:.2f}')
print(f'Esta é a quantia que sobra para você por mês R${sobra:.2f}')

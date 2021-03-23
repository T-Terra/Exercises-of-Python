num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num > num2:
    print('O PRIMEIRO valor é o maior!')
elif num < num2:
    print('O SEGUNDO valor é o maior!')
else:
    print('\033[34mOs dois valores são IGUAIS!')

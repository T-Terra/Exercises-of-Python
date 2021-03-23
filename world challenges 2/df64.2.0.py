print('Digite 999 quando quiser parar')
num = int(input('Digite um número: '))
cont = 0
soma = 0
while True:
    if num == 999:
        break
    soma += num
    num = int(input('Digite um número: '))
    cont += 1
# com f strings no lugar de .format (interpolação)
print(f'Foram digitados {cont} números e a soma deles é {soma}')

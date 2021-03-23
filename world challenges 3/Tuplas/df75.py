tupla = (int(input('Digite um número: ')), 
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores: {tupla}')
if 3 in tupla:
    print(f'O número 3 está na {tupla.index(3)+1}° posição') # pego o index do 3 mais 1
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'O número 9 aparece {tupla.count(9)} vezes')
print('Os valores pares digitados são: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ') 
        

    

# Resolução Gustavo Guanabara

# Usa uma Tupla para armazenar os valores 
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Começo Laço infinito 
while True:
    # Define variável 
    num = int(input('Digite um número entre 0 e 20: '))
    # Faz a verificação se está entre 0 e 20
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ') 
print(f'Você digitou o número {cont[num]}')
# printa o resultado


''' O cont[num] pega o número por extenso 
    que está dentro da dupla, 
    sendo que o input será apenas 
    o indíce da dupla pegando a posição.'''

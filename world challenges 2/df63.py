print('=' * 25)
print('sequência de Fibonacci')
print('=' * 25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0 
t2 = 1
print('~' * 40)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' > {} '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' ¥ Fim') 
print('~' * 40)

from time import sleep
print('Digite um número para ver sua tabuada \nou um número negativo para encerrar.')
while True:
    tabu = int(input('T: '))
    if tabu < 0:
        break
    for c in range(1, 11):
        print(f'{tabu} x {c} = {tabu*c}')
    print('=' * 20)
sleep(2)
print('\033[36mFIM... volte sempre!!!')

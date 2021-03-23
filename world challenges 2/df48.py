soma = 0 # acumulador, acumula os números somando-os
cont = 0 # contador, conta quantos números existem numa determinada série
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma entre {} valores solicitados é {} '.format(cont, soma))

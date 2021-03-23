class_times = ('sao paulo', 'atletico-mg', 'flamengo', 'gremio', 'fluminense', 'internacional',    'palmeiras', 'santos', 'ceara', 'fortaleza', 'corinthians', 'athletico', 'bahia', 'bragantino', 'atletico-go', 'sport', 'vasco', 'coritiba', 'botafogo', 'goias')

print(60*'=')
print('OS 5 PRIMEIROS COLOCADOS SÃO')
print(60*'=')
print(class_times[0:5])
print(60*'=')
print('OS 4 ÚLTIMOS COLOCADOS SÃO')
print(60*'=')
print(class_times[-4:])
print(60*'=')
print('TIMES EM ORDEM ALFABETICA')
print(60*'=')
print(sorted(class_times))
print(60*'=')
print('POSISAO DO CORINTHIANS ')
print(60*'=')
# Minha solução
for pos in range(11, 12):
    print(f'O {class_times[10]} está na {pos}° posição')

# Solução do Gustavo para a posição do corinthians

print(f'O Corinthians está na {class_times.index("corinthians")+1}° posição')

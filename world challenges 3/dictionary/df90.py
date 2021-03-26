main_dic = {}

main_dic['name'] = str(input(f'nome: '))
main_dic['media'] = float(input(f'media de {main_dic["name"]}: '))
print(25 * '-=')
print(f'O nome é igual a {main_dic["name"]}')
print(f'Média igual a {main_dic["media"]}')
if main_dic['media'] >= 7:
    main_dic['situation'] = 'Aprovado!'
elif 5 <= main_dic['media'] < 7:
    main_dic['situation'] = 'Recuperação!'
else:
    main_dic['situation'] = 'Reprovado!'
print(f'Situação é igual a {main_dic["situation"]}')
print(25 * '-=')
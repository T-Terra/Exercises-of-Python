from datetime import datetime
main_dict = {}
main_dict['name'] = str(input('Nome: '))
year_n = int(input('Ano de nascimento: '))
main_dict['job_work'] = int(input('Carteira de trabalho[ 0 não tem]: '))
main_dict['age'] = datetime.now().year - year_n
if main_dict['job_work'] != 0:
    main_dict['start_work'] = int(input('Ano de contratação: '))
    main_dict['wage'] = float(input('Salário: R$'))
    main_dict['retirement'] = main_dict['age'] + ((main_dict['start_work'] + 35) - datetime.now().year)
print(30 * '-=')
for k, v in main_dict.items():
    print(f'   - {k} tem o valor {v}')
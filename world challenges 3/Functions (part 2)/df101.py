def vote(year_c=0):
    from datetime import date
    global age
    current_year = date.today().year
    age_f = current_year - age
    if age_f < 16:
        return f'Com {age_f} anos: NÃO VOTA!'
    elif 16 <= age_f < 18 or age_f >= 65:
        return f'Com {age_f} anos: VOTO OPCIONAL.'
    else:
        return f'Com {age_f} anos: VOTO OBRIGATÓRIO.'

# main program
age = int(input('Em que ano você nasceu? '))
print(vote(age))

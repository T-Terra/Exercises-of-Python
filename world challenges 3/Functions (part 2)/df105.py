def notes(*n, sit=False):
    """-> Funcao para analisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou nao colocar a situacao.
    :return: dicionario com varias informacoes sobre a situacao da turma. 
    """
    dict_main = {}
    dict_main['tot'] = len(n)
    dict_main['maior'] = max(n)
    dict_main['menor'] = min(n)    
    dict_main['media'] = sum(n) / len(n)
    if sit:
        if media >= 7:
            dict_main['sit'] = 'Boa'
        elif media >= 5:
            dict_main['sit'] = 'Razoável'
        else:
            dict_main['sit'] = 'Ruim'
    return dict_main


# main program
response = notes(2, 3, 5, 7)
print(response)
#help(notes)
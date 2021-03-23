# desafio 019 exe para randomizar strings
from random import choice
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))

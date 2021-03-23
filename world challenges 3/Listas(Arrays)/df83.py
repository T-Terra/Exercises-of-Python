expr = str(input('Digite uma expressão: '))
pilha = []

for simb in expr: 
    if simb == '(':# acha o símbolo e adiciona na lista 
        pilha.append('(') 
    elif simb == ')':# acho o símbolo e se o tamanho da pilha for maior que 0, remove o símbolo de abertura.
        if len(pilha) > 0:
            pilha.pop() 
        else:# se não, adiciona o símbolo de fechamento tornado a expressão inválida.
            pilha.append(')')
            break

if len(pilha) == 0: # se o tamanho da pilha for 0 está válida.
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')


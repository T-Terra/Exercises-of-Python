def factorial(n, show=False):
    """
    -> Executa um calculo de fatorial
    :param n: Recebe o numero do fatorial a ser calculado.
    :param show=False: Por padrao false mas se for True mostra o processo de calculo.   
    :param return: Retorna o valor calculado   
    
    """
    print(30 * '-')
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# main program 
print(factorial(5, True))
#help(factorial)
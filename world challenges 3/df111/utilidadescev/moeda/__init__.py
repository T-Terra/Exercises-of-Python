def metade(p = 0, form=False):
    p /= 2
    return p if form is False else moeda(p)
    
def dobro(p = 0, form=False):
    p *= 2
    return p if form is False else moeda(p)

def aumentar(p = 0, quant = 0, form=False):
    percent = p + (p*quant / 100)
    return percent if form is False else moeda(percent)

def diminuir(p = 0, quant = 0, form=False):
    percent = p - (p*quant / 100)
    return percent if form is False else moeda(percent)
        
def moeda(p = 0, formatacao = 'R$'):
    return f'{formatacao}{p:.2f}'.replace('.', ',')

def write(msg):
    tam = len(msg) + 20
    print(tam * '-')
    print(f'{msg}'.center(30))
    print(tam * '-')

def resumo(p = 0, aumen = 0, redu = 0):
    write('RESUMO VALOR')
    print(f' Preço analisado:\t{moeda(p)}')
    print(f' Dobro do preço:\t{dobro(p, True)}')
    print(f' Metade do preço:\t{metade(p, True)}')
    print(f' {aumen}% de aumento:\t{aumentar(p, aumen, True)}')
    print(f' {redu}% de redução:\t{diminuir(p, redu, True)}')
    print(32 * '-')
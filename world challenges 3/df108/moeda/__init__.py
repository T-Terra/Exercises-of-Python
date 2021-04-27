def metade(p = 0):
    return p / 2

def dobro(p = 0):
    return p * 2

def aumentar(p = 0, quant = 0):
    percent = p + (p*quant / 100)
    return percent

def diminuir(p = 0, quant = 0):
    percent = p - (p*quant / 100)
    return percent

def moeda(p = 0, formatacao = 'R$'):
    return f'{formatacao}{p:.2f}'.replace('.', ',')
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
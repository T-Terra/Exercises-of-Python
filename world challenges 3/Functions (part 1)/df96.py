def area(l, c):
    tot = l * c
    print(f'A área de um terreno {l}x{c} é de {tot}m²')
    
# Main Program
print(30 * '=')
print('      Controle do Terreno')
print(30 * '=')
area(l = float(input('LARGURA (m): ')), c = float(input('COMPRIMENTO (m): ')))
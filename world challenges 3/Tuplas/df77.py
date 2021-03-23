palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

# percorre a tupla com o laço for 
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ') 
    for letra in p: # para cada letra em p
        if letra.lower() in 'aeiou': # se letra estiver em 'aeiou' escreva as letras
            print(letra, end=' ')

# resolução Guanabara

# toda string em uma tupla é uma lista

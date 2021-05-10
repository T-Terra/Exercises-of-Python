def title(msg):
    tam = len(msg) + 24
    print(tam * '-')
    print(f'{msg}'.center(tam))
    print(tam * '-')

def menu(msg):
    tam = len(msg) - 91
    print(f'{msg}')
    print(tam * '-')

def cadastro():
    return 0
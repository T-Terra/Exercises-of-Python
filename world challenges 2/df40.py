nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua nota foi {:.1f} e você está reprovado! estude mais.'.format(media))
elif media >= 5 and media < 7:
    print('Sua nota foi {:.1f} e você está de recuperação!!!'.format(media))
elif media >= 7:
    print('Sua nota foi {:.1f} e você está APROVADO!!!!!'.format(media))

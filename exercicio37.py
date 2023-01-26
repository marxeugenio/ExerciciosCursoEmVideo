altura = int(input('Informe a sua altura: '))
sexo = str(input('Informe o seu sexo: '))

if sexo=='masculino':
    pesoH = (72.7*altura) - 58
    print('O seu peso ideal é {:.2f} PARABENS È UM MENINO'.format(pesoH))
else:
    pesoM=(62.1*altura)-44.7
    print('O seu peso ideal para uma mulher é {:.2f} PARABENS È UMA MENINA '.format(pesoM))

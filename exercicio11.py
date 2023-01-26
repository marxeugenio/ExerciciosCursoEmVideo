altura = float(input('Insira o valor da altura: '))
largura = float(input('Insira o valor da largura: '))

area = altura * largura
tinta = area/2

print('Sua parede tem a dimensão de {}x{} e a sua area é de {}m.'.format(altura,largura,area))
print('Para pintar essa parede, voce precisará de {}L de tinta.'.format(tinta))
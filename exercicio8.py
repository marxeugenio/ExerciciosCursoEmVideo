medida = float(input('Insira o valor em metros: '))

centímetros = medida * 100
milímetros = medida * 1000

print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida,centímetros,milímetros))
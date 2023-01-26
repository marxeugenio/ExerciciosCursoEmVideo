dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))

pago = (dias * 60) + (Km * 0.15)

print('O total a pagar por dias é {:.2f} e o total de Km rodados é {:.2f}'.format(pago,Km))
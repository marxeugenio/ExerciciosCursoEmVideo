saldo = float(input('Digite o valor do seu saldo: R$'))

dolar = 3.27
conversão = saldo / dolar

print('O seu saldo é {} e voce pode comprar {:.2f} Dolares'.format(saldo, conversão))
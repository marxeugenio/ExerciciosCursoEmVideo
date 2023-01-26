distancia = float(input("Qual é a distancia da sua viagem? "))
print("Voce esta prestes a começar uma viagem de {}Km. ".format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))

print("ou")
distancia = float(input("Qual é a distancia da sua viagem? "))
print("Voce esta prestes a começar uma viagem de {}Km. ".format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("E o preço da sua passagem sera de R${:.2f}".format(preço))
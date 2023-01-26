velocidade = float(input("Qual é a velocidade do cidadão? "))
if velocidade > 80:
    multa= (velocidade-80) *7
    print("EI VOCE, VA COM CALMA AMIGO SUA MULTA È DE R${}".format(multa))
else:
    print("Isso bom trabalho amigo")
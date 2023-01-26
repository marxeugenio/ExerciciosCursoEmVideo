from datetime import date

ano = int(input("Digite um ano qualquer: "))
from datetime import date

ano = int(input("Digite um ano qualquer: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        print(f"{ano} é bissexto.")
    elif ano % 400 == 0:
        print(f"{ano} é bissexto. ")
    else:
        print(f"{ano} não é bisexto. ")
else:
    print(f"{ano} não é bissexto. ")

print('OU')

anio = int(input("Que ano quer analisar? "))
if anio == 0:
    anio = date.today().year
if anio % 4 == 0 and anio % 100 != 0 or:
    print("O ano {} é BISSEXTP ".format(anio))
else:
    print("O ano {} Não é BISSEXTO ".format(anio))
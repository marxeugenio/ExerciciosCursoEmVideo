from _typeshed import OpenTextModeUpdating


numero = int(input("Me diga um numero qualquer: "))
p = 0
i = 0

if numero % 2 == 0:
    p = numero
    print("O valor digitado foi {} Par".format(p))
else:
    i = numero
    print('O valor digitado foi {} impar'.format(i))

Ou
numero = int(input("Me diga um numero qualquer: "))
resultado = numero % 2
if resultado == 0:
    print("O numero {} é PAR".format(numero))
else:
    print("O numero {} é IMPAR".format(numero))
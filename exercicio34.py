A = int(input(" Primeiro valor: "))
B = int(input("Segundo valor: "))
C = int(input("Terceiro valor: "))
#Verificando quem é o menor
menor = A
if B < A and B < C:
    menor = B
if C < A and C < B:
    menor = C
#Verificando quem é o maior
maior = A
if B > A and B > C:
    maior = B
if C > A and C > B:
    maior = C
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
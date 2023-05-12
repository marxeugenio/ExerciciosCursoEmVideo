peso = int(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do Peso")

elif imc >= 18.5 and imc <= 25:
    print("Peso Ideal")

elif imc > 25 and imc <= 30:
    print("Sobrepesod")

elif imc > 30 and imc <= 40:
    print("Obesidade")

else:
    print("Obesidade Mórbida")
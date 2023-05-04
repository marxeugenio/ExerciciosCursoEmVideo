nota01 = float(input('Informe a primeira nota: '))
nota02 = float(input('Informe a segunda nota: '))

media =(nota01 + nota02) / 2

print('A primeira nota é {} e a segunda é {} a sua média é {}.'.format(nota01,nota02,media))

if media < 5:
    print('Voce foi reprovado')

elif media > 5 and media <= 6.9:
    print('Voce está de recuperação')

else:
    print('Você passou')
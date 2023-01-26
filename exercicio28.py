import random 
print('Vou pensar em um numero de 0 e 5. Tente adivinhar...')
valor = int(input('Em que numero eu pensei? '))
pc=int(5 * random.random())
if valor <= pc:
    print('Parabens voce acertou o pc pensou em {}'.format(pc))
else:
    print('Que pena o valor do computador foi diferente {}'.format(pc))

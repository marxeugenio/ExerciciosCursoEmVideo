valor = int(input('Insira um valor de [0 a 9999]: '))

c = (valor // 100) % 10
d = (valor//10)  % 10
u = valor % 10
m = (valor // 1000)

print('Centena:',c)
print('Dezena:',d)
print('Unidade:',u)
print('Milhar:',m)
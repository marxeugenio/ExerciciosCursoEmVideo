salario = float(input('Qual o salario do funcionario ? R% '))

novo = salario + ( salario* 15 / 100)

print('O seu salario é {:.2f} e o seu salario com 15% de aumento ficará R%{:.2f}.'.format(salario,novo))
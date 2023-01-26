produto = float(input('Insira o valor do produto para ver como ele fica com o desconto? R% '))

desconto = produto - (produto*5/100)

print('O preço do produto digitado é {} e com seu desconto de 5% fica = {}.'.format(produto,desconto))
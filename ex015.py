valor = float(input('Digite o valor do produto: '))

resul = valor * 0.05
desc = valor - resul

print('O valor do produto é {}R$ e com desconto de 5% ficaria {:.2f}R$.'.format(valor, desc))


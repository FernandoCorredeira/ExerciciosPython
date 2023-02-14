import math

num1 = float(input('Digite o valor do Cateto oposto: '))
num2 = float(input('Digite o valor do Cateto adjacente: '))

print('O comprimento da Hipotenusa é de: {:.3f}'.format(math.hypot(num1, num2)))

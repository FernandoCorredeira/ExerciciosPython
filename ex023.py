import math

num = float(input('Digite o valor de um ângulo: '))

print('O ângulo que você inseriu é de {}, o seno é de {:.3f} o cosseno é {:.3f} e a tangente é de {:.3f}'.format(num, math.sin(num), math.cos(num), math.tan(num)))
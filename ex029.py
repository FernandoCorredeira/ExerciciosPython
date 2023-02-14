
import math

angulo = float(input("Digite o valor do ângulo: "))
angulo = math.radians(angulo)

print("O valor do seno seria: {:.2f}".format(math.sin(angulo)))
print("O valor do cosseno seria: {:.2f}".format(math.cos(angulo)))
print("O valor da tangente seria: {:.2f}".format(math.tan(angulo)))

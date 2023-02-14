import math

catetoop = int(input("Digite o número do cateto oposto: "))
catetoadj = int(input("Digite o número do cateto adjascente: "))

hipo = math.hypot(catetoop, catetoadj)

print("o comprimento da hipotenusa seria de: {:.3f}".format(hipo))

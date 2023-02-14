temp = float(input('Informe a temperatura em ºC: '))

f = (temp * 1.8) + 32
k = temp + 273.15
print('A temperatura de {}ºC corresponde a {}ºF e {:.2f}K.'.format(temp, f, k))

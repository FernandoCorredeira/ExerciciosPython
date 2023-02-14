dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km você percorreu com o carro? '))

final = (dias *60) + (km * 0.15)

print('Você alugou o carro por {} dias e andou por {}km, o total a ser pago é R${:.2f}.'.format(dias, km, final))

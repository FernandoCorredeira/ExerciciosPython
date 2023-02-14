salario = float(input('Digite seu salário: '))

resul = salario * 0.15
novosal = salario + resul
print('Seu salário de {:.3f}R$, com 15% de aumento ficaria {:.3f}R$.'.format(salario, novosal))

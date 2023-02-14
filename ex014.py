l1 = float(input('Digite a largura da parede: '))
a1 = float(input('Digite a altura da parede: '))

resul = l1 * a1
tinta = resul / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(l1, a1, resul))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))


largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
área = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²' .format(largura , altura , área))
tinta = área / 2
print('Você precisará de {} de tinta para pintar sua parede.' .format(tinta))
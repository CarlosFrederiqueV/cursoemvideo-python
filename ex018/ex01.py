import math
ângulo = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo {}, tem o SENO {:.2f}.'.format(ângulo, seno))

cosseno = math.cos(math.radians(ângulo))
print('O ângulo {}, tem o cosseno {:.2f}'.format(ângulo, cosseno))

tangente = math.tan(math.radians(ângulo))
print('O ângulo {}, tem a tangente de {:.2f}.' .format(ângulo , tangente))
import random
n1 = str(input('Digite um nome:'))
n2 = str(input('Digite um nome:'))
n3 = str(input('Digite um nome:'))
n4 = str(input('Digite um nome:'))
sorteado = [n1 , n2 , n3 , n4]
random.shuffle(sorteado)
print('A ordem de apresentação será.')
print(sorteado)
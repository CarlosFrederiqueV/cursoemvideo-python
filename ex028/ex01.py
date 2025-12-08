from random import randint
computador = randint(0,5) #Faz o computador sortear
print('-=-' *20)
print('Vou pensar um número entre 0 e 5. Tente advinhar qual será')
print('-=-' *20 )
jogador = int(input('Em qual número eu pensei?')) #Jogador tenta acertar o número
if jogador == computador:
    print(('Parabéns! Você conseguiu me vencer.'))
else:
    print('Você perdeu. Eu pensei no número {} e não no {}!'.format(computador,jogador))

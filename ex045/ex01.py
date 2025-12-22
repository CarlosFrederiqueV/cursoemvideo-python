from random import randint
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0 , 2)
print('O computador escolheu {}.' .format(itens[computador]))
print('''Suas opções:
      [0] Pedra
      [1] papel
      [2] Tesoura
      ''')
jogador = int(input('Qual é a sua jogada?'))
print('-=' * 15)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:# Computador jogou PEDRA
    if jogador == 0:
    
    elif jogador == 1:
    print('Computador VENCEU!')
    elif jogador == 2:
    print('Jogador VENCEU!')

    else:
    print('Jogada inválida')
elif computador == 1: #Computador jogou PAPEL
        if jogador == 0:
    
    elif jogador == 1:
    
    elif jogador == 2:

    else:
    print('Jogada inválida') 

    
elif computador == 2: #Computador jogou TESOURA
         if jogador == 0:
    
    elif jogador == 1:
    
    elif jogador == 2:

    else:
    print('Jogada inválida') 


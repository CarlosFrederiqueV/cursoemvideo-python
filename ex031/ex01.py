distância = float(input('Qual é a distância de sua viagem?'))
print('Você está prestar a comecar uma viagem de {} km.' .format(distância))
if distância <= 200:
    preço = distância * 0.50
else: preço = distância * 0.45
print('E o preço da sua passagem será de {:.2f}.' .format(preço))
import math
num = float(input('Digite um número:'))
print('O número digitado foi {}, e sua porção inteira é {}.' .format(num , math.trunc(num)))

#Importação com método específico
from math import trunc
num = float(input('Digite um número:'))
print('O número digitado foi {}, e sua porção inteira é {}.' .format(num, trunc(num)))

#Outro método de quebra

num = float(input('Digite um número:'))
print('O número digitado foi {}, e sua porção inteira é {}.' .format(num , int(num)))

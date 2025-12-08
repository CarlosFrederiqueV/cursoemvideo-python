a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
#Verificando qual é o menor número
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    print('O menor valor ditado foi {}.'.format(menor))
#Verificando qual é o maior número
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c 
    print('O maior valor digitado foi {}.'.format(maior))   

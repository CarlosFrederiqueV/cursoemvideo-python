from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
print('O atleta tem {} anos.' .format(idade))
if idade <=9:
    print('Classificação: MIRIM.')
elif idade < 14:
    print('Classificação: INFANTIL.')
elif idade > 14 and idade <18:
    print('Classificação: ADOLESCENTE.')
elif idade >18:
    print('Classificação: ADULTO.')
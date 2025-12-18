peso = float(input('Qual é o seu peso?(kg):'))
altura = float(input('Qual é a sua altura?(mts):'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso NORMAL.')
elif imc >= 18.5 and imc <25:
    print('Você está com seu peso NORMAL.')
elif imc > 25  and imc <30:
    print('Você está com sobrepeso')    
elif imc > 30:
    print('ATENÇÃO!Você está com obesidade.')
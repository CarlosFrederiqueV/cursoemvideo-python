casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar a casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(casa , anos , prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')
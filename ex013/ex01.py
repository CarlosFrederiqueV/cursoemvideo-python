salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava {:.2f}R$, com o aumento de 15% passará a ganhar {:.2f}R$' .format(salário ,novo))
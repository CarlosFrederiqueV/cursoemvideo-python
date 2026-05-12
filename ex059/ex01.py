from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0  
while opção != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicação}.')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}.')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}.')
        else:
            print('Os números são iguais.')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)    
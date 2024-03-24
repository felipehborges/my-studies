# Crie um programa que leia dois valores e mostre um menu na tela:
# (1) somar (2) multiplicar (3) maior (4) novos números (5) sair do programa
# O seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
r = 0

while r != 5:
    print('\nEscolha a opção:\n')
    r = int(input('[1] SOMAR ... [2] MULTIPLICAR\n'
                  '[3] MAIOR ... [4] NOVOS NÚMEROS ... [5] SAIR\n'))
    if r == 1:
        print(f'SOMA: {n1} + {n2} = {n1 + n2}')
    elif r == 2:
        print(f'MULTIPLICAÇÃO: {n1} x {n2} = {n1 * n2}')
    elif r == 3:
        if n1 > n2:
            print(f'O maior valor entre {n1} e {n2} é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
        else:
            print(f'Os valores são iguais, não existe maior.')
    elif r == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif r == 5:
        r = 5
    else:
        print('Valor incorreto. Digite novamente: ')
print('FIM')

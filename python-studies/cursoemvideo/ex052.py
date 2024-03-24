# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[30m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('Portanto, é um número primo.')
else:
    print('Portanto, NÃO é um número primo.')

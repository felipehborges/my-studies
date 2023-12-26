# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
décimo = n1 + (10 - 1) * r

for n in range(n1, décimo + r, r):
    print(f'{n} ', end='> ')
print('FIM')

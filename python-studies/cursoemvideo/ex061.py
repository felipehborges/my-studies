# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando o WHILE.

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
termo = n1
cont = 1

while cont <= 10:
    print(f'{termo} > ', end='')
    termo += r
    cont += 1
print('FIM')

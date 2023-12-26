# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma sequência de Fibonacci. Ex.: 0 1 1 2 3 5 8

n = int(input('Defina quantos termos: '))
t1 = 0
t2 = 1
qtd = 3

print(t1, '>', t2, end=' > ')

while qtd <= n:
    t3 = t1 + t2
    print(t3, end=' > ')
    t1 = t2
    t2 = t3
    qtd += 1
print('FIM')

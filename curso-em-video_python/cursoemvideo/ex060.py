# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1=120

num = int(input('Digite um número inteiro: '))
c = num
f = 1
while c > 0:
    f *= c
    c -= 1
print(f'{num}! = {f}')

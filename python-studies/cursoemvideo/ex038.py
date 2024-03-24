# Escreva um programa que leia dois números inteiros e mostre na tela:
# O primeiro valor é maior ; O segundo valor é maior ; Não existe valor maior, são iguais.

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a > b:
    print(f'O primeiro valor é maior.')
elif b > a:
    print(f'O segundo valor é maior.')
else:
    print(f'Não existe valor maior, os dois são iguais.')

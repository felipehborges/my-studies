print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')

num = input('Digite um número de 0 a 9999: ')

print('{:>4}'.format(num))
numero = num.replace(' ', '0')
print(numero)

print('Milhar: {:>4}'.format(numero))
print('Centena: {:>4}'.format(numero))
print('Dezena: {:>4}'.format(numero))
print('Unidade: {:>4}'.format(numero))

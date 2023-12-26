print('Desenvolva um programa que leia o comprimento de três retas\n'
      'e diga ao usuário se elas podem ou não formar um triângulo.')

n1 = float(input('Primeiro lado do triângulo: '))
n2 = float(input('Segundo lado do triângulo: '))
n3 = float(input('Terceiro lado do triângulo: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
      print('É um TRIÂNGULO!')
else:
      print('NÃO é um triângulo.')
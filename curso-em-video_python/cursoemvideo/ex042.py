# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# Equilátero: todos os lados iguais; Isósceles: dois lados iguais; Escaleno: todos diferentes.

str(print('\033[1;32mCOLÉGIO IMAGINÁRIO DE PITÁGORAS\033[m\n'))

a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))

if a < b + c and b < a + c and c < a + b:
      print('É um TRIÂNGULO ', end='')
      if a == b == c:
          print('EQUILÁTERO!')
      elif a != b != c != a:
          print('ESCALENO!')
      else:
          print('ISÓSCELES!')
else:
      print('NÃO é um triângulo.')

# Crie um programa que vai gerar cinco nºs aleatórios e colocar em uma tupla.
# Depois, mostre a listagem de números gerados e também indique o menor e maior valor.
import random
num = random.randint(0, 20), random.randint(0, 20), random.randint(0, 20),\
      random.randint(0, 20), random.randint(0, 20)

print(f'Os valores sorteados foram {num}')
print(f'O maior valor é {max(num)}')
print(f'O menor valor é {min(num)}')

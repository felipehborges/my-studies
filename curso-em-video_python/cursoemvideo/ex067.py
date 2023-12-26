# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado. O programa para quando o número for negativo.
num = 0
while True:
    num = int(input('Digite um número para ver a tabuada: '))
    if num < 0:
        break
    for t in range(1, 11):
        print(f'{num} x {t} = {num * t}')
print('FIM')

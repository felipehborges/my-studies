# Refaça o desafio 09, mostrando a tabuada de algum número, só que utilizando FOR.

n = int(input('Digite um número para a tabuada: '))
for x in range(1, 11):
    print(f'{n} x {x} = {n * x}')

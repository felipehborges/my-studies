# Crie um prog que crie uma matriz de dimensão 3x3 e preencha com valores.
# No final, mostre a matriz na tela com a formatação correta.
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}], [{c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()

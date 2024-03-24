# Crie um prog onde o usuário possa digitar 5 valores num e cadastre-os na lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada.

lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Lista: {lista}')

# Crie um programa que o usuário digite 7 números e coloque-os numa lista única que
# mantenha separados os pares e ímpares. No final, mostre p e í em ordem crescente.
lista = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Lista geral: {lista}')
print(f'Lista de números pares: {lista[0]}')
print(f'Lista de números ímpares: {lista[1]}')

# Faça um programa que leia 5 valores numéricos e guarde-os numa lista. No final,
# mostre o maior e o menor valor e as suas respectivas posições na lista.
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')

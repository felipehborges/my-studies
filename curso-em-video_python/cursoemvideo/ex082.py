# Crie um prog que leia vários núms e coloque numa lista. Depois, crie 2 listas extras
# que vão conter apenas os valores pares e ímpares. Mostre o conteúdo das 3 listas geradas.
lista = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Lista 1: {lista}')
print(f'Lista 2 (pares): {listapar}')
print(f'Lista 3 (ímpares): {listaimpar}')

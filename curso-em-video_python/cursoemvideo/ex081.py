# Crie um prog que leia vários núms e colocar numa lista. A) Qtos núms foram digitados.
# B) A lista ordenada em decrescente.C) Se 5 foi digitado e se está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Quantidade de números digitados na lista: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista ordenada em decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não se encontra na lista.')
# Crie um prog onde o usuário possa digitar vários valores num e cadastre-os em uma lista.
# Caso o núm já exista na lista, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Número incluído na lista.')
    else:
        print('Número duplicado e não incluído na lista.')
    resp = input('Quer continuar? [S/N] ')
    if resp not in 'Ss':
        break
lista.sort()
print(f'Os números que você digitou em ordem crescente são: {lista}')

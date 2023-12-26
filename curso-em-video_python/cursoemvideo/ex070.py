# Crie um programa que leia nome e preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final, mostre: [A] Qual é o gasto total da compra
# [B] Quantos produtos custam mais de R$1000; [C] Qual é o nome do produto mais barato.

preçof = mil = menor = cont = 0
barato = ''
while True:
    produto = str(input('NOME DO PRODUTO: '))
    preço = float(input('PREÇO DO PRODUTO: R$ '))
    preçof += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Mais alguma coisa [S/N]? ')).upper().strip()[0]

    if resp == 'N':
        break
print('*'*30)
print(f'O preço total da compra foi de R$ {preçof}\n'
      f'Foram {mil} produtos que custaram mais de R$ 1000,00\n'
      f'O produto mais barato custou R$ {menor} e foi o (a) {barato}')

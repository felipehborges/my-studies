# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
# - A média de idade do grupo; - O nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

somaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print(f'{p}ª PESSOA')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print(f'A média de idades é {somaidade / 4:.1f}')
print(f'O nome do homem mais velho é {nomevelho.capitalize()}')
print(f'Quantidade de mulheres que têm menos de 20 anos: {totmulher20}')

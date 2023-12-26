# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 8):
    nasc = int(input(f'Digite o ano em que a {p}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Total de {totmaior} maiores de idade e {totmenor} menores de idade.')
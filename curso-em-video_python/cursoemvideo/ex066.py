# Crie um programa que leia vários números inteiros. O programa só para com o flag 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.

cont = soma = 0

while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma deles é {soma}')

# Crie um programa que leia vários núms inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

msg = 'S'
cont = 1
num = int(input('Digite um número: '))
msg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
maior = menor = soma = num
while msg == 'S':
    num = int(input('Digite um número: '))
    msg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    soma += num
print(f'Você digitou {cont} números. A soma entre eles é {soma} e a média é {soma / cont:.2f}\n'
      f'O maior valor foi {maior} e o menor foi {menor}.')
print('FIM')

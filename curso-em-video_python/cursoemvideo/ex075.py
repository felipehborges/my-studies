# Crie um programa que leia 4 valores e guarde-os em uma tupla. No final, mostre:
# (A) Quantas vezes apareceu o valor 9; (B) Em que posição foi digitado o primeiro 3;
# (C) Quais foram os números pares.

num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro 3 apareceu em {num.index(3) + 1}º lugar.')
else:
    print('Não tem nenhum 3.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário
# ou então o empréstimo será negado.

str(print('\033[1;33mBANCO ME PAGUE\033[m\n'))

casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o valor do seu salário mensal? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
prest = casa / (anos * 12)

print(f'\nO valor da prestação mensal será de {prest:.2f}\n')

if prest > sal * 0.30:
    print('Desculpe, seu empréstimo foi negado.'
          'A prestação ultrapassa 30% do seu salário mensal.')
else:
    print('Seu empréstimo foi aprovado, parabéns!')

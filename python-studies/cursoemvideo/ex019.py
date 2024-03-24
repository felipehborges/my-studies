from random import choice

print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro.'
      'Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.\n')

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
chosen = [a, b, c, d]

print(f'\nO escolhido para apagar a lousa é {choice(chosen)}')

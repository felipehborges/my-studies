import random

print('O mesmo professor quer sortear a ordem de apresentação dos trabalhos dos alunos.\n')

a = input('Aluno 1 - ')
b = input('Aluno 2 - ')
c = input('Aluno 3 - ')
d = input('Aluno 4 - ')
lista = [a, b, c, d]
random.shuffle(lista)

print(f'\nA ordem para apresentar o trabalho é: '
      f'{lista}.')

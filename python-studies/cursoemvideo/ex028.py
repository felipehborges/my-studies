import random

print('O PC vai pensar em um número e o usuário tem que tentar adivinhar qual é.\n'
      'O programa deverá informar se o usuário venceu ou perdeu.\n')

n1 = int(input('Pensei em número de 0 a 5. Adivinhe qual é: '))
pc = random.randint(0, 5)

if n1 == pc:
    print(f'Parabéns! O número que eu pensei foi esse mesmo: {pc}!')
else:
    print(f'{n1}? Não, pensei em {pc}. Tente de novo.')

# Faça um programa que jogue par ou ímpar com o PC. O jogo acaba quando o jogador perde,
# mostrando o total de vitórias consecutivas que ele conquistou no final.
import random
print('PAR OU ÍMPAR?')
print('-'*30)
num = pc = vitória = 0
while True:
    escolha = int(input('Escolha par [1] ou ímpar [2]: '))
    if escolha == 1:
        num = int(input('Você escolheu PAR. Insira um número: '))
        pc = random.randint(1, 2)
        if (num + pc) % 2 == 0:
            print(f'{num} + {pc} = {num + pc}')
            print('Você ganhou! Vamos jogar novamente.')
            print('-' * 30)
            vitória += 1
        else:
            print(f'{num} + {pc} = {num + pc}')
            break
    elif escolha == 2:
        num = int(input('Você escolheu ÍMPAR. Insira um número: '))
        pc = random.randint(1, 2)
        if (num + pc) % 2 != 0:
            print(f'{num} + {pc} = {num + pc}')
            print('Você ganhou! Vamos jogar novamente.')
            print('-' * 30)
            vitória += 1
        else:
            print(f'{num} + {pc} = {num + pc}')
            break
print('-'*30)
print(f'Você perdeu, jogo encerrado.\n'
      f'Você teve {vitória} vitórias consecutivas!')

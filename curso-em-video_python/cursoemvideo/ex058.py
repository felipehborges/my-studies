# Melhore o jogo do desafio 28, só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random
r = int(input('Pensei em número de 0 a 10. Adivinhe qual é: '))
pc = random.randint(0, 10)
soma = 1
while r != pc:
    if r < pc:
        r = int(input('Um pouco mais. Tente de novo: '))
        soma += 1
    else:
        r = int(input('Um pouco menos. Tente de novo: '))
        soma += 1
print(f'Parabéns, eu pensei em {pc}! Você adivinhou com {soma} tentativas.')


'''RESOLUÇÃO GUANABARA

computador = random.randint(0, 10)
acertou = True
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = False
    else:
        if jogador < computador:
            print('Mais... Tente de novo.')
        elif jogador > computador:
            print('Menos... Tente de novo.')
print(f'Acertou com {palpites} tentativas. Parabéns!')'''

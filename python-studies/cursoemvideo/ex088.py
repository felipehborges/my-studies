# Faça um prog que ajude um jogador da Mega criar palpites. O prog vai perguntar
# quantos jogos serão gerados e vai sortear 6 núms entre 1 e 60 pra cada jogo,
# cadastrando tudo numa lista composta.
from random import randint
lista = list()
jogos = list()
print('MEGA SENA')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {quant} jogos:')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

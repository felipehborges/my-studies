# Crie um prog que gerencie o aproveitamento de um jogador de futebol. O prog vai ler o nome do jogador, quantas
# partidas ele jogou e depois, vai ler a qtd de gols feitos em cada partida. No final, tudo isso será guardado em um
# dict, incluindo o total de gols feitos durante um campeonato.
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=' * 30)
print(jogador)
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

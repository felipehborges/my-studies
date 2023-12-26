# Crie uma tupla preenchida com os 20 primeiros do Camp Br, na ordem. Depois mostre:
# (A) Apenas os 5 primeiros colocados; (B) Os últimos 4 colocados da tabela
# (C) Uma lista com os times em ordem alfabética; (D) Em que posição está o Bragantino.
import collections

camp = ('PALMEIRAS', 'ATLÉTICOMG', 'CORINTHIANS', 'INTERNACIONAL', 'FLUMINENSE',
        'ATHLETICOPR', 'FLAMENGO', 'BRAGANTINO', 'SPFC', 'SANTOS', 'BOTAFOGO',
        'AVAÍ', 'GOIÁS', 'CEARÁ', 'CUIABÁ', 'CORITIBA', 'AMÉRICAMG', 'ATLÉTICOGO',
        'FORTALEZA', 'JUVENTUDE')

print(f'Os cinco primeiros colocados são: {camp[:6]}')
print('~'*50)
print(f'Os últimos 4 colocados da tabela são: {camp[-4:]}')
print('~'*50)
print(f'Ordem alfabética série A: {sorted(camp)}')
print('~'*50)
print(f'O Bragantino está na posição número {camp.index("BRAGANTINO")+1}.')

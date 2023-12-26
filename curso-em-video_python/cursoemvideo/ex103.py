# Faça um prog que tenha uma função chamada ficha(), que receba 2 parâmetros opcionais: o nome de
# um jogador e quantos gols ele marcou. O prog deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog='<indefinido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Qual o nome do jogador? '))
g = str(input('Quantos gols ele marcou? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

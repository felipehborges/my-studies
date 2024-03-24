# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
cont = 1
total = 0
resposta = 10

while resposta != 0:
    total += resposta
    while cont <= total:
        print(f'{n1} > ', end='')
        n1 += r
        cont += 1
    print('PAUSA')
    resposta = int(input('Quantos termos a mais você quer? '))
print(f'FIM - {total} termos mostrados.')

# Faça um prog que tenha uma função CONTADOR() que receba 3 parâmetros: início, fim e passo, e realiza a contagem.
# Seu programa tem que realizar 3 contagens através da função criada: a) de 1 até 10, de 1 em 1;
# b) de 10 até 0, de 2 em 2; c) uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.25)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.25)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Defina o início: ')), int(input('Defina o fim: ')),
         int(input('Defina o passo: ')))

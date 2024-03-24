# Crie um prog que tenha uma função fatorial() que receba 2 parâmetros: o 1º que indique o nº
# a calcular e o outro show, que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(90, show=True))

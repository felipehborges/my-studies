# Crie um programa que simule um caixa eletrônico. Pergunte qual será o valor
# a ser sacado (int) e o prog vai dizer quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1.
print('--- CAIXA ELETRÔNICO ---')
valor = int(input('Insira o valor a ser sacado: R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Obrigado.')

# Faça um prog que tenha uma função MAIOR(), que receba vários parâmetros com valores inteiros.
# Seu prog tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 8, 4, 4, 6, 1, 10)
maior(1, 5, 2)
maior(1)
maior()
maior(4, 4)

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
# extenso, de 0 até 20. Seu programa deverá ler um nº e mostrá-lo por extenso.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {extenso[num]}.')
        resp = input('Deseja continuar? [S/N] ').upper().strip()
        if resp == 'N':
            break
    else:
        print('Tente de novo. ', end='')
print(f'Obrigado.')

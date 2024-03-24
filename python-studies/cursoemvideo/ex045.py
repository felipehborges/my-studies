# Crie um programa que faça o PC jogar JOKENPO com você.
import random
import time

print('\033[31mJOKENPO\033[m\n')

user = int(input('Insira 1 para PAPEL, 2 para PEDRA e 3 para TESOURA: '))
pc = random.randint(1, 3)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO\n')

if user == 1 and pc == 2:
    print('Você escolheu PAPEL e o computador escolheu PEDRA. Você venceu!')
elif user == 1 and pc == 3:
    print('Você escolheu PAPEL e o computador escolheu TESOURA. Você perdeu!')
elif user == 2 and pc == 1:
    print('Você escolheu PEDRA e o computador escolheu PAPEL. Você perdeu!')
elif user == 2 and pc == 3:
    print('Você escolheu PEDRA e o computador escolheu TESOURA. Você venceu!')
elif user == 3 and pc == 1:
    print('Você escolheu TESOURA e o computador escolheu PAPEL. Você venceu!')
elif user == 3 and pc == 2:
    print('Você escolheu TESOURA e o computador escolheu PEDRA. Você perdeu!')
else:
    print('EMPATE!')

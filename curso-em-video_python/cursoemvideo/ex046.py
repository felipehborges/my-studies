# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

str(print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO\n'))

for x in range(10, -1, -1):
    print(x)
    time.sleep(0.5)
print('UHUL!')
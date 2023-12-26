# Faça um prog que tenha uma função chamada AREA(), que receba as dimensões de um terreno retangular
# (largura e comprimento e mostre a área do terreno.
def area(a, b):
    s = a * 2 + b * 2
    print(f'Seu terreno tem {s}m².')


area(a=float(input('Defina a largura do terreno: ')), b=float(input('Defina o comprimento do terreno: ')))

# Crie um programa que leia vários núms inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
# quantos núms foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
num = int(input('Digite um número inteiro [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles deu {soma}.')
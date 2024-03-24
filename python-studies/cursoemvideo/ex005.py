print('*Faça um programa que leia um número inteiro e mostre seu sucessor e seu antecessor*')

n1 = int(input('Digite um número inteiro: '))
print('O número antecessor de {} é {}'.format(n1, n1-1))
print('O número sucessor de {} é {}\n'.format(n1, n1+1))

#OUTRO JEITO

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print ('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(n, a, s))

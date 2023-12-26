print('*Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada*')
print('')
n1 = int(input('Digite um número inteiro: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}.\n'.format(n1,n1*2,n1*3,n1**(1/2)))

#OUTRO JEITO

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro desse número é {}\nO triplo desse número é {}\nE a raiz quadrada desse número é {:.2f}'.format(d, t, r))

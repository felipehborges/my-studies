print('[Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto]\n')

p = float(input('Digite aqui o preço do produto para verificar a possibilidade de desconto: R$ '))
print('PARABÉNS! Você ganhou 5% de desconto! O novo preço do produto será R$ {:.2f}'.format(p-p*0.05))

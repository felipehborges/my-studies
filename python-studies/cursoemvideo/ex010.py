print('*Crie um programa para converter reais em dólares (cotação do dia: R$ 5,05)*\n')
valor = float(input('Quer saber quantos dólares você consegue comprar?\nInforme quanto você tem na carteira: '))
print('Valor convertido em dólares: U$ {:.2f}'.format(valor/5.05))
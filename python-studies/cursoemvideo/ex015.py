print('ALUGUEL DE CARRO: O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO\n')

km = int(input('Digite a quantidade de km rodados com o carro: '))
d = int(input('Digite quantos dias você ficou com o carro: '))

print('O preço total a pagar é de R$ {:.2f}'.format((km*0.15)+(d*60)))

# Programa que calcule o valor a ser pago por um produto, considerando seu preço normal
# e condição de pagamento: À vista no dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desc; Até 2x no cartão: preço normal; 3x ou mais: 20% de juros.
print('\033[1;32mLOJA TRANSPARENTE DE ELETRODOMÉSTICOS\033[m\n')
compra = int(input('Preço das compras: R$ '))
print('''Formas de pagamento:
      (1) - À vista no dinheiro ou cheque;
      (2) - À vista no cartão;
      (3) - 2x no cartão;
      (4) - 3x ou mais no cartão.''')
num = int(input('Insira um número para a forma de pagamento: '))

if num == 1:
    print(f'\nSua compra de R$ {compra} terá um desconto de 10%!\n'
          f'Valor final: R$ {compra - compra * 0.10:.2f}')
elif num == 2:
    print(f'\nSua compra de R$ {compra} terá um desconto de 5%!\n'
          f'Valor final: R$ {compra - compra * 0.05:.2f}')
elif num == 3:
    print(f'\nVocê pagará em 2 parcelas de {compra / 2}\n'
          f'Valor final: R$ {compra}')
elif num == 4:
    parc = int(input('Quantas parcelas? '))
    valor = compra + compra * 0.20
    print(f'\nVocê pagará em {parc} parcelas de {valor / parc}\n'
          f'Valor final: R$ {valor}')

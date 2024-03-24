print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\n'
      'Para salários superiores a R$ 1250,00, calcule um aumento de 10%.\n'
      'Para os inferiores ou iguais, o aumento é de 15%.\n')

sal = float(input('Informe o valor do seu salário: R$ '))

if sal > 1250:
      print(f'Você recebeu um aumento de 10%. Seu novo salário é {sal*0.10+sal:.2f}.')
else:
      print(f'Você recebeu um aumento de 15%. Seu novo salário é {sal*0.15+sal:.2f}.')

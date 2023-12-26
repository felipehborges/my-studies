print('[Defina um salário de um funcionário e depois um novo salário com 15% de aumento]')

s = float(input('\nInsira aqui o valor mensal do seu salário bruto: R$ '))
print('\nParabéns, você foi promovido e ganhou um aumento salarial de 15%!\n')
print('Seu novo salário: R$ {:.2f}'.format(s+s*0.15))

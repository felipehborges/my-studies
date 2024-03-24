# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

r = str(input('Sexo [M/F]: ')).upper().strip()[0]

while r not in 'MmFf':
    r = str(input('Dado incorreto. Insira novamente: ')).upper().strip()[0]
print('Obrigado.')

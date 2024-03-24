print('Crie um programa que leia o nome completo de uma pessoa e mostre:\n'
      '- O nome com todas as letras maiúsculas;\n'
      '- O nome com todas as minúsculas;\n'
      '- Quantas letras ao todos (sem considerar espaços);\n'
      '- Quantas letras tem o primeiro nome.\n')

nome = input('Digite seu nome completo: ')
nomed = nome.split()
nomef = ''.join(nomed)

print(f'\nSeu nome completo em letras maiúsculas é: {nome.upper()}')
print(f'\nSeu nome completo em letras minúsculas é: {nome.lower()}')
print(f'\nSeu nome completo tem {len(nomef)} letras.')
print(f'\nSeu primeiro nome tem {len(nomed[0])} letras.')

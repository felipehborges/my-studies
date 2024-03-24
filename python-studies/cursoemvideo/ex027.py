print('Faça um programa que leia o nome completo de uma pessoa, '
      'mostrando em seguida o primeiro e o último nome separadamente.')

nome = input('Digite seu nome completo: ').strip()
nomesplit = nome.split()

print(f'Seu primeiro nome é {nomesplit[0].capitalize()}')
print(f'Seu último nome é {nomesplit[len(nomesplit)-1].capitalize()}')

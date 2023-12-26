print('[Faça um programa que leia a largura e a altura de uma parede em metros,] \n'
      '[  calcule a sua área e a quantidade de tinta necessária para pintá-la, ] \n'
      '[        sabendo que cada litro de tinta, pinta uma área de 2m²         ] \n')

lar = float(input('Defina uma medida para a largura da parede em metros: '))
alt = float(input('Defina uma medida para a altura da parede em metros: '))

print('\nA área da parede é de {0:.2f} metros, ou seja, a parede possui {0:.2f}m².'.format(lar * alt))
print('Tendo isso em consideração, serão necessários {:.2f} litros de tinta para pintar a parede toda.'.format(lar*alt/2))

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}, '
      f'o dobro é {moeda.dobro(p, True)}, '
      f'aumentando 10%, temos {moeda.aumentar(p, 10, True)}, '
      f'e reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')

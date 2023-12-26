from ex108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}, '
      f'o dobro é {moeda.moeda(moeda.dobro(p))}, '
      f'e aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')

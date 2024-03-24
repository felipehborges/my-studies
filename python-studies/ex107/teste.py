import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}, o dobro é R$ {moeda.dobro(p)}, '
      f'e aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')

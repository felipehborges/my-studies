print('Crie um programa que pergunte a distância de uma viagem em km.\n'
      'Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km\n'
      'e R$ 0,45 por km para viagens mais longas.')

km = float(input('Qual foi a distância da viagem em km? '))

#preço = km * 0.50 if km <= 200 else km * 0.45 (SIMPLIFICADO)

if km <= 200:
      print(f'Você deverá pagar o valor de R$ {km*0.5}')
else:
      print(f'Você deverá pagar o valor de R$ {km*0.45}')
print('Escreva um programa que leia a velocidade de um carro.\n'
      'Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.\n'
      'A multa vai custar R$ 7,00 por cada km acima do limite.\n')

velo = int(input('Digite a velocidade do carro em km/h: '))

if velo > 80:
      print(f'Você será multado em R$ {(velo - 80) * 7} por ter ultrapassado o limite de 80 km/h.')
else:
      print('Sem multas, tenha um ótimo dia.')
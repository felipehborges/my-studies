# Programa que calcule o IMC com base na altura e peso da pessoa e dê o feedback:
# Abaixo de 18.5: abaixo do peso; Entre 18.5 e 25: peso ideal; 25 a 30: sobrepeso;
# Entre 30 e 40: obesidade; Acima de 40: obesidade mórbida.
str(print('\033[4;30;47mACADEMIA MAROMBEIÇOS\033[m'))

altura = float(input('\nInsira sua altura (m): '))
peso = float(input('Insira seu peso (kg): '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'\nSeu IMC é {imc:.1f}. Você está abaixo do peso!')
elif imc < 25:
    print(f'\nSeu IMC é {imc:.1f}. Você está no peso ideal!')
elif imc < 30:
    print(f'\nSeu IMC é {imc:.1f}. Você está em sobrepeso!')
elif imc < 40:
    print(f'\nSeu IMC é {imc:.1f}. Você está em obesidade!')
else:
    print(f'\nSeu IMC é {imc:.1f}. Você está em obesidade mórbida!')

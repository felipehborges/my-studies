print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.')

nome = input('Digite seu nome completo: ').strip()
sur = nome.upper()

print('SILVA' in sur)
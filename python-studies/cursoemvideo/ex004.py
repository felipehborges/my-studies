print('Dissecando uma variável\n')

p = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(p))
print('Só tem espaços? ', p.isspace())
print('É um número? ', p.isnumeric())
print('É alfabético? ', p.isalpha())
print('É alfanumérico? ', p.isalnum())
print('Está em maiúsculas? ', p.isupper())
print('Está em minúscula? ', p.islower())
print('Está capitalizada? ', p.istitle())

# Crie um prog que leia nome, ano de nasc e CTPS e cadastre-os (com idade) em um dict. Se por acaso a CTPS diferir
# de ZERO, o dict receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Numeração da CTPS: '))
if cadastro['ctps'] != 0:
    cadastro['ctpsano'] = int(input('Ano de admissão: '))
    cadastro['ctpssal'] = float(input('Salário: R$ '))
aposent = 35 - (2022 - cadastro['ctpsano'])
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')

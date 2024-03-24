# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9: MIRIM; Até 14: INFANTIL; Até 19: JÚNIOR; Até 20: SÊNIOR; Acima: MASTER.
import datetime

str(print('\033[4;36mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m\n'))

nasc = int(input('Insira o ano do seu nascimento: '))
ano = datetime.date.today().year
idade = ano - nasc

print(f'Sua idade: {idade}')
if idade <= 9:
    print('Categoria: \033[1mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[1mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[1mJÚNIOR\033[m')
elif idade <= 25:
    print('Categoria: \033[1mSÊNIOR\033[m')
else:
    print('Categoria: \033[1mMASTER\033[m')
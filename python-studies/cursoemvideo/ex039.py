# Programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar;
# Se já passou do tempo do alistamento. Também deverá mostrar o tempo que falta ou que passou do prazo.

str(print('\033[1;34;40mSERVIÇO MILITAR FICTÍCIO DE FLORENÇA\033[m\n'))

idade = int(input('Olá, príncipe! Digite sua idade: '))

if idade < 18:
    print(f'Restam {18-idade} anos para a idade de alistamento!')
elif idade == 18:
    print(f'Você está convocado para comparecer ao corpo do exército!')
else:
    print(f'Já passou da idade! Você está atrasado em {idade-18} anos do alistamento.')

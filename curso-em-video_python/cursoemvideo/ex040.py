# Programa que leia duas notas de um aluno e calcule sua média e que apareça uma mensagem:
# Abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Acima de 7.0: APROVADO.

str(print('\033[1;35mESCOLA ARISTOTÉLICA INEXISTENTE DE MOGI DAS CRUZES\033[m\n'))

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segundo nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'\nMédia: {media:.1f}\n\033[1;31mREPROVADO\033[m')
elif media > 7:
    print(f'\nMédia: {media:.1f}\n\033[1;34mAPROVADO\033[m')
else:
    print(f'\nMédia: {media:.1f}\n\033[1;33mRECUPERAÇÃO\033[m')

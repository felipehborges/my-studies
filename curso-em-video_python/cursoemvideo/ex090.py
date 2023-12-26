# Faça um prog que leia nome e média de um aluno, guardando também a situação em um dict.
# No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média do (a) {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = str('Aprovado')
else:
    aluno['Situação'] = str('Reprovado')
for k, v in aluno.items():
    print(f'{k} é {v}.')

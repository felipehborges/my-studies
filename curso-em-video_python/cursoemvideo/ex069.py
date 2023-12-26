# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa,
# o programa pergunta se o usuário quer ou não continuar. No final, mostre:
# [A] Quantos tem mais de 18; [B] Quantos homens; [C] Quantas mulheres tem menos de 20 anos

idadef = homem = mulher = 0

while True:
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        idadef += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print('~'*30)
print(f'Pessoas maiores de 18: {idadef}\n'
      f'Homens: {homem}\n'
      f'Mulheres com menos de 20 anos: {mulher}')

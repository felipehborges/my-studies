# Crie um prog que o usuário digite uma expressão qualquer que use parênteses.
# Seu app deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válido!')
else:
    print('Inválido!')

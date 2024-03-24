# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (arara),
# desconsiderando os espaços.

frase = str(input('Digite uma frase e veja se é um palíndromo: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não é um palíndromo.')

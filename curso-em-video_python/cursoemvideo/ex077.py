# Crie um programa que tenha uma tupla com várias palavras (sem acentos).
# Depois, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = 'guanabara', 'curso', 'python', 'mundo', 'tecnologia'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

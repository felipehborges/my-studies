print('Faça um programa que leia uma frase pelo teclado e mostre:\n'
      '- Quantas vezes aparece a letra "A";\n'
      '- Em que posição ela aparece a primeira vez;\n'
      '- Em que posição ela aparece a última vez.')

frase = input('Digite uma frase: ').upper().strip()

print(f'Quantas vezes o "A" aparece: {frase.count("A")}')
print(f'Primeira vez do "A": {frase.find("A")}')
print(f'Última posição do "A": {frase.rfind("A")}')

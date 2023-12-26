# Faça um prog que tenha uma função chamada ESCREVA(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
def escreva():
    msg = input('Escreva sua mensagem: ')
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


escreva()

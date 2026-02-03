# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: 
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(txt):
    tam=len(txt) 
    print('-'*tam)
    print(txt)
    print('-'*tam)


escreva('Sandyele Severo')
escreva('Engenharia de Software')
escreva('UEPG')
print('='*20)
msg=str(input('Digite um texto: ')).strip()
escreva(msg)
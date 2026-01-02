# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase=str(input('Digite uma frase: ')).upper()
frase=frase.replace(' ', '')
inv=''
for i in range (len(frase)-1, -1, -1):
    inv += frase[i]
print('Você digitou: {}'.format(frase))
print('O inverso dela é {}'.format(inv))
if frase == inv:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')

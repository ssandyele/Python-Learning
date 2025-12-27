# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

a=int(input('Digite um número inteiro: '))
b=int(input('Digite mais um número inteiro: '))
if a>b:
    print('O primeiro valor é maior!')
elif b>a:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais.')
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

div=0
num=int(input('Digite um número inteiro: '))
for c in range (1, num):
    if num%c==0:
        div += 1
if div==1:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))

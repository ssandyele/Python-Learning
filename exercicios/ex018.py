#Faça um programa que leia um ângulo qualquer e mostre 
# na tela o valor do seno, cosseno e tangente desse ângulo.

import math
num=float(input('Digite um número: '))
s=math.sin(math.radians(num))
c=math.cos(math.radians(num))
t=math.tan(math.radians(num))
print('-'*15)
print('VALOR DO:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s,c,t))
print('-'*15)

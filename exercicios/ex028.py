#Escreva um programa que faça o computador “pensar” em um número inteiro entre 
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo 
# computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num=random.randint(0,5)
print('-=-'*18)
print('O computador pensou em um número inteiro de 0 a 5...')
n=int(input('Tente adivinhar o número escolhido: '))
print('Processando...')
sleep(2)
print('---'*18)
if num==n:
    print('PARABÉNS, VOCÊ ACERTOU!!!! O número realmente era {}'.format(n))
else:
    print('Você ERROU :(\nO número escolhido foi {}, não {}'.format(num,n))
print('-=-'*18)


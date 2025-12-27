# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep
opc = ('Pedra', 'Papel', 'Tesoura')
comp=random.randint(0,2)
print('Digite:')
print('[ 0 ] para pedra')
print('[ 1 ] para papel')
print('[ 2 ] para tesoura')
usuar=int(input('O que você vai jogar? '))
if usuar==0 or usuar==1 or usuar==2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('='*20)
    print('Jogador jogou: {}'.format(opc[usuar]))
    print('Computador jogou: {}'.format(opc[comp]))
    print('='*20)
    if comp==usuar:
        print('EMPATE!')
    elif comp==usuar+1 or comp==0 and usuar==2:
        print('VOCÊ PERDEU!')
    else:
        print('VOCÊ GANHOU!')
else:
    print('Você não digitou uma opção válida! Tente novamente.')
    

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos 
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos=[]
sorteio=[]
cont=0

print('-'*30)
print('      JOGA NA MEGA SENA      ')
print('-'*30)
qnt=int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {qnt} JOGOS =-=-=-')
for c in range (0,qnt):
    while True:
        num=randint(1,60)
        if num not in sorteio:
            sorteio.append(num)
            cont +=1
        if cont==6:
            cont=0
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
for i, j in enumerate(jogos, start=1):
    sleep(1)
    print(f'Jogo {i}: {j}')
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')
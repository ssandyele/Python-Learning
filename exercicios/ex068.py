# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando 
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
rf=''
msg=''
vitorias=0 
print('=-=-=- PAR OU ÍMPAR -=-=-=')
while True:
    n=int(input('Digite um valor: [0 a 10]. '))
    aposta=input('Par ou ímpar? [P/I] ').strip().upper()[0]
    c=randint(0,10)
    res=n+c
    rf= 'P' if res%2==0 else 'I'
    msg= 'PAR' if rf=='P' else 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {n} e o computador jogou {c}. Total {res}, DEU {msg}!')
    print('-'*30)
    if aposta==rf:
        vitorias += 1
        print('VOCÊ VENCEU! PARABÉNS!')
        print('Vamos jogar de novo...')
    else: 
        print('VOCÊ PERDEU!')
        break
    print('=-'*20)
print('=-'*20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')

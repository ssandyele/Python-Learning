# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
# palpites foram necessários para vencer.

import random
from time import sleep
num=random.randint(0,10)
cont=1
msg=''

print('-=-'*18)
print('O computador pensou em um número inteiro de 0 a 10...')
n=int(input('Tente adivinhar o número escolhido: '))
print('Processando...')
sleep(2)
while num!=n:
    print('---'*18)
    print('Você ERROU :(')
    msg= 'Talvez um valor mais baixo...' if n>num else 'Talvez um valor mais alto...'
    print(msg)
    n=int(input('Tente novamente! Digite um número de 0 a 10: '))
    print('Processando...')
    sleep(1)
    cont += 1
print('-=-'*18)
print('PARABÉNS, VOCÊ ACERTOU!!!! O número realmente era {}'.format(n))
print('Você precisou de {} palpites para conseguir acertar!'.format(cont))
print('-=-'*18)
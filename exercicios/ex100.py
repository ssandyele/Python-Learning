# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0,5):
        n=randint(1, 9)
        lst.append(n)
        sleep(0.5)
        print(n, end=' ', flush=True)
    print('PRONTO!')

def somaPar(lst):
    soma=0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lst}, temos {soma}')

numeros=[]
sorteia(numeros)
somaPar(numeros)
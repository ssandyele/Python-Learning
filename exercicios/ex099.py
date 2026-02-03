# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*valores):
    print('=-'*20)
    print('Analisando os valores passados...')
    if len(valores)==0:
        print('Nenhum valor informado.')
    else: 
        for pos, v in enumerate(valores):
            sleep(0.5)
            print(v, end=' ', flush=True)
            if pos==0:
                mai=v
            else:
                if v>mai:
                    mai=v
        print(f'Foram informados {len(valores)} valores ao todo.')
        print(f'O maior valor informado foi {mai}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
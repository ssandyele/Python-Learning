# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(inicio, final, passo):
    print('=-'*20)
    pas = passo if passo>=0 else passo*(-1)
    if passo>0 and inicio>final or passo<0 and inicio<final:
        passo *= -1
    print(f'Contagem de {inicio} até {final}, de {pas} em {pas}')
    fim = final+1 if passo >= 0 else final-1
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')
i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contador(i, f, p)
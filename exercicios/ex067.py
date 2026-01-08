# Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será interrompido quando 
# o número solicitado for negativo.

while True:
    print('PARA ENCERRAR O PROGRAMA, DIGITE UM NÚMERO NEGATIVO')
    num=int(input('Digite um número inteiro para ver sua tabuada: '))
    if num<0: break
    print('-'*30)
    for c in range(0,11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO!')
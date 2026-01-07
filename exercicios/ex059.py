# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

a=int(input('Digite um número: '))
b=int(input('Digite mais um número: '))
opc=-1
while opc!=5:
    print('''Escolha uma das seguintes opções:
          [ 1 ] somar
          [ 2 ] multiplicar
          [ 3 ] maior
          [ 4 ] novos números
          [ 5 ] sair do programa''')
    opc=int(input('-> '))
    if opc == 1:
        print('A soma de {} e {} é igual à {}'.format(a,b,a+b))
    elif opc == 2:
        print('O produto de {} e {} é igual à {}'.format(a,b,a*b))
    elif opc == 3:
        maior= a if a>b else b
        print('O maior valor digitado foi {}'.format(maior))
    elif opc == 4: 
        a=int(input('Digite um número: '))
        b=int(input('Digite mais um número: '))
    elif opc == 5:
        break
    else:
        print('Opção inválida! Tente novamente.')
print('Programa encerrado!')
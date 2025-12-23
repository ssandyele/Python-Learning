#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))
if a>=b and a>=c:
    print('{} é o maior valor!'.format(a))
elif b>=c:
    print('{} é o maior valor!'.format(b))
else:
    print('{} é o maior valor!'.format(c))

if a<=b and a<=c:
    print('{} é o menor valor!'.format(a))
elif b<=c:
    print('{} é o menor valor!'.format(b))
else:
    print('{} é o menor valor!'.format(c))
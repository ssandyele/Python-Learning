# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num=int(input('Digite um número de 0 a 9999: '))
m=num//1000
c=(num%1000)//100
d=(num%100)//10
u=num%10
print('Seu número possui:')
print('{} unidade(s)'.format(u))
print('{} dezena(s)'.format(d))
print('{} centena(s)'.format(c))
print('{} milhar(es)'.format(m))
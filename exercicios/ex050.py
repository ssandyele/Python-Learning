# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma=0
for c in range (0,6):
    a=int(input('Digite um número inteiro: '))
    if a%2==0:
        soma += a
print('\nSoma dos números pares digitados: {}'.format(soma))
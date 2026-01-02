# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('PROGRESSÃO ARITMÉTICA')
a1=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão da PA: '))
print('='*30)
print('10 PRIMEIROS TERMOS DA PA')
for c in range (1, 11):
    a=a1+(c-1)*r
    print(a, end=' ')


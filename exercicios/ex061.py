# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

c=1
print('PROGRESSÃO ARITMÉTICA')
a1=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão da PA: '))

print('='*30)
print('10 PRIMEIROS TERMOS DA PA')

while c<11:
    a=a1+(c-1)*r
    print(a, end=' ')
    c += 1

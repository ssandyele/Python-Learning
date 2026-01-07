# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

fat=1
num=int(input('Digite um número para calcular seu fatorial: '))
n=num
print('Calculando {}! = {}'.format(num, num), end=" ")
while n>1:
    fat *= n
    n -= 1
    print ('x {}'.format(n), end=' ')
print('= {}\n'.format(fat))


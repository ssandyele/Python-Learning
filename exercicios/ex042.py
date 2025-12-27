# Refaça o DESAFIO 35 dos triângulos, acrescentando o 
# recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a=float(input('Digite o comprimento da primeira reta: '))
b=float(input('Digite o comprimento da segunda reta: '))
c=float(input('Digite o comprimento da terceira reta: '))

print('-'*50)
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        tipo='EQUILÁTERO'
    elif a!=b and b!=c and c!=a:
        tipo='ESCALENO'
    else:
        tipo='ISÓSCELES'
    print('Essas retas PODEM FORMAR um triângulo {}!'.format(tipo))
else:
    print('Essas retas NÃO PODEM FORMAR um triângulo!')
print('-'*50)


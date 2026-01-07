# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

c=1
total=0
print('PROGRESSÃO ARITMÉTICA')
a1=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão da PA: '))

print('='*30)
print('10 PRIMEIROS TERMOS DA PA')

while c<11:
    a=a1+(c-1)*r
    print(a, end=' ')
    c += 1
    total += 1

lim=int(input('\nQuantos termos você quer mostrar a mais? '))
total += lim
while lim != 0:
    cont = 0                       
    while cont < lim:                
        a += r
        print(a, end=' ')
        cont += 1
    lim = int(input('\nQuantos termos você quer mostrar a mais? '))
    total += lim
print('Progressão finalizada com {} termos mostrados.'.format(total))
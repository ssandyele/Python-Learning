#OPERADORES MATEMÁTICOS -------------------------------------------
# // divisão inteira
# % resto da divisão
# ** potenciação


n1=int(input('Digite um número: '))
n2=int(input('Digite mais um número: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
r=n1%n2
p=n1**n2
print('RESULTADO DA:\n Soma: {}, Multiplicação: {}, Divisão: {:.2f}'.format(s,m,d), end=', ')
print('Divisão inteira: {}, Resto da divisão: {}, Potenciação: {}'.format(di,r,p))
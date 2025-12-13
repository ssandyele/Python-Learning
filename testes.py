# APRENDENDO PYTHON
#ESSE ARQUIVO FOI CRIADO PARA MINHAS ANOTAÇÕES
#-----------------------------------------------
#print("Hello, World!")

#print(1+2)
#print('1'+'2')
#print('1+2')

#nome="Sandyele" 
#idade="18"
#print(nome,idade)

#name=input("Qual é o seu nome? ")
#age=input("Qual sua idade? ")
#print(name,age)

#nome=input("Qual seu nome? ")
#print("Olá",nome,"! Prazer em te conhecer!")

#dia=input("Dia - ")
#mes=input("Mês - ")
#ano=input("Ano - ")
#print("Você nasceu em",dia,"de",mes,"de",ano,". Correto?")

#TIPOS PRIMITIVOS -------------------------------------------

#a=int(input("Primeiro número - "))
#b=int(input("Segundo número - "))
#print("A soma é:",a+b)
#s=a+b
#print('A soma entre',a,'e',b,'é igual à',s)
#print('A soma entre {} e {} é igual à {}'.format(a,b,s))

#n1=input('Digite um número: ')
#print(type(n1))
#n2=int(input('Digite um número: '))
#print(type(n2))

#print('='*20)

#n=input('Qual seu nome? ')
#print('Olá {}!'.format(n))
#print('Olá {:20}!'.format(n))
#print("Olá {:>20}!".format(n))
#print("Olá {:<20}!".format(n))
#print('Olá {:^20}!'.format(n))
#print("Olá {:=^20}!".format(n))

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

